from django.shortcuts import render, get_object_or_404, redirect
from .models import Post 
from django.utils import timezone
from .forms import CommentForm


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # is_authenticated is an alternative to this
    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                # return redirect(request.path_info)
                return redirect('blog-post-detail', slug=post.slug)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None

    context = {'post': post,
               'comment_form': comment_form,
               }
    return render(request, 'blog/post-detail.html', context)
