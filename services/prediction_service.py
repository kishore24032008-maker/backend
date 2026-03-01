def calculate_risk(data):
    score = (
        data.attendance * 0.4 +
        data.study_hours * 5 +
        data.previous_grades * 0.5
    )

    return "High" if score < 100 else "Low"


def predict_student_risk(data):
    return {"risk": calculate_risk(data)}