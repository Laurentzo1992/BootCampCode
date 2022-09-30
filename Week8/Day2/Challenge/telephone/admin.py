from django.contrib import admin
from telephone.models import Personne

admin.site.site_header = 'CENTRE D\'AMINNISTRATION'
admin.site.site_title = 'Admin centre'
admin.site.register(Personne)


# Register your models here.
