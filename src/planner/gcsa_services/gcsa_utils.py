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
