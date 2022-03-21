from django.shortcuts import render,redirect
from .models import Post,Likes,DisLikes,Tags,Comments,Category
from .forms import comment_form , post_form, edit_post_form, category_form, tags_form

#--------------------------------------------------------------------------------------------------------
# view all posts oredered by created date and show only most new 9 posts 
def allPosts(request):
    posts = Post.objects.order_by('-created')[:9] 
    form = post_form()
    categories = Category.objects.all()
    if request.method == 'POST':
        form = post_form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save_m2m()
            return redirect('allposts')
        else:
            form = post_form()
    context = {
        'allposts': posts,
        'form': form,
        'categories': categories,
        }
    return render(request, 'allposts.html', context)


def categoryPosts(request, categoryID):
    posts = Post.objects.filter(category= categoryID)
    form = post_form()
    categories = Category.objects.all()
    context = {
        'allposts': posts,
        'form': form,
        'categories': categories,
        }
    return render(request, 'allposts.html', context)


def showPost(request, postID):
    post = Post.objects.get(id = postID)
    categories = Category.objects.all()
    tags = Tags.objects.all()
    # To enter a new comment
    if request.method == 'POST':
        comment_form = comment_form(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False) # commit=False means not save yet
            instance.user = request.user # send user name with comment
            instance.post = post # make relation between post and comment
            instance.save()
            return redirect('post', postID = post.id)
    else:
        comment_form = comment_form()
    context = {
        'post': post,   
        'comment_form': comment_form,
        'categories': categories,
        'tags': tags,
        }
    return render(request, 'post.html', context)


def postEdit(request, postID):
    if request.user.is_authenticated:
        post = Post.objects.get(id = postID)
        form = edit_post_form(instance=post)
        categories = Category.objects.all()
        tags = Tags.objects.all()
        if request.method=='POST':
            form = edit_post_form(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('post', postID=post.id)
            else:
                form = edit_post_form(instance=post)

        context = {
            'post': post, 
            'form': form,
            'categories': categories,
            'tags': tags,
            }
        return render(request, 'editpost.html', context)
    else:
        return redirect('allposts')


def postDelete(request, postID):
    if request.user.is_authenticated and request.user.is_superuser:
        post = Post.objects.get(id=postID)
        post.delete()
    return redirect('allposts')


def likePost(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            post_id = request.POST.get('post_id')
            post_obj = Post.objects.get(id=post_id)

            if user in post_obj.liked.all():
                post_obj.liked.remove(user)
                post_obj.disliked.add(user)
            else:
                post_obj.liked.add(user)
                post_obj.disliked.remove(user)
            
            post_obj.save()
    return redirect('allposts')


def dislikePost(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            post_id = request.POST.get('post_id')
            post_obj = Post.objects.get(id=post_id)

            if user in post_obj.disliked.all():
                post_obj.disliked.remove(user)
                post_obj.liked.add(user)
            else:
                post_obj.disliked.add(user)
                post_obj.liked.remove(user)
            
            post_obj.save()
    return redirect('allposts')


def addCategory(request):
    #if user is logged in and user is admin he can create category
    if request.user.is_authenticated and request.user.is_superuser:
        form = category_form()
        if request.method == "POST":
            form = category_form(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('allposts')
        context = {'form': form}
        return render(request, 'add_cat.html', context)
    else:
        return redirect('allposts')   

