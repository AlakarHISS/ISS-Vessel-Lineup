from django.core.management.base import BaseCommand
from apscheduler.schedulers.background import BackgroundScheduler
from App.jobs import move_sailed_data, send_port_update_emails, send_port_update_missed_emails

class Command(BaseCommand):
    def handle(self, *args, **options):
        scheduler = BackgroundScheduler()
        scheduler.add_job(move_sailed_data, 'cron', hour=2, minute=3)
        scheduler.add_job(send_port_update_emails, 'cron', hour=11, minute=30)
        scheduler.add_job(send_port_update_missed_emails, 'cron', hour=16, minute=59)
        scheduler.start()