from django.urls import path

from . import views
app_name = 'ml_model'


urlpatterns = [
    path('', views.index, name='home'),
    path('results/', views.results_page, name='results'),
]