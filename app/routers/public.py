import datetime

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
import app.crud as crud
import app.schemas as schemas
import app.models as models
import app.dependencies as dep
from datetime import time


public = APIRouter(
    tags=["public"],
    dependencies=[Depends(dep.get_db)],
    responses={404: {"description": "Not Found"}}
)


@public.get("/public/opening-times")
def get_opening_times(db: Session = Depends(dep.get_db)) -> list[schemas.DayOpeningTimes]:
    return crud.get_opening_times(db=db)


@public.get("/public/opening-days")
def get_opening_days(db: Session = Depends(dep.get_db)) -> list[int]:
    return crud.get_opening_week_days(db=db)


@public.get("/public/opening-hours")
def get_opening_hours(db: Session = Depends(dep.get_db)) -> dict[str, time]:
    return crud.get_opening_hours(db=db)


@public.get("/public/slot-duration")
def get_slot_duration(db: Session = Depends(dep.get_db)) -> int:
    return crud.get_slot_duration(db=db)


@public.get("/public/next-closed-day")
def get_next_closed_day(db: Session = Depends(dep.get_db)) -> schemas.ClosedDay:
    return crud.get_closed_days(db=db, start_date=datetime.datetime.utcnow())[0]
