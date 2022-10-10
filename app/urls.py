from django.urls import path
from .views import home, detail

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:work_id>/<str:work_name>/', detail, name='detail'),
]
