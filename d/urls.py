from django.urls import path
from .views import home,guruhlash,takroriy, orin,p
urlpatterns=[
    path('', home, name='home' ),
    path('guruh/', guruhlash, name="guruh"),
    path('takroriy/', takroriy, name='takroriy'),
    path('orin/', orin, name='orin'),
    path('url/', p, name='url')
]
