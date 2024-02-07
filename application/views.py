from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Blog_category,Blog_post,add_Likes,add_views,add_comments
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.
def home(request):
    if request.method == 'GET':
     x=Blog_category.objects.all()
     return render(request, 'index.html',{"category":x})
    else:
        Data=request.POST.get('data')
        print(Data)
        x=Blog_category.objects.filter(Q(category_name__icontains=Data))
        return render(request, 'index.html',{"category":x})


def input(request):
    if request.method == 'GET':
        return render(request, 'form.html')
    else:
        name = request.POST.get('blogname')
        image = request.FILES.get('img')
        content = request.POST.get('blog_content')
        x=Blog_category(category_name=name,blog_img=image,blog_summary=content)
       
        x.save()
        

        return render(request, 'form.html',{"Category":"Your Response is Submitted Successfully!"})
def View(request,blog_id ,blog_category_name):
    if request.method == 'GET':

     x=Blog_category.objects.get(id=blog_id)
     y=Blog_post.objects.filter(category_name=Blog_category.objects.get(category_name=blog_category_name))
     print(y)
     return render(request, 'allblog.html',{"Data":x, "Category":y})
    else:
     Data=request.POST.get('data')   
     x=Blog_category.objects.get(id=blog_id)
     y=Blog_post.objects.filter(Q(Blog_Name__icontains=Data))
     print(y)
     return render(request, 'allblog.html',{"Data":x, "Category":y})

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid username or password'})

    else:
        return render(request,'registration/login.html')
def Sign_up(request):
    if request.method == 'GET':

     return render(request, 'registration/signup.html')
    else:
        username=request.POST.get('username')
        mail=request.POST.get('mail')
        password=request.POST.get('password')
        Confirm_password=request.POST.get('Confirm_password')
        print(username,mail,password,Confirm_password)
        Name=User.objects.get(username=username)
        if Name is not None:
            return render(request,'registration/signup.html',{'message':"User Already Registered Please Enter New User"})
        user=User.objects.create_user(username,mail,password)
        user.save()
        return render(request, 'registration/login.html',{'message':"Account Created Successfully"})

def Logout(request):
     logout(request)
     return redirect("/")

def Change_Password(request):
    if request.method=='GET':
        return render(request,'registration/change_pass.html',{"Password":"Please Enter the Deatails Carefully"})
    else:
        Username=request.POST.get('username')
        Old_password = request.POST.get('old_password')
        x=authenticate(request,username=Username,password=Old_password)
        if x is not None:
            U=User.objects.get(username=Username)
            U.set_password(request.POST.get('password'))
            U.save()
            return render(request,'registration/change_pass.html',{"Password":"Password Changed Successfully"})
        else:
            return render(request,'registration/change_pass.html',{"Password":"Check your Old Password"})    
                
def View_blog(request,blog_id):
    if request.method == 'GET':

     x=Blog_post.objects.get(id=blog_id)
     z=add_Likes.objects.filter(blog_id=Blog_post.objects.get(Blog_Name=x.Blog_Name)).count()
     #print(x.Blog_Name)
     y=add_views(blog_id=Blog_post.objects.get(Blog_Name=x.Blog_Name))
     y.save()
     k=add_views.objects.filter(blog_id=Blog_post.objects.get(Blog_Name=x.Blog_Name)).count()
     b=add_comments.objects.filter(blog_id=Blog_post.objects.get(Blog_Name=x.Blog_Name))
     Comment=""
     for c in b:
        print(c.comment)
        Comment=str(c.comment)
        
     print(Comment)
     #print(k)
     return render(request,'View_blog.html',{"Data":x,"Count":z,"views":k,"Comment":b})
    else:
        comment=request.POST.get('comment')
        #print(comment)
        if comment:
            x=Blog_post.objects.get(id=blog_id)
            #print(x.Blog_Name)
            username = request.user.username
            print(username)
            a=add_comments(blog_id=Blog_post.objects.get(Blog_Name=x.Blog_Name),comment=comment,username=username)
            a.save()
            #print(a.comment)
            b=add_comments.objects.filter(blog_id=Blog_post.objects.get(Blog_Name=x.Blog_Name)).order_by('-id')
            z=add_Likes.objects.filter(blog_id=Blog_post.objects.get(Blog_Name=x.Blog_Name)).count()
            k=add_views.objects.filter(blog_id=Blog_post.objects.get(Blog_Name=x.Blog_Name)).count()
            Comment=""
            for c in b:
                #print(c.comment)
                Comment=str(c.comment)
                
            print(Comment)    
            return render(request,'View_blog.html',{"Data":x,"Count":z,"Greet":"Thanks for your feedback","views":k,"Comment":b})
        else:

         x=Blog_post.objects.get(id=blog_id)
         #print(x.Blog_Name)
         y=add_Likes(blog_id=Blog_post.objects.get(Blog_Name=x.Blog_Name))
         y.save()
         #print(y)
         z=add_Likes.objects.filter(blog_id=Blog_post.objects.get(Blog_Name=x.Blog_Name)).count()
         print(z)
         k=add_views.objects.filter(blog_id=Blog_post.objects.get(Blog_Name=x.Blog_Name)).count()
         b=add_comments.objects.filter(blog_id=Blog_post.objects.get(Blog_Name=x.Blog_Name)).order_by('-id')
         Comment=""
         for c in b:
            #print(c.comment)
            Comment=str(c.comment)
            
         print(Comment)
         return render(request,'View_blog.html',{"Data":x,"Count":z,"Greet":"Thanks for your feedback","views":k, "Comment":b})      
          