from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    # render 는 주어진 1, 2 번째 인수를 사용해서
    # 1번째 인수: HttpResponse인스턴스
    # 2번째 인수: 문자열 (TEMPLATE['DIRS']를 기준으로 탐색할 템플릿 파일의 경로)
    # 3번째 인수: 템플릿을 렌더링 할 때 사용할 객체 모음
    return render(request,'blog/post_list.html', context)

