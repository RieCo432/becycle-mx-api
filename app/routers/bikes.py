from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
import app.crud as crud
import app.schemas as schemas
import app.models as models
import app.dependencies as dep


bikes = APIRouter(
    tags=["bikes"],
    dependencies=[Depends(dep.get_db)],
    responses={404: {"description": "Not Found"}}
)


@bikes.get("/bikes", dependencies=[Depends(dep.get_current_active_user)])
async def get_bikes(
        make: str = None,
        model: str = None,
        colour: str = None,
        decals: str = None,
        serial_number: str = None,
        db: Session = Depends(dep.get_db)
    ) -> list[schemas.Bike]:
    return crud.get_bikes(make=make, model=model, colour=colour, decals=decals, serialNumber=serial_number, db=db)


@bikes.post("/bike", dependencies=[Depends(dep.get_current_active_user)])
async def create_bike(
        bike_data: schemas.BikeCreate,
        db: Session = Depends(dep.get_db)
) -> schemas.Bike:
    return crud.create_bike(bike_data=bike_data, db=db)


@bikes.get("/bikes/suggest-makes", dependencies=[Depends(dep.get_current_active_user)])
async def get_make_suggestions(
        make: str,
        db: Session = Depends(dep.get_db)
) -> list[str]:
    return crud.get_similar_makes(db=db, make=make.lower())


@bikes.get("/bikes/suggest-models", dependencies=[Depends(dep.get_current_active_user)])
async def get_model_suggestions(
        model: str,
        db: Session = Depends(dep.get_db)
) -> list[str]:
    return crud.get_similar_models(db=db, model=model.lower())


@bikes.get("/bikes/suggest-serial-numbers", dependencies=[Depends(dep.get_current_active_user)])
async def get_serial_number_suggestions(
        serial_number: str,
        db: Session = Depends(dep.get_db)
) -> list[str]:
    return crud.get_similar_serial_numbers(db=db, serial_number=serial_number.lower())
