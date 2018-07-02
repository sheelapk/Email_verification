from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',include('student.urls')),
    # path('hr/',include('hr.urls')),
    path('signup/',include('signup.urls')),

]

urlpatterns +=staticfiles_urlpatterns()