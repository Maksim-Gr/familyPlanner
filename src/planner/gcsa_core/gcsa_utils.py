from datetime import datetime, timedelta, date, time
from typing import Tuple


def create_week_interval() -> Tuple[datetime, datetime]:
    """
    Create one-week interval from Monday till Sunday
    :return: tuple of two datetime objects indicating the start and end
    """
    monday = date.today() - timedelta(days=datetime.now().weekday())
    midnight = time(hour=0, minute=00)
    sunday = monday + timedelta(days=7)
    monday_datetime = datetime.combine(monday, midnight)
    sunday_datetime = datetime.combine(sunday, midnight)
    return monday_datetime, sunday_datetime


def create_one_day_interval() -> Tuple[datetime, datetime]:
    """
    Create one-day interval
    :return: datetime object
    """
    start_day = date.today() + timedelta(days=1)
    end_day = date.today() + timedelta(days=2)
    midnight = time(hour=0, minute=00)
    beginning_of_the_day = datetime.combine(start_day, midnight)
    end_of_the_day = datetime.combine(end_day, midnight)
    return beginning_of_the_day, end_of_the_day

