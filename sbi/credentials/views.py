from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import ForumForm
from .models import Forum,District,Branch




def register(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                print('Username taken')
                messages.info(request,'Username taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print('user saved')
                return redirect('login')

        else:
            messages.info(request,'Password is not matching')
            return redirect('register')
    return render(request,'register.html')


def login(request):

    if request.method == 'POST':
        name1 = request.POST['name1']
        password = request.POST['password']
        user = auth.authenticate(username=name1, password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            return redirect('preform')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def preform(request):
    return render(request,'preform.html')

def success(request):
    return render(request,'success.html')



def addForm(request):
    if request.method == 'POST':
        forum_form = ForumForm(request.POST)
        print('forumform')
        if forum_form.is_valid():
            forum_form.save()
            return redirect("success")
        else:
            return redirect("form1")

    forum_form = ForumForm()

    forum = Forum.objects.all()
    print(forum)
    district = District.objects.all()
    branch = Branch.objects.filter()
    context = {'forum_form': forum_form, 'forum': forum, 'district': district, 'branch': branch}

    return render(request,"form1.html",context)


def load_branches(request):
    district_id = request.GET.get('district')
    branches = Branch.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'branch_dropdown_list_options.html', {'branches': branches})









