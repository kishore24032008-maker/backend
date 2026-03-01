def predict_student_risk(data):
    score = (
        data.attendance * 0.4 +
        data.study_hours * 5 +
        data.previous_grades * 0.5
    )

    if score < 100:
        return {"risk": "High"}
    else:
        return {"risk": "Low"}