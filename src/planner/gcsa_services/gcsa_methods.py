from typing import List
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa_utils import create_week_interval


def get_weekly_upcoming_events(gc: GoogleCalendar) -> List[Event]:
    """
    Retrieve all upcoming events for a specific gcsa_services week
    :return: list of events for upcoming week
    """
    gc = GoogleCalendar()
    start, end = create_week_interval()

    return None


def get_daily_events(gc: GoogleCalendar) -> List[Event]:
    """
    Retrieve all events for upcoming day
    :return:
    """
    return None
