from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string


def post_list(request):
    html = render_to_string('blog/post_list.html')
    return render(request, 'blog/post_list.html')
    # return HttpResponse(html)
