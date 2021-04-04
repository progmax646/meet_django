from django import template
from datetime import timedelta, datetime, tzinfo, timezone
import pytz

register = template.Library()


@register.simple_tag
def get_month_day(month):
    pytz.timezone("Asia/Tashkent")
    t2 = month+'-01'
    t = datetime.fromisoformat(t2).strftime('%B')
    return t