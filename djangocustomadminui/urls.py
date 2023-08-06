from django.contrib import admin
from django.urls import path
admin.site.site_header  =  "Mini Blog Header"  
admin.site.site_title  =  "Mini Blog Title"
admin.site.index_title  =  "Dashboard"
urlpatterns = [
    path('admin/', admin.site.urls),
]
