from django.shortcuts import render,redirect,get_object_or_404
from blog.models import Post
from blog import forms
from django.http import HttpResponseRedirect
from taggit.models import Tag
from django.contrib.auth.decorators import login_required

# Create your views here.
def postlist_view(request,tag_slug=None):
    post_list=Post.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])
    return render(request,'blog/post_list.html',{'post_list':post_list,'tag':tag})

def postcreate_view(request):
    form=forms.CreateForm()
    if request.method=='POST':
        form=forms.CreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    return render(request,'blog/post_create.html',{'form':form})

@login_required
def postdetail_view(request,year,month,day,post):
    post=get_object_or_404(Post,status='published',slug=post,publish__year=year,publish__month=month,publish__day=day)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=forms.CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=forms.CommentForm()
    likes=post.likes.filter(active=True)
    click=False
    if request.method=='POST':
        form1=forms.LikeForm(request.POST)
        if form1.is_valid():
            new_like=form1.save(commit=False)
            new_like.post=post
            new_like.save()
            click=True
    else:
        form1=forms.LikeForm()
    return render(request,'blog/post_detail.html',{'post':post,'comments':comments,'csubmit':csubmit,'form':form,'form1':form1,'click':click,'likes':likes})

def postupdate_view(request,id):
    post_list=Post.objects.get(id=id)
    if request.method=='POST':
        form=forms.UpdateForm(request.POST,instance=post_list)
        if form.is_valid():
            form.save()
        return redirect('/home')
    return render(request,'blog/post_update.html',{'post_list':post_list})

def postdelete_view(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return redirect('/home')

def signup_view(request):
    form=forms.SignUpForm()
    if request.method=='POST':
        form=forms.SignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=True)
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'blog/signup.html',{'form':form})

def logout_view(request):
    return render(request,'blog/logout.html')
