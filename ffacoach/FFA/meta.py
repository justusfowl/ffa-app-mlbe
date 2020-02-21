questions = [
    {
        "varname": "AKoft12_k",
        "actionable": {
            "incrVal": 1,
            "skipVals": [8],
            "maxVal": 9,
            "sug_en": "Reduce your alcohol consumption.",
            "sug_de": "Reduzieren Sie ihren Alkoholkonsum."
        },
        "q_de": "Wie oft trinken Sie Alkohol?",
        "q_en": "How often do you consume alcohol?",
        "type": "select",
        "meta": [
            {
                "val": 1,
                "display_en": "Daily",
                "display_de": "Täglich"
            },
            {
                "val": 2,
                "display_en": "Weekly",
                "display_de": "Wöchentlich"
            },
            {
                "val": 5,
                "display_en": "Monthly",
                "display_de": "Monatlich"
            },
            {
                "val": 7,
                "display_en": "Less than monthly",
                "display_de": "Weniger als monatlich"
            },
            {
                "val": 8,
                "display_en": "No more alcohol consumption",
                "display_de": "Kein Alkoholkonsum mehr"
            },
            {
                "val": 9,
                "display_en": "No alcohol consumption",
                "display_de": "Kein Alkoholkonsum"
            }
        ]
    },
    {
        "varname": "AMarztB",
        "q_de": "Haben Sie in den letzten zwei Wochen Medikamente eingenommen, die vom Arzt verschrieben wurden?",
        "q_en": "Did you take medications that have been prescribed by a doctor within the last two weeks?",
        "type": "binary",
        "meta": [
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            },
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            }
        ]
    },
    {
        "varname": "AMfrei",
        "actionable": {
            "targetVal": 2,
            "sug_en": "Contact your doctor to discuss your OTC supplements.",
            "sug_de": "Überdenken Sie Ihren Medikamentenplan - Kontaktieren Sie unsere Ärzte für eine Beratung."
        },
        "q_de": "Freie Präparate: Haben Sie in den letzten zwei Wochen Medikamente eingenommen, die nicht vom Arzt verschrieben wurden?",
        "q_en": "OTC Medication: Did you take medications that have not been prescribed by a doctor within the last two weeks?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "AUarbzD_k",
        "q_de": "Wie viele Wochen im letzten Jahr sind Sie krankheitsbedingt beruflich ausgefallen?",
        "q_en": "How many weeks last year did you miss work due to illness?",
        "type": "continuous",
        "meta": {
            "min": 0,
            "max": 53,
            "step": 1
        }
    },
    {
        "varname": "BBbehB",
        "q_de": "Haben Sie eine amtlich anerkannte Behinderung?",
        "q_en": "Do you have an officially recognized disability?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "BBblas12B",
        "q_de": "Litten Sie in den leztten 12 Monaten unter Harninkontinenz?",
        "q_en": "Have you suffered from urinary incontinence in the last 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "BBdors112",
        "q_de": "Hatten Sie in den letzten 12 Monaten Beschwerden im unteren Rücken?",
        "q_en": "Have you had lower back pain in the last 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {

        "varname": "BBdors212",
        "q_de": "Hatten Sie in den letzten 12 Monaten Beschwerden im Nacken / Halswirbelsäule?",
        "q_en": "Have you had  neck, cervical spin pain in the last 12 months? ",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "BBgehen",
        "q_de": "Haben Sie Schwierigkeiten beim Laufen ohne Gehhilfe auf 500m?",
        "q_en": "Do you have difficulty walking without a walking aid at 500m?",
        "type": "select",
        "meta": [
            {
                "val": 4,
                "display_en": "It is not possible for me / I'm not capable of doing",
                "display_de": "Es ist mir nicht möglich/Ich bin dazu nicht in der Lage"
            },
            {
                "val": 3,
                "display_en": "Great difficulties",
                "display_de": "Große Schwierigkeiten"
            },
            {
                "val": 1,
                "display_en": "No difficulties",
                "display_de": "Keine Schwierigkeiten"
            },
            {
                "val": 2,
                "display_en": "some difficulties",
                "display_de": "Einige Schwierigkeiten"
            }
        ]
    },
    {
        "varname": "BBmyo12",
        "q_de": "Haben Sie chronische Beschwerden nach einem Herzinfarkt innerhalb der letzten 12 Monate?",
        "q_en": "Do you have chronic complaints after a heart attack within the last 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            },
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            }

        ]
    },
    {
        "varname": "BBsa12",
        "q_de": "Haben Sie chronische Beschwerden nach einem Schlaganfall innerhalb der letzten 12 Monate?",
        "q_en": "Do you have chronic complaints after a stroke within the last 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "BBtreppe",
        "q_de": "Haben Sie Schwierigkeiten, eine Treppe mit mehr als 12 Stufen heraufzusteigen?",
        "q_en": "Do you have difficulty climbing stairs with more than 12 steps?",
        "type": "select",
        "meta": [
            {
                "val": 3,
                "display_en": "Great difficulties",
                "display_de": "Große Schwierigkeiten"
            },
            {
                "val": 2,
                "display_en": "some difficulties",
                "display_de": "Einige Schwierigkeiten"
            },
            {
                "val": 1,
                "display_en": "No difficulties",
                "display_de": "Keine Schwierigkeiten"
            },
            {
                "val": 4,
                "display_en": "It is not possible for me / I'm not capable of doing",
                "display_de": "Es ist mir nicht möglich/Ich bin dazu nicht in der Lage"
            }
        ]
    },
    {
        "varname": "ENgemBz1",
        "actionable": {
            "incrVal": 1,
            "skipVals": [],
            "maxVal": 10,
            "sug_en": "Enrich your diet with a little more vegetables.",
            "sug_de": "Reichern Sie Ihre Ernährung mit etwas mehr Gemüse an."
        },
        "q_de": "Verzehr von Gemüse: Wie viel Portionen Gemüse essen Sie pro Tag?",
        "q_en": "Consumption of vegetables: How many portions of vegetables do you eat per day?",
        "type": "continuous",
        "meta": {
            "min": 0,
            "max": 10,
            "step": 1
        }
    },
    {
        "varname": "ENobstBz1",
        "actionable": {
            "incrVal": 1,
            "skipVals": [],
            "maxVal": 10,
            "sug_en": "Enrich your diet with a little more fruit. ",
            "sug_de": "Reichern Sie Ihre Ernährung mit etwas mehr Obst an."
        },
        "q_de": "Verzehr von Obst: Wie viel Portionen Obst essen Sie pro Tag?",
        "q_en": "Consumption of fruit: How many portions of fruit do you eat per day?",
        "type": "continuous",
        "meta": {
            "min": 0,
            "max": 10,
            "step": 1
        }
    },
    {
        "varname": "GZmehm1",
        "q_de": "Wie schätzen Sie Ihren allgemeinen Gesundheitszustand ein?",
        "q_en": "How do you assess your general state of health?",
        "type": "select",
        "meta": [
            {
                "val": 4,
                "display_en": "Good",
                "display_de": "Gut"
            },
            {
                "val": 5,
                "display_en": "Very good",
                "display_de": "Sehr gut"
            },
            {
                "val": 2,
                "display_en": "Bad",
                "display_de": "Schlecht"
            },
            {
                "val": 3,
                "display_en": "Mediocre",
                "display_de": "Mittelmäßig"
            },
            {
                "val": 1,
                "display_en": "Very bad",
                "display_de": "Sehr schlecht"
            }
        ]
    },
    {
        "varname": "GZmehm2D",
        "q_de": "Wurden Sie durch eine Krankheit für mindestens 6 Monate in irgendeiner Art im Leben eingeschränkt?",
        "q_en": "Have you been limited in any way in your life by effects of a disease for at least 6 months?",
        "type": "select",
        "meta": [
            {
                "val": 3,
                "display_en": "No, not limited",
                "display_de": "Nein, nicht eingeschränkt"
            },
            {
                "val": 2,
                "display_en": "Yes, moderately restricted",
                "display_de": "Ja, mäßig eingeschränkt"
            },
            {
                "val": 1,
                "display_en": "Yes, strongly limited",
                "display_de": "Ja, stark eingeschränkt"
            }
        ]
    },
    {
        "varname": "GZmehm3C",
        "q_de": "Haben Sie chronische Krankheiten?",
        "q_en": "Do you have chronic diseases?",
        "type": "binary",
        "meta": [
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            },
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            }
        ]
    },
    {
        "varname": "GZsubj1",
        "actionable": {
            "incrVal": 1,
            "skipVals": [],
            "maxVal": 5,
            "sug_en": "Be aware about your health.",
            "sug_de": "Machen Sie sich Ihre Gesundheit ewtwas bewusster."
        },
        "q_de": "Wie stark achten Sie auf Ihre Gesundheit?",
        "q_en": "How health-concious would you rate yourself?",
        "type": "select",
        "meta": [
            {
                "val": 5,
                "display_en": "Very strong",
                "display_de": "Sehr stark"
            },
            {
                "val": 4,
                "display_en": "strongly",
                "display_de": "Stark"
            },
            {
                "val": 3,
                "display_en": "Mediocre",
                "display_de": "Mittelmäßig"
            },
            {
                "val": 2,
                "display_en": "Less strong",
                "display_de": "Weniger stark"
            },
            {
                "val": 1,
                "display_en": "Not at all",
                "display_de": "Gar nicht"
            }
        ]
    },
    {
        "varname": "IAarzt14B",
        "actionable": {
            "decrVal": 1,
            "skipVals": [],
            "minVal": 5,
            "sug_en": "Consider making an appointment for your dentist.",
            "sug_de": "Vielleicht würde Ihnen ein Termin beim Zahnarzt helfen?"
        },
        "q_de": "Wann war Ihre letzte zahnmedizinische Untersuchung?",
        "q_en": "When was your last dental examination?",
        "type": "select",
        "meta": [
            {
                "val": 1,
                "display_en": "Less than 6 months",
                "display_de": "Vor weniger als 6 Monaten"
            },
            {
                "val": 4,
                "display_en": "Never",
                "display_de": "Nie"
            },
            {
                "val": 2,
                "display_en": "6 to less than 12 months",
                "display_de": "Vor 6 bis weniger als 12 Monaten"
            },
            {
                "val": 3,
                "display_en": "12 months or more ago",
                "display_de": "Vor 12 Monaten oder länger"
            }
        ]
    },
    {
        "varname": "IAarzt1B4w",
        "q_de": "Wie oft haben Sie in den letzten 4 Wochen einen Allgemeinarzt oder Hausarzt aufgesucht?",
        "q_en": "How often have you visited a general practitioner or family doctor in the last 4 weeks?",
        "type": "continuous",
        "meta": {
            "min": 0,
            "max": 10,
            "step": 1
        }
    },
    {
        "varname": "IAarzt8C",
        "q_de": "Wurden Sie in den letzten 12 Monaten bei einem Psychologen vorstellig?",
        "q_en": "Have you seen a psychologist in the last 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "IAcholus",
        "actionable": {
            "targetVal": 1,
            "sug_en": "Get your blood fat determined. ",
            "sug_de": "Lassen Sie ihre Blutfettwerte überprüfen."
        },
        "q_de": "Wann war Ihre letzte Blutfettwertebestimmung?",
        "q_en": "When was your last blood fat determination?",
        "type": "select",
        "meta": [
            {
                "val": 1,
                "display_en": "Within the last 12 months",
                "display_de": "Innerhalb der letzten 12 Monate"
            },
            {
                "val": 4,
                "display_en": "more 5 years ago or",
                "display_de": "Vor 5 Jahren oder mehr"
            },
            {
                "val": 3,
                "display_en": "3 to less than 5 years",
                "display_de": "Vor 3 bis weniger als 5 Jahren"
            },
            {
                "val": 2,
                "display_en": "1 to less than 3 years",
                "display_de": "Vor 1 bis weniger als 3 Jahren"
            },
            {
                "val": 5,
                "display_en": "Never",
                "display_de": "Nie"
            }
        ]
    },
    {
        "varname": "IAdiabus",
        "actionable": {
            "targetVal": 1,
            "sug_en": "Get your blood suger level determined. ",
            "sug_de": "Lassen Sie Ihren Bluttzucker bestimmen."
        },
        "q_de": "Wann war Ihre letzte Blutzuckermessung?",
        "q_en": "When was your last blood glucose monitoring?",
        "type": "select",
        "meta": [
            {
                "val": 1,
                "display_en": "Within the last 12 months",
                "display_de": "Innerhalb der letzten 12 Monate"
            },
            {
                "val": 2,
                "display_en": "1 to less than 3 years",
                "display_de": "Vor 1 bis weniger als 3 Jahren"
            },
            {
                "val": 3,
                "display_en": "3 to less than 5 years",
                "display_de": "Vor 3 bis weniger als 5 Jahren"
            },
            {
                "val": 5,
                "display_en": "Never",
                "display_de": "Nie"
            },
            {
                "val": 4,
                "display_en": "more 5 years ago or",
                "display_de": "Vor 5 Jahren oder mehr"
            }
        ]
    },
    {
        "varname": "IAfa4w",
        "q_de": "Wie oft waren Sie i.d. letzten 4 Wochen beim Facharzt vorstellig?",
        "q_en": "How often have you been visiting a medical specialist in the past 4 weeks?",
        "type": "continuous",
        "meta": {
            "min": 0,
            "max": 10,
            "step": 1
        }
    },
    {
        "varname": "IAhypus",
        "actionable": {
            "targetVal": 1,
            "sug_en": "Get your blood pressure monitored.",
            "sug_de": "Lassen Sie sich den Blutdruck messen"
        },
        "q_de": "Wann war Ihre letzte Blutdruckmessung?",
        "q_en": "When was your last blood pressure test?",
        "type": "select",
        "meta": [
            {
                "val": 5,
                "display_en": "Never",
                "display_de": "Nie"
            },
            {
                "val": 4,
                "display_en": "more than 5 years ago",
                "display_de": "Vor 5 Jahren oder mehr"
            },
            {
                "val": 3,
                "display_en": "3 or less than 5 years",
                "display_de": "Vor 3 bis weniger als 5 Jahren"
            },
            {
                "val": 2,
                "display_en": "1 or less than 3 years",
                "display_de": "Vor 1 bis weniger als 3 Jahren"
            },
            {
                "val": 1,
                "display_en": "Within the last 12 months",
                "display_de": "Innerhalb der letzten 12 Monate"
            }
        ]
    },
    {
        "varname": "IAkfutyp2B_lz",
        "q_de": "Wann war Ihr letzter Stuhltest?",
        "q_en": "When was your last stool test?",
        "type": "select",
        "meta": [
            {
                "val": 1,
                "display_en": "Within the last 12 months",
                "display_de": "Innerhalb der letzten 12 Monate"
            },
            {
                "val": 5,
                "display_en": "Never",
                "display_de": "Nie"
            },
            {
                "val": 4,
                "display_en": "more 3 years ago or",
                "display_de": "Vor 3 Jahren oder mehr"
            },
            {
                "val": 3,
                "display_en": "2 to less than 3 years",
                "display_de": "Vor 2 bis weniger als 3 Jahren"
            },
            {
                "val": 2,
                "display_en": "1 to less than 2 years",
                "display_de": "Vor 1 bis weniger als 2 Jahren"
            }
        ]
    },
    {
        "varname": "IAkfutyp4B_lz",
        "q_de": "Wann war Ihre letzte Darmspiegelung?",
        "q_en": "When did you last have a colonoscopy?",
        "type": "select",
        "meta": [
            {
                "val": 4,
                "display_en": "more 10 years ago or",
                "display_de": "Vor 10 Jahren oder mehr"
            },
            {
                "val": 3,
                "display_en": "Before 5 to less than 10 years",
                "display_de": "Vor 5 bis weniger als 10 Jahren"
            },
            {
                "val": 2,
                "display_en": "1 to less than 5 years",
                "display_de": "Vor 1 bis weniger als 5 Jahren"
            },
            {
                "val": 1,
                "display_en": "Within the last 12 months",
                "display_de": "Innerhalb der letzten 12 Monate"
            },
            {
                "val": 5,
                "display_en": "Never",
                "display_de": "Nie"
            }
        ]
    },
    {
        "varname": "IAkhs",
        "q_de": "Wurden Sie in den letzten 12 Monaten stationär im Krankenhaus aufgenommen?",
        "q_en": "Have you been hospitalized in the past 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "IAkhs_k",
        "q_de": "Wie viele Nächste haben Sie stationär im Krankenhaus verbracht während der letzten 12 Moonate?",
        "q_en": "How many nights have you spent in a hospital in the past 12 months?",
        "type": "continuous",
        "meta": {
            "min": 0,
            "max": 365,
            "step": 7
        }
    },
    {
        "varname": "IApflege",
        "q_de": "Haben Sie in den letzten 12 Monaten den häuslichen Pflegedienst genutzt?",
        "q_en": "Have you used the home care service in the last 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            },
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            }
        ]
    },
    {
        "varname": "IAtermin",
        "q_de": "Hat sich bei Ihnen in den letzten 12 Monaten eine Untersuchung oder Behandlung verzögert, weil Sie zu lange auf einen Termin warten mussten?",
        "q_en": "Have you had a delayed examination or treatment in the last 12 months because you had to wait too long for an appointment?",
        "type": "select",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            },
            {
                "val": 3,
                "display_en": "No need for examination or treatment",
                "display_de": "Kein Bedarf an Untersuchung oder Behandlung"
            }
        ]
    },
    {
        "varname": "IAther2B",
        "actionable": {
            "targetVal": 1,
            "sug_en": "Potentially a visit with your physiotherapist would help?",
            "sug_de": "Eventuell würde Ihnen ein Besuch beim Physiotherapeuten helfen?"
        },
        "q_de": "Wurden Sie in den letzten 12 Monaten bei einem Physiotherapeuten vorstellig?",
        "q_en": "Have you visited a physiotherapists in the past 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "IAweg",
        "q_de": "Hat sich in den letzten 12 Monaten eine Untersuchung / Behandlung bei Ihnen verzögert, weil Ihr Termin zu weit entfernt war?",
        "q_en": "Has an examination / treatment been delayed in the last 12 months because your appointment was too far away?",
        "type": "select",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 3,
                "display_en": "No need for examination or treatment",
                "display_de": "Kein Bedarf an Untersuchung oder Behandlung"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "IPinfl4",
        "actionable": {
            "targetVal": 3,
            "sug_en": "Get informed about a flu vaccination - contact our staff for more information.",
            "sug_de": "Informieren Sie sich zur Grippeschutzimpfnug - Kontaktieren Sie unsere Team für eine Beratung."
        },
        "q_de": "Wann war Ihre letzte Grippeimpfung?",
        "q_en": "When was your last flu vaccination?",
        "type": "select",
        "meta": [
            {
                "val": 1,
                "display_en": "It's been too long (no vaccination in the past year)",
                "display_de": "Es ist zu lange her (Keine Impfung im vergangenen Jahr)"
            },
            {
                "val": 2,
                "display_en": "Never",
                "display_de": "Noch nie"
            },
            {
                "val": 3,
                "display_en": "vaccination date available",
                "display_de": "Impfdatum vorhanden"
            }
        ]
    },
    {
        "varname": "IPinfl6B",
        "actionable": {
            "incrVal": 1,
            "skipVals": [],
            "maxVal": 4,
            "sug_en": "Get informed about a flu vaccination - contact our staff for more information.",
            "sug_de": "Informieren Sie sich zur Grippeschutzimpfnug - Kontaktieren Sie unsere Team für eine Beratung."
        },
        "q_de": "Wie oft haben Sie die Grippeimpfung erhalten?",
        "q_en": "How often have you been vaccinated against the flu?",
        "type": "select",
        "meta": [
            {
                "val": 4,
                "display_en": "5 times",
                "display_de": "5 Mal"
            },
            {
                "val": 3,
                "display_en": "3-4 times",
                "display_de": "3-4 Mal"
            },
            {
                "val": 2,
                "display_en": "1-2 times",
                "display_de": "1-2 Mal"
            },
            {
                "val": 1,
                "display_en": "Not at all",
                "display_de": "Gar nicht"
            }
        ]
    },
    {
        "varname": "IPtet_lz",
        "actionable": {
            "targetVal": 1,
            "sug_en": "Get informed about a tetatnus vaccination - contact our staff for more information.",
            "sug_de": "Informieren Sie sich zur Tetanusimpfung - Kontaktieren Sie unsere Team für eine Beratung."
        },
        "q_de": "Wann war Ihre letzte Tetanusimpfung?",
        "q_en": "How long has the last tetanus vaccination been?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Less than 10 years",
                "display_de": "Weniger als 10 Jahre"
            },
            {
                "val": 2,
                "display_en": "10 years or more",
                "display_de": "10 Jahre oder länger"
            }
        ]
    },
    {
        "varname": "KAehispaq2",
        "actionable": {
            "incrVal": 1,
            "skipVals": [],
            "maxVal": 7,
            "sug_en": "Consider moving more by foot.",
            "sug_de": "Bauen Sie mehr Spaziergänge in Ihren Alltag ein."
        },
        "q_de": "An wie vielen Tagen in der Woche bewegen Sie sich zu Fuß fort?",
        "q_en": "How many days a week do you walk?",
        "type": "continuous",
        "meta": {
            "min": 0,
            "max": 7,
            "step": 1
        }
    },
    {
        "varname": "KAehispaq4",
        "actionable": {
            "incrVal": 1,
            "skipVals": [],
            "maxVal": 7,
            "sug_en": "Consider moving more by bicycle (days / week).",
            "sug_de": "Versuchen Sie's mal mit dem Fahrrad - zur Arbeit oder im Fitnessstudio (Tage / Woche)."
        },
        "q_de": "An wie vielen Tagen in der Woche benutzen Sie das Fahrrad?",
        "q_en": "How many days a week do you use the bicycle?",
        "type": "continuous",
        "meta": {
            "min": 0,
            "max": 7,
            "step": 1
        }
    },
    {
        "varname": "KAehispaq8",
        "actionable": {
            "incrVal": 1,
            "skipVals": [],
            "maxVal": 7,
            "sug_en": "Work out to strengthen your muscles (days / week).",
            "sug_de": "Muskeltraining ist gut für Kräftigung und Ballance (Tage / Woche)."
        },
        "q_de": "An wie vielen Tagen in der Woche führen Sie Kräftigungsübungen durch?",
        "q_en": "How many days a week do you do strengthening exercises?",
        "type": "continuous",
        "meta": {
            "min": 0,
            "max": 7,
            "step": 1
        }
    },
    {
        "varname": "KAgfa",
        "actionable": {
            "targetVal": 1,
            "sug_en": "Try enriching your week with some cardio workout for at least 2 days a week.",
            "sug_de": "Versuchen Sie an 2 Tagen pro Woche Ausdauersport. Z.B. Fahrradfahren."
        },
        "q_de": "Betätigen Sie sich mindestens 2x in der Woche mit Ausdauersport in Summe >= 2 Stunden (z.B. Fahrradfahren)?",
        "q_en": "Do you engage in endurance sports at least twice a week for a total of >= 2 hours (e.g. cycling)?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KAgfka",
        "actionable": {
            "targetVal": 1,
            "sug_en": "Try going for a walk here and there - 150min / week can already make a difference.",
            "sug_de": "Versuchen Sie Spaziergänge in Ihren Alltag zu integrieren - 150 Minuten / Woche machen bereits einen Unterschied.."
        },
        "q_de": "Betätigen Sie sich gemäß der WHO Empfehlung mindestens 150 Min. in der Woche aerobe köperlich aktiv (incl. Gehen)?",
        "q_en": "According to WHO recommendations, are you physically active aerobically for at least 150 min/week (including walking)?",
        "type": "binary",
        "meta": [
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            },
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            }
        ]
    },
    {
        "varname": "KAgfka1",
        "actionable": {
            "targetVal": 1,
            "sug_en": "Try going for some physical exercise at least 2 hrs per week.",
            "sug_de": "Versuchen Sie mindestens 2 Stunden / Woche körperlich zu betätigen."
        },
        "q_de": "Betätigen Sie sich in der Woche mind. 2 Stunden körperlich aktiv (ohne Gehen)?",
        "q_en": "Are you physically active for at least 2 hours per week (without walking)?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KAgfmk",
        "actionable": {
            "targetVal": 1,
            "sug_en": "Try going for some muscle strengthening at least 2 hrs oper week.",
            "sug_de": "Versuchen Sie mindestens 2 Stunden / Woche Kräftigungstraining."
        },
        "q_de": "Führen Sie Muskelkräftigung aus (mind. 2x in der Woche)?",
        "q_en": "Do you carry out muscle strengthening (at least twice a week)?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KAspodauC_k",
        "actionable": {
            "incrVal": 30,
            "skipVals": [],
            "maxVal": 900,
            "sug_en": "Increase your sporting activity by 30 minutes per week",
            "sug_de": "Erhöhen Sie Ihre sportliche Aktivität um 30 Minuten in der Woche"
        },
        "q_de": "Wie viel Sport pro Woche machen Sie insgesamt (in Minuten)",
        "q_en": "How much sport you do per week in total (in minutes)",
        "type": "continuous",
        "meta": {
            "min": 0,
            "max": 900,
            "step": 30
        }
    },
    {
        "varname": "KHab12",
        "q_de": "Hatten Sie in den letzten 12 Monaten Asthma?",
        "q_en": "Did you have asthma in the past 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            },
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            }
        ]
    },
    {
        "varname": "KHalgi112",
        "q_de": "Hatten Sie in den letzten 12 Monaten Allergien?",
        "q_en": "Did you suffer from allergies in the past 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHcb12",
        "q_de": "Hatten Sie in den letzten 12 Monaten chronische Bronchitis?",
        "q_en": "Did you suffer from Chronic bronchitis in the past 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHced12",
        "q_de": "Hatten Sie in den letzten 12 Monaten eine chronische entzündliche Darmerkrankung?",
        "q_en": "Did you have an inflammatory bowel disease in the past 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHcle12",
        "q_de": "Hatten Sie andere chronische Lebererkrankungen in den letzten 12 Monaten?",
        "q_en": "Did you have other chronic liver diseases in the last 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHdge12",
        "q_de": "Hatten Sie in den letzten 12 Monaten Arthrose?",
        "q_en": "Did you suffer from osteoarthritis in the last 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHdiabB12",
        "q_de": "Litten Sie in den letzten 12 Monaten an Diabetis?",
        "q_en": "Have you been diabetic in the last 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            },
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            }
        ]
    },
    {
        "varname": "KHhi12",
        "q_de": "Hatten Sie in den letzten 12 Monaten eine Herzinsuffizienz?",
        "q_en": "Did you have a heart failure in the last 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHhyp",
        "q_de": "Wurde bei Ihnen jemals Bluthochdruck diagnostiziert?",
        "q_en": "Have you ever been diagnosed with hypertension?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHhyp12",
        "q_de": "Hatten Sie in den letzten 12 Monaten Bluthochdruck?",
        "q_en": "Have you had hypertension in the last 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            },
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            }
        ]
    },
    {
        "varname": "KHhyp12pB",
        "q_de": "Wurde in den letzten 12 Monaten bei Ihnen ärztlich Bluthochdruckdruck diagnostiziert?",
        "q_en": "Have you been medically diagnosed with high blood pressure in the last 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            },
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            }
        ]
    },
    {
        "varname": "KHhypmedC",
        "q_de": "Nehmen Sie blutdrucksenkende Mittel aufgrund einer bekannten Hypertonie ein?",
        "q_en": "Are you taking antihypertensive medication for a known hypertension?",
        "type": "binary",
        "meta": [
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            },
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            }
        ]
    },
    {
        "varname": "KHkarz12",
        "q_de": "Hatten Sie eine Krebserkrankung in den letzten 12 Monaten?",
        "q_en": "Have you been diagnosed with cancer in the past 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHkhk12",
        "q_de": "Hatten Sie in den letzten 12 Monaten eine koronare Herzerkrankung/Angina Pectoris?",
        "q_en": "Have you had coronary artery disease / angina pectoris in the last 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHbbmyo12",
        "q_de": "Hatten Sie in den letzten 12 Monaten chronische Probleme mit Ihrem Herz / Herzinfarkt?",
        "q_en": "Have you had chronical issues with your heart / heart attack in the last 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHlip12A",
        "q_de": "Hatten Sie in den letzten 12 Monaten erhöhte Blutfette oder Cholesterien?",
        "q_en": "Have you had elevated blood lipids or cholesterol in the last 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHlipA",
        "q_de": "Wurde bei Ihnen jemals ärztlich erhöhte Blutfette/Cholesterinwerte diagnostiziert?",
        "q_en": "Have you ever been diagnosed with elevated blood lipids or cholesterol?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHlipmedA",
        "q_de": "Nehmen Sie aktuell Medikamente ein aufgrund erhöhten Cholesterins?",
        "q_en": "Are you currently taking medication for high cholesterol?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHlz12",
        "q_de": "Hatten Sie in den letzten 12 Monaten eine Leberzirrhose?",
        "q_en": "Have you had cirrhosis of the liver in the last 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHmyo12",
        "q_de": "Hatten Sie in den letzten 12 Monaten einen Herzinfarkt?",
        "q_en": "Did you have a heart attack in the past 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHniB12",
        "q_de": "Hatten Sie chronische Nierenprobleme in den letzten 12 Monaten?",
        "q_en": "Have you had chronic kidney problems in the past 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHos12",
        "q_de": "Hatten Sie Osteoporose in den letzten 12 Monaten?",
        "q_en": "Have you had Osteoporosis in the past 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHra12",
        "q_de": "Hatten Sie Arthritis in den letzten 12 Monaten?",
        "q_en": "Have you had arthritis in the past 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            },
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            }
        ]
    },
    {
        "varname": "KHsa12",
        "q_de": "Hatten Sie in den letzten 12 Monaten einen Schlaganfall?",
        "q_en": "Have you had a stroke in the past 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "KHulc12",
        "q_de": "Hatten Sie in den letzten 12 Monaten ein Magen- oder Zwölffingerdarmgeschwür?",
        "q_en": "Have you had a gastric or duodenal ulcer in the past 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            },
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            }
        ]
    },
    {
        "varname": "LQsf367C",
        "q_de": "Hatten Sie in den letzten 4 Wochen Schmerzen? Falls, ja, wie stark waren diese?",
        "q_en": "Have you had any pain in the last four weeks? If so, how severe were they?",
        "type": "select",
        "meta": [
            {
                "val": 3,
                "display_en": "Light",
                "display_de": "Leicht"
            },
            {
                "val": 6,
                "display_en": "Very strong",
                "display_de": "Sehr stark"
            },
            {
                "val": 5,
                "display_en": "strongly",
                "display_de": "Stark"
            },
            {
                "val": 4,
                "display_en": "Moderate",
                "display_de": "Mäßig"
            },
            {
                "val": 2,
                "display_en": "Very easy",
                "display_de": "Sehr leicht"
            },
            {
                "val": 1,
                "display_en": "No pain",
                "display_de": "Keine Schmerzen"
            }
        ]
    },
    {
        "varname": "LQsf368C",
        "q_de": "Litten Sie an Behinderung in Alltagstätigkeiten durch Schmerzen in den letzetn 4 Wochen?",
        "q_en": "Have you suffered from disability in everyday activities due to pain in the last 4 weeks?",
        "type": "select",
        "meta": [
            {
                "val": 5,
                "display_en": "Very",
                "display_de": "Sehr"
            },
            {
                "val": 4,
                "display_en": "Quite",
                "display_de": "Ziemlich"
            },
            {
                "val": 3,
                "display_en": "Moderate",
                "display_de": "Mäßig"
            },
            {
                "val": 2,
                "display_en": "Something",
                "display_de": "Etwas"
            },
            {
                "val": 1,
                "display_en": "Not at all",
                "display_de": "Überhaupt nicht"
            }
        ]
    },
    {
        "varname": "LQzufrB10",
        "q_de": "Wie zufrieden sind Sie mit Ihrem Leben insgesamt (10=total zufrieden)?",
        "q_en": "How satisfied are you with your life overall (10=totally satisfied)?",
        "type": "continuous",
        "meta": {
            "min": 0,
            "max": 10,
            "step": 1
        }
    },
    {
        "varname": "PKdep12",
        "q_de": "Hatten Sie eine Depression in den letzten 12 Monaten?",
        "q_en": "Have you had a depression in the last 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },
    {
        "varname": "RCstat",
        "actionable": {
            "incrVal": 1,
            "skipVals": [3],
            "maxVal": 4,
            "sug_en": "Reduce smoking",
            "sug_de": "Verringern Sie Ihr Rauchverhalten."
        },
        "q_de": "Rauchen Sie?",
        "q_en": "Do you smoke?",
        "type": "select",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes, daily",
                "display_de": "Ja, täglich"
            },
            {
                "val": 2,
                "display_en": "Yes, occasionally",
                "display_de": "Ja, gelegentlich"
            },
            {
                "val": 3,
                "display_en": "No not more",
                "display_de": "Nein, nicht mehr"
            },
            {
                "val": 4,
                "display_en": "Have never smoked",
                "display_de": "Habe noch nie geraucht"
            }
        ]
    },
    {
        "varname": "SFoslo1C",
        "q_de": "Wie viele Personen, würden Sie als Ihnen 'nahe stehend' bezeichnen?",
        "q_en": "How many people would you describe as 'close friends/relatives'?",
        "type": "select",
        "meta": [

            {
                "val": 2,
                "display_en": "1 to 2",
                "display_de": "1 bis 2"
            },
            {
                "val": 3,
                "display_en": "3 to 5",
                "display_de": "3 bis 5"
            },
            {
                "val": 4,
                "display_en": "6 or more",
                "display_de": "6 oder mehr"
            },
            {
                "val": 1,
                "display_en": "No",
                "display_de": "Keine"
            }
        ]
    },
    {
        "varname": "SFoslo3A",
        "q_de": "Wie schwierig ist es für sie, in schwierigen Lebenssituationen von Ihnen nahestehenden Personen zu erbitten?",
        "q_en": "How difficult is it for you to ask people close to you in difficult life situations for help?",
        "type": "select",
        "meta": [
            {
                "val": 1,
                "display_en": "Very difficult",
                "display_de": "Sehr schwierig"
            },
            {
                "val": 2,
                "display_en": "Difficult",
                "display_de": "Schwierig"
            },
            {
                "val": 4,
                "display_en": "Simple",
                "display_de": "Einfach"
            },
            {
                "val": 3,
                "display_en": "Possible",
                "display_de": "Möglich"
            },
            {
                "val": 5,
                "display_en": "Very easy",
                "display_de": "Sehr einfach"
            }
        ]
    },
    {
        "varname": "SFosloA",
        "q_de": "Wie schätzen Sie soziale Unterstützung ein, die Sie durch Ihre Familie, Freunde und Angehörige erfahren?",
        "q_en": "How do you rate the social support you receive from your family, friends and loved ones?",
        "type": "select",
        "meta": [
            {
                "val": 3,
                "display_en": "strong support",
                "display_de": "Starke Unterstützung"
            },
            {
                "val": 1,
                "display_en": "little support",
                "display_de": "Geringe Unterstützung"
            },
            {
                "val": 2,
                "display_en": "medium support",
                "display_de": "Mittlere Unterstützung"
            }
        ]
    },
    {
        "varname": "SHhoer1",
        "q_de": "Nutzen Sie ein Hörgerät?",
        "q_en": "Are you using a hearing aid?",
        "type": "select",
        "meta": [
            {
                "val": 3,
                "display_en": "I'm hard of hearing or deaf",
                "display_de": "Ich bin hochgradig schwerhörig oder gehörlos"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            },
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            }
        ]
    },
    {
        "varname": "SHseh1",
        "q_de": "Haben Sie eine Brille oder Kontaktlinsen?",
        "q_en": "Do you wear glasses or contacts?",
        "type": "select",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            },
            {
                "val": 3,
                "display_en": "I am severely visually impaired or can not see",
                "display_de": "Ich bin stark sehbehindert oder kann nicht sehen"
            }
        ]
    },
    {
        "varname": "flagHadAccident",
        "q_de": "Hatten Sie in den letzten 12 Monaten einen Unfall, durch den Sie verletzt wurden?",
        "q_en": "Have you had an accident through which you were injured within the past 12 months?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    },

    # imputed / generated questions:
    {
        "varname": "IAarzt_general4w",
        "q_de": "Hatten Sie in den letzten 4 Wochen irgendeinen Arztbesuch?",
        "q_en": "Did you see any doctor within the last four weeks?",
        "type": "binary",
        "meta": [
            {
                "val": 1,
                "display_en": "Yes",
                "display_de": "Ja"
            },
            {
                "val": 2,
                "display_en": "No",
                "display_de": "Nein"
            }
        ]
    }

]