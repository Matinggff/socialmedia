from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile,Post,Like,Comment
from django.contrib import auth
from django.contrib.auth.hashers import make_password
@login_required(login_url="core:signin")
def home(request):
    user_profile = Profile.objects.get(username = request.user)
    posts = Post.objects.all()
    context = {
        'home':user_profile,
        'posts':posts,
        'crn_user':request.user.username
               }
    return render(request,'index.html',context)

def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2 and len(password) >= 8:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username has been taken")
                return redirect("core:signup") #name url

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email has been taken")
                return redirect("core:signup")

            else:
                user_object = User.objects.create(username=username,email=email,password=make_password(password))
                user_object.save()
                user = User.objects.get(username=username)

                user_profile = Profile.objects.create(username=user)
                user_profile.save()
                auth.login(request,user)
                return redirect('core:setting')
        else:
            messages.info(request,"Passwords are not the same")
            return redirect("core:signup")
    else:
        return render(request,"signup.html")                

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("core:home")
        else:
            messages.info(request,"Invalid credentials")
            return redirect("core:signin")
    else:
        return render(request,'signin.html')
    
@login_required(login_url="core:signin")
def log_out(request):
    auth.logout(request)
    return render(request,'signin.html')

@login_required(login_url="core:signin")
def setting(request):
    user_profile = Profile.objects.get(username = request.user)
    if request.method == "POST":
        if request.FILES.get('image') == None:
            user_profile.address = request.POST['location']
            user_profile.bio = request.POST['bio']
            user_profile.save()
        elif request.FILES.get('image') != None:
            user_profile.profile_image = request.FILES.get('image')
            user_profile.address = request.POST['location']
            user_profile.bio = request.POST['bio']
            user_profile.save()
    return render(request,'setting.html', context={'profile':user_profile})

def upload(request):
    if request.method == 'POST':
        user = request.user.username
        caption = request.POST['caption']
        image = request.FILES.get('image')
        
        new_post = Post.objects.create(user=user,caption=caption,image=image)
        new_post.save()
        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url="core:signin")
def profile(request,username):
    user_object = User.objects.get(username=username)
    user_profile = Profile.objects.get(username=user_object)
    user_posts = Post.objects.filter(user= user_profile.username.username)
    context = {
        'user_object':user_object,
        'user_profile':user_profile,
        'user_posts':user_posts,
        'posts':len(user_posts)
    }
    return render(request,'profile.html',context)

def like(request,post_id):
    post = Post.objects.get(id=post_id)
    is_like = Like.objects.filter(post_id = post.id, user=request.user.username)

    if is_like.exists():
        is_like.delete()
        post.no_likes -= 1
        post.save()
        return redirect("/")
    elif not is_like.exists():
        new_like = Like.objects.create(post_id = post.id, user=request.user.username)
        new_like.save()
        post.no_likes +=1
        post.save()
        return redirect("/")

def comment(request):
    if request.method == "POST":
        author = request.user.username
        comment = request.POST['comment']
        postid = request.POST['postid']
        postuser = request.POST['postuser']
    
        post= Post.objects.get(id=postid)
        new_comment = Comment.objects.create(author=author, post=post, user=postuser, comment=comment)
        new_comment.save()
        messages.info(request,f"You add comment for post of {postuser}")
        return redirect('/')

    else:
        return redirect('/')

def delete(request,post_id):
    post_obj = Post.objects.get(id=post_id)
    post_obj.delete()
    return redirect('/')
        
        
