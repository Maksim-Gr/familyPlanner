import datetime
from typing import Tuple


def create_week_interval() -> Tuple[datetime.datetime, datetime.datetime]:
    """
    Create one-week interval from Monday till Sunday
    :return: tuple of two datetime objects indicating the start and end
    """
    now = datetime.datetime.now()
    monday = datetime.date.today() - datetime.timedelta(days=now.weekday())
    monday_midnight = datetime.time(hour=0, minute=00)
    sunday = monday + datetime.timedelta(days=7)
    sunday_midnight = datetime.time(hour=0, minute=00)
    monday_datetime = datetime.datetime.combine(monday, monday_midnight)
    sunday_datetime = datetime.datetime.combine(sunday, sunday_midnight)
    return monday_datetime, sunday_datetime
