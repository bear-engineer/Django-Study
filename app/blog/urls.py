from django.conf.urls import url

# 아래의 import 처럼 상대경로로 가져오는 것이 좋다.
from .views import post_list, post_detail

urlpatterns = [
    # url의 첫 번째 인자: 매치될 URL정규표현식
    # url의 두 번째 인자: view function
        # view function
        # requests를 받아서 response를 돌려주는 함수
    url(r'^$', post_list, name='post-list'),
    url(r'^(\d+)/', post_detail, name='post-detail'),
]