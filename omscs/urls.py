"""CS6460 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from advisor import views

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/register/', views.register),
    url(r'^planner/', views.planner, name='planner'),
    url(r'^meta/courses/', views.course_metadata),
    url(r'^meta/specializations/', views.specialization_metadata),
    url(r'^profile/info/(?P<viewed>\d+)?$', views.profile_info),
    url(r'^profile/plan/(?P<viewed>\d+)?$', views.profile_plan),
    url(r'^profile/history/(?P<viewed>\d+)?$', views.profile_history),
    url(r'^profile/account/', views.account),
    url(r'^courses/', views.browse_courses),
    url(r'^course/(?P<id>\d+)/view/$', views.view_course),
    url(r'^course/(?P<id>\d+)/review/$', views.review_course)
]
