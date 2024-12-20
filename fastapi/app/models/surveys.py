from datetime import datetime
from uuid import uuid4

from sqlalchemy import text, Boolean, Text, Integer, UUID, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database.db import Base


class PreBecycleSurvey(Base):
    __tablename__ = "prebecyclesurvey"

    id: Mapped[UUID] = mapped_column("id", UUID, primary_key=True, default=uuid4, server_default=text("uuid_generate_v4()"), index=True, quote=False)
    datetime: Mapped[datetime] = mapped_column("datetime", DateTime, nullable=False, quote=False, default=datetime.utcnow(), server_default=text("current_timestamp"))
    # hurdles
    hurdleSafety: Mapped[bool] = mapped_column("hurdleSafety", Boolean, default=False, server_default=text("FALSE"), nullable=False, quote=False)
    hurdleMoney: Mapped[bool] = mapped_column("hurdleMoney", Boolean, default=False, server_default=text("FALSE"),
                                             nullable=False, quote=False)
    hurdleTime: Mapped[bool] = mapped_column("hurdleTime", Boolean, default=False, server_default=text("FALSE"), nullable=False, quote=False)
    hurdleSweating: Mapped[bool] = mapped_column("hurdleSweating", Boolean, default=False, server_default=text("FALSE"), nullable=False, quote=False)
    hurdleComfort: Mapped[bool] = mapped_column("hurdleComfort", Boolean, default=False, server_default=text("FALSE"), nullable=False, quote=False)
    hurdleDistance: Mapped[bool] = mapped_column("hurdleDistance", Boolean, default=False, server_default=text("FALSE"), nullable=False, quote=False)
    hurdleOther: Mapped[str] = mapped_column("hurdleOther", Text, default=None, server_default=text("NULL"), nullable=True, quote=False)

    # motivation
    motivationMoney: Mapped[bool] = mapped_column("motivationMoney", Boolean, default=False, server_default=text("FALSE"), nullable=False, quote=False)
    motivationHealth: Mapped[bool] = mapped_column("motivationHealth", Boolean, default=False, server_default=text("FALSE"), nullable=False, quote=False)
    motivationEnvironmental: Mapped[bool] = mapped_column("motivationEnvironmental", Boolean, default=False, server_default=text("FALSE"), nullable=False,
                                             quote=False)
    motivationOther: Mapped[str] = mapped_column("motivationOther", Text, default=None, server_default=text("NULL"), nullable=True,
                                             quote=False)

    # options considered
    consideredNewOnline: Mapped[bool] = mapped_column("consideredNewOnline", Boolean, default=False, server_default=text("FALSE"), nullable=False,
                                          quote=False)
    consideredNewShop: Mapped[bool] = mapped_column("consideredNewShop", Boolean, default=False,
                                                      server_default=text("FALSE"), nullable=False,
                                                      quote=False)
    consideredUsed: Mapped[bool] = mapped_column("consideredUsed", Boolean, default=False,
                                                      server_default=text("FALSE"), nullable=False,
                                                      quote=False)
    consideredLendingPrivate: Mapped[bool] = mapped_column("consideredLendingPrivate", Boolean, default=False,
                                                      server_default=text("FALSE"), nullable=False,
                                                      quote=False)
    consideredLendingBecycle: Mapped[bool] = mapped_column("consideredLendingBecycle", Boolean, default=False,
                                                      server_default=text("FALSE"), nullable=False,
                                                      quote=False)
    consideredOther: Mapped[str] = mapped_column("consideredOther", Text, default=None,
                                                      server_default=text("NULL"), nullable=True,
                                                      quote=False)

    # training
    trainingExperienceMonths: Mapped[int] = mapped_column("trainingExperience", Integer, nullable=False, quote=False)
    trainingFormal: Mapped[bool] = mapped_column("trainingFormal", Boolean, default=False, server_default=text("FALSE"), nullable=False,
                                          quote=False)
    trainingConfidence: Mapped[int] = mapped_column("trainingConfidence", Integer, nullable=False, quote=False)
    trainingRules: Mapped[bool] = mapped_column("trainingRules", Boolean, default=False, server_default=text("FALSE"),
                                                 nullable=False,
                                                 quote=False)
    trainingDriver: Mapped[bool] = mapped_column("trainingDriver", Boolean, default=False, server_default=text("FALSE"),
                                                nullable=False,
                                                quote=False)

    # interest
    interestMaintenanceDesired: Mapped[int] = mapped_column("interestMaintenanceDesired", Integer, nullable=False, quote=False)
    interestMaintenanceCurrent: Mapped[int] = mapped_column("interestMaintenanceCurrent", Integer, nullable=False, quote=False)


class PeriBecycleSurvey(Base):
    __tablename__ = "peribecyclesurvey"

    id: Mapped[UUID] = mapped_column("id", UUID, primary_key=True, default=uuid4, server_default=text("uuid_generate_v4()"), index=True, quote=False)
    datetime: Mapped[datetime] = mapped_column("datetime", DateTime, nullable=False, quote=False, default=datetime.utcnow(), server_default=text("current_timestamp"))

    # service satisfaction
    serviceSatisfactionGetBike: Mapped[int] = mapped_column("serviceSatisfactionGetBike", Integer, nullable=False, quote=False,
                                                     default=0, server_default=text('0'))
    serviceSatisfactionFixBike: Mapped[int] = mapped_column("serviceSatisfactionFixBike", Integer, nullable=False, quote=False,
                                                     default=0, server_default=text('0'))
    serviceSatisfactionLearn: Mapped[int] = mapped_column("serviceSatisfactionLearn", Integer, nullable=False, quote=False,
                                                     default=0, server_default=text('0'))

    # roads opinion
    roadsGreat: Mapped[bool] = mapped_column("roadsGreat", Boolean, default=False, server_default=text("FALSE"), nullable=False, quote=False)
    roadsLight: Mapped[bool] = mapped_column("roadsLight", Boolean, default=False, server_default=text("FALSE"),
                                             nullable=False, quote=False)
    roadsPotholes: Mapped[bool] = mapped_column("roadsPotholes", Boolean, default=False, server_default=text("FALSE"), nullable=False, quote=False)
    roadsRubbish: Mapped[bool] = mapped_column("roadsRubbish", Boolean, default=False, server_default=text("FALSE"), nullable=False, quote=False)
    roadsParking: Mapped[bool] = mapped_column("roadsParking", Boolean, default=False, server_default=text("FALSE"), nullable=False, quote=False)
    roadsDark: Mapped[bool] = mapped_column("roadsDark", Boolean, default=False, server_default=text("FALSE"), nullable=False, quote=False)

    # road users
    usersSafe: Mapped[bool] = mapped_column("usersSafe", Boolean, default=False, server_default=text("FALSE"), nullable=False, quote=False)
    usersBusesUnsafe: Mapped[bool] = mapped_column("usersBusesUnsafe", Boolean, default=False, server_default=text("FALSE"), nullable=False, quote=False)
    usersCarsUnsafe: Mapped[bool] = mapped_column("usersCarsUnsafe", Boolean, default=False, server_default=text("FALSE"), nullable=False,
                                             quote=False)
    usersTrucksUnsafe: Mapped[bool] = mapped_column("usersTrucksUnsafe", Boolean, default=None, server_default=text("FALSE"),
                                            nullable=True,
                                            quote=False)
    usersTaxisUnsafe: Mapped[bool] = mapped_column("usersTaxisUnsafe", Boolean, default=None, server_default=text("FALSE"), nullable=True,
                                             quote=False)
    usersCyclistsUnsafe: Mapped[bool] = mapped_column("usersCyclistsUnsafe", Boolean, default=None, server_default=text("FALSE"),
                                                  nullable=True, quote=False)
    usersPedestriansUnsafe: Mapped[bool] = mapped_column("usersPedestriansUnsafe", Boolean, default=None,
                                                     server_default=text("FALSE"), nullable=True, quote=False)

    # routes used
    routesRoads: Mapped[bool] = mapped_column("routesRoads", Boolean, default=False, server_default=text("FALSE"), nullable=False,
                                          quote=False)
    routesPavements: Mapped[bool] = mapped_column("routesPavements", Boolean, default=False,
                                                      server_default=text("FALSE"), nullable=False,
                                                      quote=False)
    routesOffroad: Mapped[bool] = mapped_column("routesOffroad", Boolean, default=False,
                                                      server_default=text("FALSE"), nullable=False,
                                                      quote=False)

    # accidents
    accidentsNearMisses: Mapped[int] = mapped_column("accidentsNearMisses", Integer, nullable=False, quote=False, default=0, server_default=text('0'))
    accidentsContact: Mapped[int] = mapped_column("accidentsContact", Integer, nullable=False, quote=False, default=0, server_default=text('0'))

    # harassment
    harassmentExperienced: Mapped[bool] = mapped_column("harassmentExperienced", Boolean, default=False, server_default=text("FALSE"), nullable=False,
                                          quote=False)
    harassmentSuggestions: Mapped[str] = mapped_column("harassmentSuggestions", Text, nullable=True, quote=False)


class PostBecycleSurvey(Base):
    __tablename__ = "postbecyclesurvey"

    id: Mapped[UUID] = mapped_column("id", UUID, primary_key=True, default=uuid4, server_default=text("uuid_generate_v4()"), index=True, quote=False)
    datetime: Mapped[datetime] = mapped_column("datetime", DateTime, nullable=False, quote=False, default=datetime.utcnow(), server_default=text("current_timestamp"))

    # service satisfaction
    serviceSatisfactionGetBike: Mapped[int] = mapped_column("serviceSatisfactionGetBike", Integer, nullable=False, quote=False,
                                                     default=0, server_default=text('0'))
    serviceSatisfactionFixBike: Mapped[int] = mapped_column("serviceSatisfactionFixBike", Integer, nullable=False, quote=False,
                                                     default=0, server_default=text('0'))
    serviceSatisfactionLearn: Mapped[int] = mapped_column("serviceSatisfactionLearn", Integer, nullable=False, quote=False,
                                                     default=0, server_default=text('0'))

    # stopped cycling
    reasonStoppedCycling: Mapped[bool] = mapped_column("reasonStoppedCycling", Boolean, default=False, server_default=text("FALSE"), nullable=False, quote=False)
    reasonLeavingAberdeen: Mapped[bool] = mapped_column("reasonLeavingAberdeen", Boolean, default=False,
                                                       server_default=text("FALSE"),
                                                       nullable=False, quote=False)

    # if stopped, why

    issueSafety: Mapped[bool] = mapped_column("issueSafety", Boolean, default=False, server_default=text("FALSE"),
                                               nullable=False, quote=False)
    issueMoney: Mapped[bool] = mapped_column("issueMoney", Boolean, default=False, server_default=text("FALSE"),
                                              nullable=False, quote=False)
    issueTime: Mapped[bool] = mapped_column("issueTime", Boolean, default=False, server_default=text("FALSE"),
                                             nullable=False, quote=False)
    issueSweating: Mapped[bool] = mapped_column("issueSweating", Boolean, default=False, server_default=text("FALSE"),
                                                 nullable=False, quote=False)
    issueComfort: Mapped[bool] = mapped_column("issueComfort", Boolean, default=False, server_default=text("FALSE"),
                                                nullable=False, quote=False)
    issueDistance: Mapped[bool] = mapped_column("issueDistance", Boolean, default=False, server_default=text("FALSE"),
                                                 nullable=False, quote=False)
    issueOther: Mapped[str] = mapped_column("issueOther", Text, default=None, server_default=text("NULL"),
                                             nullable=True, quote=False)

    # these improvements would make me more likely to cycle again
    improvementNone: Mapped[bool] = mapped_column("improvementNone", Boolean, default=False,
                                                  server_default=text("FALSE"),
                                                  nullable=False, quote=False)
    improvementCyclingPaths: Mapped[bool] = mapped_column("improvementCyclingPaths", Boolean, default=False, server_default=text("FALSE"),
                                                nullable=False, quote=False)
    improvementLights: Mapped[bool] = mapped_column("improvementLights", Boolean, default=False,
                                                          server_default=text("FALSE"),
                                                          nullable=False, quote=False)
    improvementSurface: Mapped[bool] = mapped_column("improvementSurface", Boolean, default=False,
                                                          server_default=text("FALSE"),
                                                          nullable=False, quote=False)
    improvementCleaner: Mapped[bool] = mapped_column("improvementCleaner", Boolean, default=False,
                                                          server_default=text("FALSE"),
                                                          nullable=False, quote=False)
    improvementOther: Mapped[str] = mapped_column("improvementOther", Text, default=None,
                                                          server_default=text("NULL"),
                                                          nullable=True, quote=False)

    # if not stopped cycling, what is the alternative
    alternativeOwnBike: Mapped[bool] = mapped_column("alternativeOwnBike", Boolean, default=False, server_default=text("FALSE"),
                                               nullable=False, quote=False)
    alternativeShareFriendsFamily: Mapped[bool] = mapped_column("alternativeShareFriendsFamily", Boolean, default=False,
                                                     server_default=text("FALSE"),
                                                     nullable=False, quote=False)
    alternativeAnotherBecycle: Mapped[bool] = mapped_column("alternativeAnotherBecycle", Boolean, default=False,
                                                         server_default=text("FALSE"),
                                                         nullable=False, quote=False)
    alternativeOtherRental: Mapped[bool] = mapped_column("alternativeOtherRental", Boolean, default=False,
                                                     server_default=text("FALSE"),
                                                     nullable=False, quote=False)
