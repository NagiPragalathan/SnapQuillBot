"""
URL configuration for MediBot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import home, about, chatbot_res,update_qa, login_form,signup,logout1,upload_image,text_bard, add_text_entry,download_file

from django.conf.urls.static import static
from MediBot import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home,name="home"),
    path('about',about,name="about"),
    path('chatbot_res',chatbot_res,name="chatbot_res"),
    path('signup', signup, name='signup'),
    path('', home, name='home'),
    path('logout', logout1, name='logout'),
    path('upload_image', upload_image, name='upload_image'),
    path('text_bard', text_bard, name='text_bard'),
    path('add_text', add_text_entry, name='add_text_entry'),
     path('download', download_file, name='download_file'),
     path('update-qa', update_qa, name='update_qa'),
]

from django.conf.urls.static import static
from MediBot import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)