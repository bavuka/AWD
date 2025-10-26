from django.core.management.base import BaseCommand,CommandError
import csv
from dataentry.models import *
from django.apps import apps

class Command(BaseCommand):
    help='import from csv file'

    def add_arguments(self, parser):
        parser.add_argument("file_path",type=str,help="path to the csv file")
        parser.add_argument("model_name",type=str,help="model to be the data inserted")
       

    def handle(self, *args, **options):
        file_path=options.get("file_path")
        model_name=options.get("model_name").capitalize()
        model=None
        for app_config in apps.get_app_configs():
            try:
                 model=apps.get_model(app_config.label,model_name)
            except LookupError:
                continue

        if not model:
            raise CommandError(f"model {model_name} is not found in any app")         

        with open(file_path,"r") as file:
            reader=csv.DictReader(file) # dict reader is a method used to read the rows of a file and convert each row  to dictionary format- list of dictionarries
            for row in reader:
              model.objects.create(**row)
        self.stdout.write(f"file is is added to db")
      