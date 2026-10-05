from django.contrib import admin
from poll_app.models import CustomUser,poll,choice
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(poll)
admin.site.register(choice)