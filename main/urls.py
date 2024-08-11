from django.urls import path
from main.views import *

urlpatterns = [
    path('rezume/sozdanie/', SozdanieRezume.as_view(), name='sozdanie_rezume'),
    path('vakansii/sozdanie/', SozdanieVakansii.as_view(), name='sozdanie_vakansii'),
    path('rezume/', SpisokRezume.as_view(), name='spisok_rezume'),
    path('vakansii/', SpisokVakansii.as_view(), name='spisok_vakansii'),
    path('rezume/<int:pk>/', DetailRezume.as_view(), name='detail_rezume'),
    path('vakansii/<int:pk>/', DetailVakansii.as_view(), name='detail_vakansii'),
    path('rezume/<int:pk>/udalenie/', UdalenieRezume.as_view(), name='udalenie_rezume'),
    path('vakansii/<int:pk>/udalenie/', UdalenieVakansii.as_view(), name='udalenie_vakansii'),
]
