from django.contrib import admin
from django.contrib.auth.models import Group
from uauth.models import User

admin.site.unregister(Group)
admin.site.register(User)
