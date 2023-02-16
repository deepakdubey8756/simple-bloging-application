from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
    post_list = Post.objects.filter(status = 1).order_by('-created_on')
    paginator  = Paginator(post_list, 1)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first group
        post_list = paginator.page(1)
    except EmptyPage:
        # if page is out of range then deliver last page of reults;
        post_list = paginator.page(paginator.num_pages)
    return render(request, "blog/index.html", {"post_list": post_list})


def details(request, slug):
    template_name = "blog/post_detail.html"
    post = get_object_or_404(Post, slug = slug)
    comments = post.comments.filter(active=True)
    new_comments = None

    if request.method == "POST":
        comment_form =  CommentForm(data=request.POST)
        if comment_form.is_valid():
            
            new_comments = comment_form.save(commit=False)

            new_comments.post = post

            new_comments.save()

    else:
        comment_form = CommentForm()
    
    return render(request, template_name, {'post':post, 'comments': comments, 'new_comment': new_comments, 'comment_form': comment_form})


