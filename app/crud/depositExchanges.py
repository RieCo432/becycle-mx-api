from datetime import date
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

import app.models as models


def create_deposit_exchange(
        db: Session,
        amount: int,
        from_user_id: UUID,
        to_user_id: UUID) -> models.DepositExchange:

    deposit_exchange = models.DepositExchange(
        amount=amount,
        fromUserId=from_user_id,
        toUserId=to_user_id
    )

    db.add(deposit_exchange)
    db.commit()

    return deposit_exchange


def get_deposit_exchange_dates(db: Session) -> list[date]:
    return [_ for _ in db.scalars(
        select(models.DepositExchange.date)
        .distinct()
    )]


def get_deposit_exchanges_by_date(db: Session, date_of_exchange: date) -> list[models.DepositExchange]:
    return [_ for _ in db.scalars(
        select(models.DepositExchange)
        .where(models.DepositExchange.date == date_of_exchange)
    )]


def get_deposit_exchanges_grouped_by_date(db: Session) -> dict[date, list[models.DepositExchange]]:
    deposit_exchanges_by_date = {date_of_exchange: get_deposit_exchanges_by_date(db=db, date_of_exchange=date_of_exchange) for date_of_exchange in get_deposit_exchange_dates(db=db)}
    return deposit_exchanges_by_date


def get_deposit_exchange_users(db: Session) -> list[models.User]:
    return [_ for _ in db.scalars(
        select(models.User)
        .where(
            (models.User.depositBearer == True)
            | (models.User.treasurer == True)
            | (models.User.username == "BANK")
        )
    )]

