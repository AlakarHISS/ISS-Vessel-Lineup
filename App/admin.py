from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(PasswordReset)
admin.site.register(Users)
admin.site.register(LineUpForm)
admin.site.register(SailedData)
admin.site.register(UniquePortDetails)
admin.site.register(Port_Berth_Form)