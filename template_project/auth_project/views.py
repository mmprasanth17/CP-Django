from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from .models import Post

def index(request):
    return render(request, 'auth_project/index.html')

class AddFormView(View):
    def get(self, request, post_id):
        form = CommentForm()
        context = {'form': form, 'post_id': post_id}
        return render(request, 'auth_project/add_form.html', context)

    def post(self, request, post_id):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, id=post_id)  # Link comment to the post
            comment.save()
            return redirect('post_detail', post_id=post_id)
        context = {'form': form, 'post_id': post_id}
        return render(request, 'auth_project/add_form.html', context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'auth_project/post_detail.html'
    context_object_name = 'post'

class PostListView(ListView):
    model = Post
    template_name = 'auth_project/post_list.html'
    context_object_name = 'posts'
