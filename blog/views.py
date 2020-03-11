from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post,Image,Audio
from .forms import ImageForms,AudioForms


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def MultiMedia(request):
    return render(request, 'blog/multimedia-post.html', {'title': 'Post Multimedia'})

def ImageMedia(request):
    if request.method == "POST":
        form = ImageForms(request.POST,request.FILES)
        
        if form.is_valid():
            form.instance.author = request.user;
            form.save()
            messages.success(request, f'Posted Succesfully')
        
    return render(request, 'blog/imagemedia-post.html', {'title': 'Post images'})

def AudioMedia(request):
    if request.method == "POST":
        form = AudioForms(request.POST,request.FILES)
        print(form.errors)

        if form.is_valid():
            form.instance.author = request.user;
            form.save()
            messages.success(request, f'Posted Succesfully')
        

    return render(request, 'blog/audiomedia-post.html', {'title': 'Post-Audio'})

def MultiMediaView(request):
    return render(request, 'blog/multimedia-view.html', {'title': 'Post-Multimedia'})

def ImageMediaView(request):

    print(Image.objects.all())
    context = {
        'images': Image.objects.all(),
        'media_url': "/media/"
    }
    return render(request, 'blog/imagemedia-view.html', context)

class ImagePostListView(ListView):
    model = Image
    template_name = 'blog/imagemedia-view.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'images'
    ordering = ['-date_posted']
    paginate_by = 5

def AudioMediaView(request):
    print(Image.objects.all())
    context = {
        'audios': Audio.objects.all(),
        'media_url':"/media/"
    }
    return render(request, 'blog/audiomedia-view.html', context)

class AudioPostListView(ListView):
    model = Audio
    template_name = 'blog/audiomedia-view.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'audios'
    ordering = ['-date_posted']
    paginate_by = 5
