"""DogAndCat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from dac.views import index, put_ajax,show
from dac.views import uploadImg

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index), #在url中凡是以url开头的访问都使用index函数来处理该请求
    url(r'^uploadImg/',uploadImg),
    url(r'^put_ajax/', put_ajax),
    url(r'^show/',show),
]
