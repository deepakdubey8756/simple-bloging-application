from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.
from django.views import generic

# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = "index.html"


# class PostDetail(generic.ListView):
#     model = Post
#     template_name = 'post_details.html'

def index(request):
    post_list = Post.objects.filter(status = 1).order_by('-created_on')
    return render(request, "blog/index.html", {"post_list": post_list})


def details(request, slug):
    post = Post.objects.filter(slug = slug)
    if len(post) > 0:
        return render(request, 'blog/post_detail.html', {"post": post[0]})
    return HttpResponse("Error! Page not found")



