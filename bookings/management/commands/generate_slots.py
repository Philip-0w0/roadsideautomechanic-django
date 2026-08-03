import datetime
from django.core.management.base import BaseCommand
from bookings.models import AvailabilitySlot

SLOT_TIMES = [
    (datetime.time(10, 0), datetime.time(13, 30)),
    (datetime.time(13, 30), datetime.time(17, 0)),
]

class Command(BaseCommand):
    help = 'Generate 2 evenly-spaced availability slots per day (10am-5pm) for the next N days'

    def add_arguments(self, parser):
        parser.add_argument('--days', type=int, default=60)

    def handle(self, *args, **options):
        days = options['days']
        today = datetime.date.today()
        created_count = 0

        for i in range(days):
            day = today + datetime.timedelta(days=i)
            if day.weekday() == 6:  # skip Sundays
                continue
            for start_time, end_time in SLOT_TIMES:
                slot, created = AvailabilitySlot.objects.get_or_create(
                    date=day, start_time=start_time,
                    defaults={'end_time': end_time, 'max_bookings': 1},
                )
                if created:
                    created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Created {created_count} new slots.'))