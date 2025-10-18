from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help="greets the user"
    def handle(self, *args, **kwargs):
       self.stdout.write("hi bavuka good morning")