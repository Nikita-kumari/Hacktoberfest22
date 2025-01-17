from pathlib import Path

def add_alarm_to_calender_events(filepath, num_day_before_notif = 0, num_hour_before_notif = 0, num_min_before_notif = 5, num_sec_before_notif = 0):
    """
    function will take an .ics file and then add notif to the file
    Args:
        filepath : the location of the file
        num_day_before_notif : The num days before which notif will be scheduled
        num_hour_before_notif : The num hour before which notif will be scheduled
        num_min_before_notif : The num  min before notif will be scheduled
        num_sec_before_notif : The num sec before which notif will be schedules
    """

    # Alarm Schema
    alarm_schema = f"""
    BEGIN:VALARM
    ACTION:DISPLAY
    DESCRIPTION:This is an event reminder
    TRIGGER:-P{num_day_before_notif}DT{num_hour_before_notif}H{num_min_before_notif}M{num_sec_before_notif}S
    END:VALARM
    """

    to_replace = """END:VEVENT"""

    data = Path(filepath).read_text()

    updated_file = data.replace(to_replace, alarm_schema + to_replace)

    Path(filepath).write_text(updated_file)

