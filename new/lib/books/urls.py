"""
URL configuration for lib project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from students import views
from books import views
from books import views
app_name="books"
urlpatterns = [
    path('',views.home,name="home"),
    path('add',views.addbooks,name="add"),
    path('add1',views.addbooks1,name="add1"),
    path('view',views.viewbook,name="view"),
    path('fact',views.fact,name="fact"),
    path('bookdetail/<int:p>',views.bookdetail,name="bookdetail"),
    path('bookdelete/<int:p>',views.bookdelete, name="bookdelete"),
    path('bookedit/<int:p>', views.bookdelete, name="bookedit"),
    path('search',views.search,name="search"),



]
