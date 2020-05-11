
import os
import h2o
import pandas as pd
import uuid
from .meta import questions
import copy

h2o.connect(ip="localhost")

class Coach:

    def __init__(self):

        self.model = h2o.load_model(os.environ.get("COACH_MODEL")) # import_mojo(os.environ.get("COACH_MODEL"))

        self._get_actionable_q()

    def get_model_predictors(self):
        var_imp = self.model._model_json['output']['variable_importances'].as_data_frame()
        return var_imp["variable"]

    def _prepare_evaluation(self, df_input):
        all_predictors = self.get_model_predictors()

        for p in all_predictors:
            if not p in df_input:
                print("Warning: %s missing in inputVector" % p)
            else:
                try:
                    df_input[p] = pd.to_numeric(df_input[p])
                except:
                    print("Warning: %s cannot be converted to numeric in inputVector" % p)

        return df_input

    def get_meta(self):
        return questions

    def estimate_wellbeing(self, input_):

        try:

            if isinstance(input_, dict):
                print("dict")
                df_input = pd.DataFrame(input_)
            elif isinstance(input_, list):
                print("list")
                df_input = pd.DataFrame(input_)
            elif isinstance(input_, pd.DataFrame):
                print("PD")
            else:
                raise ValueError('Only dictionary, list or pandas dataframe are supported for prediction.')

            # input_vector needs to be a python dictionary, no list!
            df_input = self._prepare_evaluation(df_input)

            df_eval = h2o.H2OFrame(df_input)

            pred = self.model.predict(df_eval)

            df_out = pred.as_data_frame()

            return df_out

        except Exception as e:

            return None

    def _get_evaluation(self, df_eval):
        try:
            pred = self.model.predict(df_eval)
            df_out = pred.as_data_frame()

            return df_out.to_dict("records")[0]

        except Exception as e:

            return None

    def get_simple_prediction(self, inputVector):
        try:
            # input_vector needs to be a python dictionary, no list!
            df_eval = self._prepare_evaluation(inputVector)

            df_predicted = self._get_evaluation(df_eval)

            return df_predicted
        except Exception as e:
            print(e)
            return None, None

    def simulate_input_vectors(self, inputVector):

        copy_inputVector = inputVector.copy()

        try:
            _uuid = "df_" + str(uuid.uuid1())

            copy_inputVector = self._prepare_evaluation(copy_inputVector)

            copy_inputVector["_id"] = _uuid
            copy_inputVector["_id_parent"] = None
            copy_inputVector["new"] = 0

            new_records = self.get_improvement_prep(copy_inputVector)

            return copy_inputVector, new_records
        except Exception as e:
            print(e)
            return None, None

    def get_wellbeing_improvements(self, inputVector):

        try:
            # input_vector needs to be a python dictionary, no list!
            df_eval = self._prepare_evaluation(inputVector)

            df_predicted = self._get_evaluation(df_eval)

            try:
                score = df_predicted["predict"]
            except:
                score = -1

            if score > 0:
                if score < 5:
                    next_score = int(score) + 1
                else:
                    next_score = 5

                base_line = df_predicted["p" + str(next_score)]

                df_improvements = self.analyze_improvements(df_eval, next_score, base_line)
                return df_predicted, df_improvements
            else:
                return None, None

        except Exception as e:
            print(e)
            return None, None

    @staticmethod
    def _validate_q_meta_item(q, val):

        flag_itm_exists = False
        found_itm = None

        if q["type"] in ["binary", "select"]:
            for itm in q["meta"]:
                if float(itm["val"]) == float(val):
                    flag_itm_exists = True
                    found_itm = itm
                    break
        elif q["type"] == 'continuous':
            if q["meta"]["min"] <= val and q["meta"]["max"] >= val:
                flag_itm_exists = True
                found_itm = {
                    "key" : float(val)
                }

        return flag_itm_exists, found_itm

    def _get_next_val(self, q, curr_val):

        action_meta = q["actionable"]

        # what is the current value of the answer?
        # init_val = curr_val.as_data_frame().iloc[:, 0].values[0]
        _, init_val_itm = self._validate_q_meta_item(q, curr_val)

        iterate_val = float(curr_val)

        next_val_out = None

        if "incrVal" in action_meta:

            flag_running = True

            while flag_running:
                iterate_val += float(action_meta["incrVal"])

                flag_itm_exists, next_val_itm = self._validate_q_meta_item(q, iterate_val)

                if flag_itm_exists:
                    if iterate_val not in action_meta["skipVals"]:
                        next_val_out = iterate_val

                if next_val_out is not None:
                    break

                if iterate_val > float(action_meta["maxVal"]):
                    flag_running = False

        if "decrVal" in action_meta:

            flag_running = True

            while flag_running:
                iterate_val -= float(action_meta["decrVal"])

                flag_itm_exists, next_val_itm = self._validate_q_meta_item(q, iterate_val)

                if flag_itm_exists:
                    if iterate_val not in action_meta["skipVals"]:
                        next_val_out = iterate_val

                if next_val_out is not None:
                    break

                if iterate_val < float(action_meta["minVal"]):
                    flag_running = False

        if "targetVal" in action_meta:

            if not action_meta["targetVal"] == iterate_val:

                flag_itm_exists, next_val_itm = self._validate_q_meta_item(q, action_meta["targetVal"])

                if flag_itm_exists :
                    next_val_out = action_meta["targetVal"]

        if next_val_out is not None:
            return True, next_val_out, next_val_itm, init_val_itm, action_meta
        else:
            return False, next_val_out, None, init_val_itm, action_meta

    def get_improvement_prep(self, input_vector):

        new_records = []

        for q in self.actionable_q:

            try:

                _uuid = "df_" + str(uuid.uuid1())

                df_mod = input_vector.copy()
                # df_mod = h2o.deep_copy(df_eval, _uuid)

                impr = {
                    "varname": q["varname"]
                }
                # modify single variable by increment / decrement

                flag_re_run = False

                if "actionable" in q:

                    curr_val = df_mod[q["varname"]]

                    flag_re_run, new_val, new_val_itm, init_val_itm, action_meta = self._get_next_val(q, curr_val)

                    if flag_re_run:
                        df_mod[q["varname"]] = new_val

                        df_mod["_changed"] = q["varname"]

                        #df_out = df_mod.as_data_frame()
                        #this_dict = df_out.to_dict()
                        df_mod["new"] = 1
                        df_mod["_id"] = None
                        df_mod["_id_parent"] = input_vector["_id"]

                        new_records.append(df_mod)

            except Exception as e:
                print(e)

        return new_records

    def analyze_improvements(self, df_eval, target_class, base_line_scoring):

        improvement_results = []

        for q in self.actionable_q:

            try:

                _uuid = "df_" + str(uuid.uuid1())

                df_mod = h2o.deep_copy(df_eval, _uuid)

                impr = {
                    "varname": q["varname"]
                }
                # modify single variable by increment / decrement

                flag_re_run = False

                if "actionable" in q:

                    curr_val = df_mod[q["varname"]]

                    flag_re_run, new_val, new_val_itm, init_val_itm, action_meta  = self._get_next_val(q, curr_val)

                    if flag_re_run:
                        df_mod[q["varname"]] = new_val

                    # print(df_mod[q["varname"]])

                if flag_re_run:
                    # predict with slightly modified feature vector

                    df_prediction = self._get_evaluation(df_mod)

                    impr["p" + str(target_class)] = float(df_prediction["p" + str(target_class)])
                    impr["target_class" ] = str(target_class)
                    impr["meta"] = action_meta
                    impr["new_val_itm"] = new_val_itm
                    impr["init_val_itm"] = init_val_itm
                    impr["delta"] = float(df_prediction["p" + str(target_class)]) - base_line_scoring

                    improvement_results.append(impr)

            except Exception as e:
                print(e)

        df_improvements = pd.DataFrame(improvement_results)
        df_improvements.sort_values(by="delta", ascending=False, inplace=True)

        df_improvements = df_improvements[df_improvements["delta"]>0]

        return df_improvements

    def _get_actionable_q(self):
        self.actionable_q = []
        for q in questions:
            if "actionable" in q:
                self.actionable_q.append(q)