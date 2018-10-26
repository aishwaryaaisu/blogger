pr"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from blogger.views import home, post_page, post_comment
from blogregistration.views import signin,logout_user,signup_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('post/<int:post_id>/',post_page),
    path('login/',signin),
    path('logout/',logout_user),
    path('signup/',signup_user),
    path('comment/<int:post_id>/', post_comment)
]
