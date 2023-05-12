from django.urls import path

from .views import home_view , try_view, change_algo , about , options_view, extractPDF_view , convertionView
from . import views

urlpatterns = [
    path('' , view=home_view , name = 'home_view'),
    path('summarizer/' , view = try_view , name = 'summarizer'),
    path('summarizer/change_algo/' , view = change_algo , name = 'change_algo'),
    path('about/' , view = about , name ='about'),
    path('options/' , view = options_view , name = 'options'),
    path('options/extractpdf/' , view = extractPDF_view  , name = 'extractPDF'),
    path('summarizer/convertion/' , view=convertionView , name = 'convertion')

]

