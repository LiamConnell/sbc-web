from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.views import generic
from django.views.generic.list import ListView



from .models import *
from .forms import *


def index(request):
    return render(request, 'zine/index.html')



# class Index(ListView):
#     template_name = 'zine/index.html'
#     queryset = Post.objects.all()
#     context_object_name = 'Posts'

class Index(generic.View):
    def get(self, request):
        # current_user = self.request.user
        post_list = Post.objects.all()
        # DatasetTable(Dataset.objects.filter(owner=current_user.id))
        return render(request, 'zine/index.html', {
                'list_name': 'Posts',
                'list': post_list
                })


def get_post(request):
    if request.method == 'POST': #its not POST, its GET
        form = PostForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = PostForm()
    return render(request, 'zine/get_post.html', {'form': form})

def write_post(request):
    body = request.POST
    print(body)
    # for code in body.getlist('codesfield'):
        # code_obj = get_object_or_404(DatasetCode, pk=code)
    post = Post(
        title = request.POST['title'] ,
        text= request.POST['text'],
        author=request.user
    )
    post.save()

    return HttpResponseRedirect(reverse('zine:index'))

class Post_Detail(generic.DetailView):
    model = Post
    template_name = 'zine/post_detail.html'
    def get_context_data(self, **kwargs):
        context = super(Post_Detail, self).get_context_data(**kwargs)
        context.update({
          'form': CommentForm()
        })
        return context
    



def get_comment(request):
    if request.method == 'POST': #its not POST, its GET
        form = CommentForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = CommentForm()
    return render(request, 'zine/get_comment.html', {'form': form})

def write_comment(request, post_id):
    body = request.POST
    print(body)
    print(post_id)
    # for code in body.getlist('codesfield'):
        # code_obj = get_object_or_404(DatasetCode, pk=code)
    comment = Comment(
        author = request.user,
        text= request.POST['text'],
        post_id=post_id
    )
    comment.save()


    return HttpResponseRedirect(reverse('zine:post_detail', kwargs={'pk':post_id}))
     
