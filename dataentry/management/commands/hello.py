from django.core.management.base import BaseCommand

class Command(BaseCommand):#we inhert the class which is essential to create custom commands ,we make use of its methods and variables
    help="prints hello world" #py manage.py hello --help this command print the help variable-which helps developrs know the the use of the command 
    def handle(self,*args,**kwargs):
        #we write the logic
        self.stdout.write("hello world") # print this in terminal when py manage.py hello    
        