from django.contrib import admin
from .models import Question , Answer

# Register your models here.
admin.site.register(Question)          # registering the models 
admin.site.register(Answer)

