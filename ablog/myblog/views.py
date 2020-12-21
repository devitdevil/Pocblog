from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse

from .models import Post,Category
from .forms import PostForm,EditForm
from django.http import HttpResponseRedirect

def LikeView (request, pk):
    print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",pk)
    post=get_object_or_404(Post,id=pk)
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))

class HomeView(ListView):
    model=Post
    template_name ='home.html'
    ordering = ['-id']
    paginate_by = 3

def CategoryView(request,cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'category.html', {'cats':cats.title(),'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model=Post
    template_name ='article_detail.html'

class AddpostView(CreateView):
    model=Post
    form_class = PostForm
    template_name='add_post.html '
    #fields = '__all__'

class AddCategoryView(CreateView):
    model=Category
    template_name='add_category.html '
    fields = '__all__'

class UpdatePostView(UpdateView):
    model=Post
    template_name='update_post.html'
    form_class = EditForm

    #fields = ['title','title_tag','body']

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')









































# def upvote(request, pk):
#     if request.method == 'POST':
#         upvote_count = get_object_or_404(Post,pk = pk)
#         upvote_count.upvote +=1
#         upvote_count.save()
#         return redirect('/')


# def LikeView (request, pk):
#     post=get_object_or_404(Post,id=request.POST.get('post_id'))
#     post.likes.add(request.user)
#     return HttpResponseRedirect(reverse('article-detail',args=[(pk)]))