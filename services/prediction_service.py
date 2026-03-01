from schemas.student_schema import StudentRequest, StudentResponse, RiskExplanation
from utils.helpers import calculate_percentage


class PredictionService:

    def calculate_prediction(self, student: StudentRequest) -> StudentResponse:

        attendance_risk = 0.4 * (1 - student.attendance / 100)
        marks_risk = 0.4 * (1 - student.internal_marks / 100)
        lms_risk = 0.2 * (1 - student.lms_activity_score / 100)

        total_risk = attendance_risk + marks_risk + lms_risk

        academic_health_score = int(
            student.attendance * 0.4 +
            student.internal_marks * 0.4 +
            student.lms_activity_score * 0.2
        )

        if total_risk < 0.3:
            risk_level = "LOW"
        elif total_risk < 0.6:
            risk_level = "MEDIUM"
        else:
            risk_level = "HIGH"

        alert_message = None
        if risk_level == "HIGH":
            alert_message = "Immediate academic intervention required."

        explanation = RiskExplanation(
            attendance_contribution_percent=calculate_percentage(attendance_risk, total_risk),
            internal_marks_contribution_percent=calculate_percentage(marks_risk, total_risk),
            lms_activity_contribution_percent=calculate_percentage(lms_risk, total_risk),
        )

        return StudentResponse(
            student_id=student.student_id,
            risk_probability=round(total_risk, 2),
            risk_level=risk_level,
            academic_health_score=academic_health_score,
            alert=alert_message,
            risk_explanation=explanation
        )