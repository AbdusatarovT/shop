from django.contrib import admin

# Register your models here.
from applications.spam.models import Contact

admin.site.register(Contact)