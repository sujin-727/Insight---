from django.urls import path
from .views import drama_list  # views에서 drama_list 뷰를 임포트

urlpatterns = [
    path('', drama_list, name='drama_list'),  # URL 패턴이 반드시 있어야 합니다.
]