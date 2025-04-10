from huey.contrib.djhuey import periodic_task
from huey import crontab
from .methods import send_guest_summary_email

@periodic_task(crontab(hour=23, minute=59))
def send_daily_guest_summary():
    count = send_guest_summary_email()
    print(f"[Huey] Email sent!, Total guest today: {count}")