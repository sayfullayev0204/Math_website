from django.urls import path
from .views import home,guruhlash
urlpatterns=[
    path('', home, name='home' ),
    path('guruh/', guruhlash, name="guruh")
]