from django.shortcuts import render, reverse, redirect
from django.db.models import Count
from .models import Post, Tag
from .mixins import ObjectListView
from .forms import PostForm
from django.contrib.auth.decorators import login_required


class PostListView(ObjectListView):
    model = Post
    template = 'blog/index.html'
    queryset = Post.objects.all()


class TagListView(ObjectListView):
    model = Tag
    template = 'blog/tags_list.html'
    queryset = Tag.objects.annotate(posts_count=Count('posts'))


def post_detail_view(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post': post})


def tag_detail_view(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag': tag})


@login_required(login_url='/admin/')
def post_create_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            return redirect('post_detail_url', slug=post.slug)
        return render(request, 'blog/post_create.html', context={'form': form})
    form = PostForm()
    return render(request, 'blog/post_create.html', context={'form': form})
