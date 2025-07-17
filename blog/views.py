from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm
from .models import BlogPost

@login_required
def create_post(request):
    if request.user.user_type != 'doctor':
        return redirect('dashboard')
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('my_posts')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def my_posts(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'blog/my_posts.html', {'posts': posts})

@login_required
def view_posts_by_category(request):
    
    
    # process mental health posts

    # posts = BlogPost.objects.filter(category=selected_category, is_draft=False)
    return render(request, 'blog/view_category.html')

@login_required
def all_post(request):
    posts = BlogPost.objects.filter(author=request.user)

    if request.method == 'POST':
        selected_category = request.POST.get('categoryDropdown')
        if selected_category=='mental':
            posts=BlogPost.objects.filter(category=selected_category, is_draft=False)
        elif selected_category=='heart':
            posts=BlogPost.objects.filter(category=selected_category, is_draft=False)
        elif selected_category=='covid':
            posts=BlogPost.objects.filter(category=selected_category, is_draft=False)
        elif selected_category=='general':
            posts=BlogPost.objects.filter(category=selected_category, is_draft=False)
        else:
             posts = BlogPost.objects.filter(author=request.user)

    return render(request, 'blog/blogs.html', {'posts': posts,})