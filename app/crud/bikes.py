from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.orm import Session
import app.models as models
import app.schemas as schemas
from sqlalchemy import select, func


def get_bike(db: Session, bike_id: UUID) -> models.Bike:
    return db.scalar(
        select(models.Bike)
        .where(models.Bike.id == bike_id)
    )


def find_similar_bikes(db: Session, make: str | None = None, model: str | None = None, colour: str | None = None, decals: str | None = None, serialNumber: str | None = None) -> list[schemas.Bike]:
    bikes = [bike for bike in db.scalars(
        select(models.Bike)
        .where(
            (func.levenshtein(models.Bike.make, make) <= 2)
            & (func.levenshtein(models.Bike.model, model) <= 2)
            & (func.levenshtein(models.Bike.colour, colour) <= 2)
            & (func.levenshtein(models.Bike.serialNumber, serialNumber) <= 2)
        )
        .order_by(func.levenshtein(models.Bike.serialNumber, serialNumber))
    )]

    if len(bikes) == 0:
        raise HTTPException(status_code=404, detail={"description": "No bikes found"})

    return bikes


def get_all_bikes(db: Session) -> list[schemas.Bike]:
    return [_ for _ in db.scalars(
        select(models.Bike)
    )]


def create_bike(bike_data: schemas.BikeCreate, db: Session) -> schemas.Bike:
    bike = models.Bike(
        make=bike_data.make.lower(),
        model=bike_data.model.lower(),
        colour=bike_data.colour.lower(),
        decals=bike_data.decals.lower() if bike_data.decals is not None else None,
        serialNumber=bike_data.serialNumber.lower()
    )
    db.add(bike)
    db.commit()
    return bike


def get_similar_makes(db: Session, make: str) -> list[str]:
    similar_makes = [_ for _ in db.scalars(
        select(models.Bike.make)
        .where(models.Bike.make.contains(make))
        .distinct()
    )]

    return similar_makes


def get_similar_models(db: Session, model: str) -> list[str]:
    similar_models = [_ for _ in db.scalars(
        select(models.Bike.model)
        .where(models.Bike.model.contains(model))
        .distinct()
    )]

    return similar_models


def get_similar_serial_numbers(db: Session, serial_number: str) -> list[str]:
    similar_serial_numbers = [_ for _ in db.scalars(
        select(models.Bike.serialNumber)
        .where(models.Bike.serialNumber.contains(serial_number))
        .distinct()
    )]

    return similar_serial_numbers


def get_similar_colours(db: Session, colour: str) -> list[str]:
    similar_colours = [_ for _ in db.scalars(
        select(models.Bike.colour)
        .where(models.Bike.colour.contains(colour))
        .distinct()
    )]

    return similar_colours
