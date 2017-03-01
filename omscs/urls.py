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
from advisor import views as advisor
from stats import views as stats
import links

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', advisor.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/register/', advisor.register),
    url(r'^planner/', advisor.planner, name='planner'),
    url(r'^meta/courses/', advisor.course_metadata),
    url(r'^meta/specializations/', advisor.specialization_metadata),
    url(r'^profile/info/(?P<viewed>\d+)?$', advisor.profile_info),
    url(r'^profile/plan/(?P<viewed>\d+)?$', advisor.profile_plan),
    url(r'^profile/history/(?P<viewed>\d+)?$', advisor.profile_history),
    url(r'^profile/account/', advisor.account),
    url(r'^courses/', advisor.browse_courses),
    url(r'^course/(?P<id>\d+)/view/$', advisor.view_course),
    url(r'^course/(?P<id>\d+)/review/$', advisor.review_course),
    url(r'^stats/', stats.dashboard),
    url(r'^links/', include(links.urls))
]
