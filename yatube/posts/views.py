from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]

    template = 'posts/index.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)

    template = 'posts/group_list.html'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]

    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
