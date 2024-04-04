from typing import Dict
from gcsa.google_calendar import GoogleCalendar

from planner.gcsa_core.gcsa_utils import create_week_interval, create_one_day_interval
import locale

# set up russian locale
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


def get_weekly_upcoming_events(gc: GoogleCalendar) -> Dict[str, str | None]:
    """
    Retrieve all upcoming events for a specific gcsa_core week
    :return: list of events for upcoming week
    """
    start, end = create_week_interval()
    events = list(gc[start:end:"startTime"])
    return {event.start.strftime('%A %d %B %H:%M').upper(): event.description for event in events}


def get_daily_events(gc: GoogleCalendar) -> Dict[str, str | None]:
    """
    Retrieve all events for upcoming day
    :return: list of events for upcoming day
    """
    start, end = create_one_day_interval()
    events = list(gc[start:end:])
    return {event.start.strftime('%A %d %B %H:%M').upper(): event.description for event in events}
