from datetime import datetime
import pytz

def convert_to_timezone(dt: datetime, tz_name: str):
    return dt.astimezone(pytz.timezone(tz_name))
