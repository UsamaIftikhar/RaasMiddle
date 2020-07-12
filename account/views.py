from Tools.scripts.serve import app
from django.db.models import Model
from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import UserForm,AppForm
from django.contrib.auth.models import User
from account.models import userInfo
from django.contrib.auth import login
from django.contrib.sessions import *
from django.db import connection
cursor = connection.cursor()
def register(request):

    if request.method == 'GET':
        form = UserForm()
        return render(request, 'register.html', {'form': form})
    else:
        form = UserForm()
        email= request.POST.get('email')
        try:
            credentials=None
            credentials = userInfo.objects.get(email=email)
        except Exception:
            print("Good To Go")
        if credentials is not None:
            messages.error(request, 'Email Already Taken')
            return render(request,'register.html',{'form':form})
        else:
            form = UserForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # request.session['email']=email
                # print(request.session.get('email'))
                messages.success(request, 'Successfully Registered In')
                return redirect('register')

            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('register')


def login(login_request):

    if login_request.method == 'GET':
        form = UserForm()
        # messages.success(login_request, 'Successfully Registered In')
        return render(login_request, 'login.html', {'form': form})
    else:
        email = login_request.POST.get('email')
        password = login_request.POST.get('password')
        try:
            credentials = None
            credentials = userInfo.objects.get(email=email, password=password)
        except:
            print("Invalid Entry")
        if credentials is None:
            form = UserForm()
            messages.error(login_request,"Invalid entry!")
            return render(login_request,'login.html',{'form':form})
        else:
            login_request.session['email'] = email
            print(login_request.session.get('email'))
            print(credentials.id);
            # cursor.execute('''SELECT id FROM public.account_userinfo WHERE email=$email;''')
            # row = cursor.fetchone()
            # print (row)
            # messages.success(login_request, 'Successfully logged In')
            return redirect('dashboard')


def update(update_response, id):
    obj = userInfo.objects.get(id=id)

    if update_response.method == 'GET':
        form = UserForm(instance=obj)
        return render(update_response, 'update.html', {'form': form})
    else:
        form = UserForm()
        email= update_response.POST.get('email')
        try:
            credentials=None
            credentials = userInfo.objects.get(email=email)
        except Exception:
            print("Good To Go")
        if credentials is not None:
            messages.error(update_response, 'Email Already Taken!')
            form = UserForm(update_response.POST, update_response.FILES, instance=obj)
            return render(update_response,'update.html',{'form':form})
        else:
            form = UserForm(update_response.POST, update_response.FILES,instance=obj)
            if form.is_valid():
                form.save()
                return redirect('welcome')

def welcome(welcomes):
    return render(welcomes, "welcome.html")

def addapp(request):
    if request.method == 'GET':
        form = AppForm()
        return render(request, 'addapp.html', {'form': form})
    else:
        form = AppForm()
        appname = request.POST.get('appname')
        webaddress=request.POST.get('webaddress')

        email=request.session.get('email')
        print(request.session.get('email'))
        credentials = userInfo.objects.get(email=email)
        print(credentials.id);
        user_id = credentials.id;
        # try:
        #     credentials = None
        #     credentials = userInfo.objects.get(email=email)
        # except Exception:
        #     print("Good To Go")
        # if credentials is not None:
        #     messages.error(request, 'Email Already Taken')
        #     return render(request, 'appdata.html', {'form': form})
        # else:
        # form = AppForm(request.POST, request.FILES)
        post = request.POST.copy()  # to make it mutable
        import uuid
        app_id = uuid.uuid1()
        post['app_id'] = app_id
        post['user_id'] = credentials.id;
        # and update original POST in the end
        request.POST = post
        form = AppForm(request.POST, request.FILES)
        # import uuid
        # app_id = uuid.uuid1()
        # appid=request.POST[app_id]
        # request.POST._mutable = True
        #form.fields['user_id'] = int(1)
        if form.is_valid():
            # and update original POST in the end
            request.POST = post
            form = AppForm(request.POST, request.FILES)
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('addapp')
def dashboard(request):
    email = request.session.get('email')

    credentials = userInfo.objects.get(email=email)
    return render(request,'dashboard.html',{'email': email})
def logout(request):

    del request.session['email']
    return redirect('login')
