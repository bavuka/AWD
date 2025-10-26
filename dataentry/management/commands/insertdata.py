from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help='it will inssert data to table'
    def handle(self, *args, **kwargs):
        dataset=[{"name":"bav","roll_no":21,"age":22},
                 {"name":"vysh","roll_no":22,"age":32},
                 {"name":"josna","roll_no":23,"age":19},]
        for data in dataset:
          
            roll=data["roll_no"]
            exist=Student.objects.filter(roll_no=roll).exists()
            if not exist:
             Student.objects.create(name=data["name"],roll_no=data["roll_no"],age=data["age"])
            else:
               self.stdout.write(f"invalid roll num {data["roll_no"]}") 
        self.stdout.write("data inserted ") 

     