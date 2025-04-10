from django.core.mail import send_mail
from django.utils import timezone

from .models import Guest


def send_guest_summary_email():
    today = timezone.now().date()
    count = Guest.objects.filter(visit_date=today).count()

    subject = "Daily Guestbook Summary"
    message = f"Hi Admin,\n\nTotal guests today ({today}): {count}.\n\nRegards,\nGuestbook System"

    send_mail(
        subject, message, None, ["guestbookdjango@gmail.com"], fail_silently=False
    )

    return count
