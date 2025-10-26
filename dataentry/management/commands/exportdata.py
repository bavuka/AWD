from django.core.management.base import BaseCommand,CommandError
from django.apps import apps

import datetime
import csv


class Command(BaseCommand):
    help='to export data from table to csv file'
    def add_arguments(self, parser):
         parser.add_argument("model_name",type=str,help="model name")
    def handle(self,*args,**kwargs):
        model_name=kwargs.get("model_name").capitalize()
        model=None
        for app_config in apps.get_app_configs(): # contain metadata of all apps in the projrct
             try:
                 model=apps.get_model(app_config.label,model_name)
             except LookupError:
                  continue    
        if not model:
             raise CommandError(f"no such model")
        datas=model.objects.all()
        timestamp=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        file_path=f"exported_{model_name}_{timestamp}.csv"
        with open(file_path,"w",newline='') as file:
            writer=csv.writer(file)
            writer.writerow([field.name for field in model._meta.fields])
            try:
                for data in datas:
                    writer.writerow([getattr(data,field.name) for field in model._meta.fields])
            except:
                raise CommandError(f"no data in table")
        self.stdout.write("expoted!!!!!")