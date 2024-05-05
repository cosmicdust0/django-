



from django.contrib import admin
from django.urls import path , include
from home.views import *
from vege.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('receipes/',receipes, name='recepies')
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import  static

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()