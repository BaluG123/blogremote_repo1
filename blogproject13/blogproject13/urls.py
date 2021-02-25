"""blogproject13 URL Configuration

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
from django.urls import path,include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.postlist_view,name='home'),
    path('create/',views.postcreate_view),
    path('(?p<year>\d{4})/(?p<month>\d{2})/(?p<day>\d{2})/(?p<post>[-\w+])/$',views.postdetail_view,name='detail'),
    path('update/<int:id>',views.postupdate_view,name='list'),
    path('delete/<int:id>',views.postdelete_view),
    path('signup/',views.signup_view),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/',views.logout_view),
    path('tag/(?p<tag_slug>[-\w]+)/$',views.postlist_view,name='post_tags'),
]
