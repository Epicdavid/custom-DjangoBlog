from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic.edit import (CreateView,UpdateView,DeleteView,FormMixin)
from django.views.generic import (View,TemplateView,ListView,DetailView,)
from blog.models import Post,MyComment
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm,MyCommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from django.utils import timezone

# Create your views here.

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published__lte=timezone.now()).order_by('-published')
    

    template_name = 'blog/post-list.html'
class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post-details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MyCommentForm
        return context



class CreatePost(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Post
    redirect_field_name = 'blog/post-detail.html'
    form_class = PostForm
    template_name = 'blog/post-form.html'

@login_required
def publish_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('blog:post_detail',pk=pk)    

class UpdatePost(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    model = Post
    redirect_field_name = 'blog/post-detail.html'
    form_class = PostForm
    template_name = 'blog/edit_form.html'

    

class DeletePost(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')
    template_name = 'blog/confirm_delete_post.html'

class DraftView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post-list.html'
    model = Post    
    template_name = 'blog/drafts.html'

    def get_queryset(self):
        return Post.objects.filter(published__isnull=True).order_by('created')


def makecomments(request, pk):
    template_name = 'blog/comment_form.html'
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = MyCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form = MyCommentForm()
    return render(request, 'blog/post_detail.html',{'form':form})


@login_required
def approve_comment(request, pk):
    comment = get_object_or_404(MyComment, pk=pk)
    comment.approve()
    return redirect('blog:post_detail',pk=comment.post.pk)

@login_required
def delete_comment(request,pk):
    comment = get_object_or_404(MyComment,pk=pk)
    post_pk = comment.post.pk
    comment.delete_comment()
    return render(request, 'blog:post_detail',pk=post_pk)

