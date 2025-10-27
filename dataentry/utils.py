from django.apps import apps
def get_custom_models():
    default = [
    
    "Group",
    "Permission",
    "ContentType",
    "Session",
    "LogEntry",
    "User"
]
    custom_models=[]
    for model in apps.get_models(): #returns the objects of all models
        if model.__name__ not in default:
            custom_models.append(model.__name__)
    return custom_models        
