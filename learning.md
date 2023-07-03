# Rest Framework 
1. After create Django project 
2. ```
   pip install djangorestframework
    pip install markdown       # Markdown support for the browsable API.
    pip install django-filter  # Filtering support
   ```
3. INSTALLED_APPS = [
    ...
    'rest_framework',
]

## Make migration from model command - 
```
python manage.py makemigration 
```
## Django super user create command 
```
python manage.py createsuperuser
```

## Register a model in admin 
```
from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    pass
admin.site.register(Task, TaskAdmin)
```

