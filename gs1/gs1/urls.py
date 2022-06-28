"""gs1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path,include
from enroll import views
from django.conf import settings
from django.conf.urls.static import static
from django.core.paginator import Paginator
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    # path('hello/',views.hello,name='hello'),
    path('admin/', admin.site.urls),
    path('',views.show_details, name ="detail"),
    path('form/', views.index),  
    path('sign/',views.sign,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('users/',views.users,name='allusers'),
    path('contact/', views.contact, name="n4"),
    path('multi_docs/',views.multi_docs, name='multi_docs'),
    path('uploadimage/',views.upload,name="upload"),
    path('paginate/', views.paginate, name="paginate"),
    path('enroll/employees',views.employeeListView),
    path('api/token/',
         jwt_views.TokenObtainPairView.as_view(),
         name ='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),
    #path('', include('enroll.urls')),
    path('api/registration/',include('enroll.urls'))


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

