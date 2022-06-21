from django.contrib import admin
from .models import vacany, carasoul, application_form, contactus, sotrecarasoul, laptopinfo, laptopbrandname
# Register your models here.

admin.site.register(vacany)
admin.site.register(carasoul)
admin.site.register(sotrecarasoul)
admin.site.register(application_form)
admin.site.register(contactus)
admin.site.register(laptopinfo)
admin.site.register(laptopbrandname)


