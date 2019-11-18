from django.contrib import admin
from index.models import *


admin.site.register(City)
admin.site.register(Hotel)
admin.site.register(FeedBack)
# admin.site.register(SimpleUser,CustomizedAdmin)