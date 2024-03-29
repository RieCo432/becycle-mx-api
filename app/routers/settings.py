from fastapi import APIRouter, Depends, Body
import app.schemas as schemas
import app.crud as crud
import app.dependencies as dep
from uuid import UUID
from sqlalchemy.orm import Session
import app.models as models
from typing import Annotated
from datetime import date, time

settings = APIRouter(
    tags=["settings"],
    dependencies=[Depends(dep.get_db), Depends(dep.get_current_active_user)],
    responses={404: {"description": "Not Found"}}
)


@settings.get("/settings/appointments/general", dependencies=[Depends(dep.get_current_active_user)])
async def get_appointment_general_settings(
        db: Session = Depends(dep.get_db)) -> schemas.AppointmentGeneralSettings:

    return crud.get_appointment_general_settings(db=db)


@settings.patch("/settings/appointments/general", dependencies=[Depends(dep.get_current_appointment_manager_user)])
async def update_appointment_general_settings(
        updated_appointment_settings: schemas.PatchAppointmentGeneralSettings,
        db: Session = Depends(dep.get_db)
) -> schemas.AppointmentGeneralSettings:
    return crud.update_appointment_general_settings(db=db, updated_appointment_settings=updated_appointment_settings)


@settings.get("/settings/appointments/concurrency", dependencies=[Depends(dep.get_current_active_user)])
async def get_appointment_concurrency_limits(
        db: Session = Depends(dep.get_db)) -> list[schemas.AppointmentConcurrencyLimit]:

    return crud.get_appointment_concurrency_limits(db=db)


@settings.post("/settings/appointments/concurrency", dependencies=[Depends(dep.get_current_appointment_manager_user)])
async def create_appointment_concurrency_limit(
        appointment_concurrency_limit_data: schemas.AppointmentConcurrencyLimit,
        db: Session = Depends(dep.get_db)) -> schemas.AppointmentConcurrencyLimit:

    return crud.add_appointment_concurrency_limit(
        db=db,
        appointment_concurrency_limit_data=appointment_concurrency_limit_data)


@settings.delete("/settings/appointments/concurrency/{after_time}", dependencies=[Depends(dep.get_current_appointment_manager_user)])
async def update_appointment_concurrency_limit(
        after_time: time,
        db: Session = Depends(dep.get_db)) -> None:
    crud.delete_appointment_concurrency_limit(db=db, after_time=after_time)



@settings.patch("/settings/appointments/concurrency/{after_time}", dependencies=[Depends(dep.get_current_appointment_manager_user)])
async def update_appointment_concurrency_limit(
        after_time: time,
        new_appointment_concurrency_limit_data: schemas.PatchAppointmentConcurrencyLimit,
        db: Session = Depends(dep.get_db)) -> schemas.AppointmentConcurrencyLimit:
    return crud.patch_appointment_concurrency_limit(db=db, after_time=after_time, new_appointment_concurrency_limit_data=new_appointment_concurrency_limit_data)


@settings.get("/settings/closed-days", dependencies=[Depends(dep.get_current_active_user)])
async def get_closed_days(start_date: date | None = None, end_date: date | None = None, db: Session = Depends(dep.get_db)) -> list[schemas.ClosedDay]:
    return crud.get_closed_days(db=db, start_date=start_date, end_date=end_date)


@settings.post("/settings/closed-day", dependencies=[Depends(dep.get_current_appointment_manager_user)])
async def create_closed_day(
        closed_day_data: schemas.ClosedDay,
        db: Session = Depends(dep.get_db)) -> schemas.ClosedDay:

    return crud.create_closed_day(db=db, closed_day_data=closed_day_data)


@settings.delete("/settings/closed-day/{closed_day_date}", dependencies=[Depends(dep.get_current_appointment_manager_user)])
async def delete_closed_day(
        closed_day_date: date,
        db: Session = Depends(dep.get_db)):

    crud.delete_closed_day(db=db, closed_day_date=closed_day_date)
