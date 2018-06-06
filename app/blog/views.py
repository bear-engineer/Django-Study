from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string

from .models import Post


def post_list(request):
    post = Post.objects.all()


    return HttpResponse(print(post))

