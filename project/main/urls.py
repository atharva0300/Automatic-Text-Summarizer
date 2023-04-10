from django.urls import path

from .views import home_view , try_view, select_algo

urlpatterns = [
    path('' , view=home_view , name = 'home_view'),
    path('try/' , view = try_view , name = 'try'),
    path('try/select_algo/<algo_name>' , view = select_algo , name = 'select_algo'),
]