from django.urls import path

from .views import home_view , try_view, change_algo

urlpatterns = [
    path('' , view=home_view , name = 'home_view'),
    path('try/' , view = try_view , name = 'try'),
    path('try/change_algo/' , view = change_algo , name = 'change_algo'),
]