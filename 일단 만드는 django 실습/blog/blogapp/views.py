from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comment
from .forms import CommentModelForm

def home(request):
    blogs = Blog.objects.all()

    return render(request, 'index.html', {'blogs':blogs})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        blog = Blog()
        blog.author = request.POST['author']
        blog.body = request.POST['body']
        blog.save()

        return redirect('home')

def detail(request, blog_id):
    chosen_blog = get_object_or_404(Blog, pk=blog_id)
    comment_form = CommentModelForm()

    return render(request, 'detail.html', {'blog':chosen_blog, 'comment_form':comment_form})

def comment_create(request, blog_id):
    comment_form = CommentModelForm(request.POST)
    
    if comment_form.is_valid():
        form = comment_form.save(commit=False)
        form.post = get_object_or_404(Blog, pk=blog_id)
        form.save()

    return redirect('detail', blog_id)
        