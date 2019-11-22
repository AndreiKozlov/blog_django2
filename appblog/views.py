from django.shortcuts import render
from django.views.generic.base import View
from .models import Category, Post


class HomeView(View):
    """Главная страница"""
    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.all()
        context = {'categories': category_list, 'posts': post_list}
        return render(request, 'appblog/home.html', context)

