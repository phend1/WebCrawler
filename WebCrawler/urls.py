"""WebCrawler URL Configuration

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
from WebCrawler import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index, name='index'),
    url(r'^search_currency/', views.search_currency, name='search_currency'),
    url(r'^search_currency_action/', views.search_currency_action, name ='search_currency_action'),
    url(r'^search_bank/', views.search_bank, name='search_bank'),
    url(r'^search_bank_action/', views.search_bank_action, name='search_bank_action'),
    # Index Page
    #url(r'^index/$', WebCrawler.views.index),
    # Search Currency Page
    #url(r'^search_currency/$', search_currency),
    # Search Currency's Action
    #url(r'^search_currency_action/', search_currency_action),
    # Search Bank
    #url(r'^search_bank/$', search_bank),
    # Search Currency's Action
    #url(r'^search_bank_action/', search_bank_action),

]
