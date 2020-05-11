import os
from flask import Flask, flash, request, redirect, url_for, jsonify, make_response
from werkzeug.utils import secure_filename
import datetime as dt
import pytz

from FFA.Coach import Coach



def initAPI():

    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER")

    app = Flask(__name__)
    app.secret_key = os.environ.get("API_SECRET")
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


    @app.route('/hb', methods=['get'])
    def hb():
        data = {'message': 'OK', 'code': 'SUCCESS'}
        return make_response(jsonify(data), 201)

    @app.route('/coach/meta', methods=['get'])
    def coachMeta():
        ffaCoach = Coach()
        meta = ffaCoach.get_meta()
        return make_response(jsonify(meta), 201)

    @app.route('/coach/simple', methods=["post"])
    def simple():
        ffaCoach = Coach()

        try:

            body = request.get_json(force=True)
            inputVector = body["inputVector"]

            df_pred, df_new_records = ffaCoach.u(inputVector)

            data = {
                'message': 'OK',
                'code': 'SUCCESS',
                'evalDate': str(dt.datetime.now(pytz.utc))
            }

            return make_response(jsonify(data), 201)

        except Exception as e:
            print(e)
            score = -1

            data = {
                'message': str(e),
                'code': 'ERROR',
                'GZmehm01_score': int(score),
                'evalDate': str(dt.datetime.now(pytz.utc)),
                'evalDetails': [],
                'suggestions': []
            }

            return make_response(jsonify(data), 500)


    @app.route('/coach/info', methods=['get'])
    def coachInfo():
        ffaCoach = Coach()
        model_predictors = ffaCoach.get_model_predictors()
        data = {'message': 'OK', 'code': 'SUCCESS', 'predictors': model_predictors}
        return make_response(jsonify(data), 201)

    @app.route('/coach', methods=['post'])
    def coach():

        ffaCoach = Coach()

        try:
            body = request.get_json(force=True)
            inputVector = body["inputVector"]
        except:
            flash('No body sent')
            return redirect(request.url)

        df_pred, df_improvements = ffaCoach.get_wellbeing_improvements(inputVector)

        try:
            score = df_pred["predict"]

            data = {
                'message': 'OK',
                'code': 'SUCCESS',
                'GZmehm01_score': int(score),
                'evalDate': str(dt.datetime.now(pytz.utc)),
                'evalDetails': df_pred,
                'suggestions': df_improvements.to_dict("records")
            }

            return make_response(jsonify(data), 201)

        except Exception as e:
            print(e)
            score = -1

            data = {
                'message': str(e),
                'code': 'ERROR',
                'GZmehm01_score': int(score),
                'evalDate': str(dt.datetime.now(pytz.utc)),
                'evalDetails': [],
                'suggestions': []
            }

            return make_response(jsonify(data), 500)

    return app


app = initAPI()