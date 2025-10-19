from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help="greets the user"
    def add_arguments(self, parser):
        parser.add_argument('name',type='str',help='specifies name')
        
    def handle(self, *args, **kwargs):
       name=kwargs.get("name")
       self.stdout.write(f"hi {name} good morning")