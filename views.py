from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blogApp.models import Post, Comment
from blogApp.forms import commentForm, postForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from datetime import datetime


# Create your views here.
#### VIEWS FOR POSTS #####
class aboutView(TemplateView):
    template_name = 'about.html'

class myLoginView(LoginView):
    template_name = 'login.html'

class myLogoutView(LogoutView):
    template_name = 'login.html'
    


class postListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publishedDate__lte = datetime.now()).order_by('-publishedDate')
    

class postDetailView(DetailView):
    model = Post


class createPostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blogApp/post_detail.html'
    
    form_class = postForm
    model = Post

class updatePostView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blogApp/post_detail.html'
    
    form_class = postForm
    model = Post

class deletePostView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    success_url = reverse_lazy('postList')
    def get_queryset(self):
        return Post.objects.filter(publishedDate__lte = datetime.now()).order_by('-publishedDate')
    

class draftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blogApp/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publishedDate__isnull=True).order_by('createDate')
    

####VIEWS FOR COMMENTS #####

@login_required
def addCommentToPost(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('postDetail', pk=post.pk)
    else:
        form = commentForm()
    return render(request,'blogApp/comment_form.html',{'form': form})
@login_required
def commentApprove(request, pk):
   comment = get_object_or_404(Comment, pk=pk)
   comment.approve()
   return redirect('postDetail', pk = comment.post.pk) 

@login_required
def commentDelete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    postPk = comment.post.pk
    comment.delete()
    return redirect('postDetail', pk = postPk)

@login_required
def postPublish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('postDetail', pk = pk)


