from django.urls import path

from .views import home_view , try_view

urlpatterns = [
    path('' , view=home_view , name = 'home_view'),
    path('try/' , view = try_view , name = 'try')
]