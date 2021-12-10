from django.urls import path

from . import views

urlpatterns = [ path ('',views.test_can, name = 'home'),
 path ('display_info', views.DisplayResultView.as_view(), name='search'),
 path('search_user',views.search_user_info,name='search_user'),]