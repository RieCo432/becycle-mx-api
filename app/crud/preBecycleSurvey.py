from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import app.models as models
import app.schemas as schemas


def create_pre_becycle_survey_entry(db: Session, survey_answers: schemas.PreBecycleSurvey) -> None:
    survey_entry = models.PreBecycleSurvey(**survey_answers.model_dump())

    try:
        db.add(survey_entry)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"description": "Something went wrong"})