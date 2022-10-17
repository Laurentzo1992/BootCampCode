
from django.contrib import admin
from django.urls import path, include
from  django.conf.urls.static import  static
from  django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('authentication.urls')),
    #path('contrat', include('gestioncontrat.urls')),
    #path('convention', include('gestionconvention.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
