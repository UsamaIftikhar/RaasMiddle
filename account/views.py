from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import UserForm, AppForm, CompanyForm,NewAppForm
from account.models import *
from django.db import connection

cursor = connection.cursor()


def register(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'register.html', {'form': form})
    else:
        form = UserForm()
        email = request.POST.get('email')
        try:
            credentials = None
            credentials = userInfo.objects.get(email=email)
        except Exception:
            print("Good To Go")
        if credentials is not None:
            messages.error(request, 'Email Already Taken')
            return render(request, 'register.html', {'form': form})
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


def newregister(request):
    if request.method == 'GET':
        form = CompanyForm()
        return render(request, 'register.html', {'form': form})
    else:
        form = CompanyForm()
        email = request.POST.get('email')
        try:
            credentials = None
            credentials = userInfo.objects.get(email=email)
        except Exception:
            print("Good To Go")
        if credentials is not None:
            messages.error(request, 'Email Already Taken')
            return render(request, 'register.html', {'form': form})
        else:
            allCompanies=company.objects.all()
            for singleCompany in allCompanies:
                if singleCompany.email == email:
                    messages.error(request, 'Email Already Taken')
                    return render(request, 'register.html', {'form': form})
            form = CompanyForm(request.POST, request.FILES)
            post = request.POST.copy()  # to make it mutable
            import uuid
            allKeysList = Keys.objects.all()
            company_id = None
            found = True
            while found is True:
                company_id = uuid.uuid1()
                print(company_id)
                found = True
                for key in allKeysList:
                    if str(key) != str(company_id):
                        found = False
                    else:
                        found = True

                if found is False:
                    break
                if allKeysList.count() == 0:
                    break

            print(company_id)
            post['company_id'] = company_id
            request.POST = post
            form = CompanyForm(request.POST, request.FILES)
            keyObj=Keys()
            keyObj.key_id=company_id
            if form.is_valid():
                form.save()
                keyObj.save()
                messages.success(request, 'Successfully Registered In')
                return redirect('newregister')

            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('newregister')


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
            messages.error(login_request, "Invalid entry!")
            return render(login_request, 'login.html', {'form': form})
        else:
            login_request.session['email'] = email
            print(login_request.session.get('email'))
            print(credentials.id);
            # cursor.execute('''SELECT id FROM public.account_userinfo WHERE email=$email;''')
            # row = cursor.fetchone()
            # print (row)
            # messages.success(login_request, 'Successfully logged In')
            return redirect('dashboard')


def newlogin(login_request):
    if login_request.method == 'GET':
        form = CompanyForm()
        # messages.success(login_request, 'Successfully Registered In')
        return render(login_request, 'login.html', {'form': form})
    else:
        email = login_request.POST.get('email')
        password = login_request.POST.get('password')
        print("email ",email)
        print("password ",password)
        try:
            credentials = None
            print("None")
            credentials = company.objects.get(email=email, password=password)
            print(credentials.company_id)
        except:
            print("Invalid Entry")
        if credentials is None:
            form = CompanyForm()
            messages.error(login_request, "Invalid entry!")
            return render(login_request, 'login.html', {'form': form})
        else:
            login_request.session['email'] = email
            print(login_request.session.get('email'))
            print(credentials.company_id);
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
        email = update_response.POST.get('email')
        try:
            credentials = None
            credentials = userInfo.objects.get(email=email)
        except Exception:
            print("Good To Go")
        if credentials is not None:
            messages.error(update_response, 'Email Already Taken!')
            form = UserForm(update_response.POST, update_response.FILES, instance=obj)
            return render(update_response, 'update.html', {'form': form})
        else:
            form = UserForm(update_response.POST, update_response.FILES, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('welcome')


def welcome(welcomes):
    return render(welcomes, "welcome.html")

def showApps(request):
    allApps=APP.objects.all()
    email = request.session.get('email')
    loggedInCompany = company.objects.get(email=email)
    # print(loggedInCompany.company_id)
    companies_apps=list()
    for app in allApps:
        # print(app.company_id)
        if str(app.company_id_id)==str(loggedInCompany.company_id):
            # print("found")
            companies_apps.append(app)

    # print(companies_apps)
    return companies_apps


def addapp(request):
    if request.method == 'GET':
        form = AppForm()
        return render(request, 'addapp.html', {'form': form})
    else:
        form = AppForm()
        appname = request.POST.get('appname')
        webaddress = request.POST.get('webaddress')

        email = request.session.get('email')
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
        # form.fields['user_id'] = int(1)
        if form.is_valid():
            # and update original POST in the end
            request.POST = post
            form = AppForm(request.POST, request.FILES)
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('addapp')


def newaddapp(request):
    if request.method == 'GET':
        form = NewAppForm()
        applist=showApps(request)
        email = request.session.get('email')

        credentials = company.objects.get(email=email)
        # companyid=applist[0].company_id_id
        return render(request, 'addapp.html', {'form': form, 'applist':applist,'companyID':credentials.company_id})

    else:
        form = NewAppForm()
        appname = request.POST.get('appname')
        webaddress = request.POST.get('webaddress')

        email = request.session.get('email')
        print(request.session.get('email'))
        credentials = company.objects.get(email=email)
        # print(credentials.company_id_id);
        user_id = credentials.company_id;
        post = request.POST.copy()  # to make it mutable
        allKeysList=Keys.objects.all()
        app_id = None
        found = True
        import  uuid
        while found is True:
            app_id = uuid.uuid1()
            print(app_id)
            found = True
            for key in allKeysList:
                if str(key) != str(app_id):
                    found = False
                else:
                    found = True

            if found is False:
                break
            if allKeysList.count() == 0:
                break

        post['app_id'] = app_id
        post['company_id'] = credentials.company_id;
        # and update original POST in the end
        request.POST = post
        form = NewAppForm(request.POST, request.FILES)
        keyObj = Keys()
        keyObj.key_id = app_id
        if form.is_valid():
            # and update original POST in the end
            request.POST = post
            form = NewAppForm(request.POST, request.FILES)
            form.save()
            keyObj.save()
            messages.error(request,"COMPANY ID: " + str(credentials.company_id ))
            messages.error(request,"APP ID: "+ str(app_id) )
            return redirect('newaddapp')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('newaddapp')


def dashboard(request):
    email = request.session.get('email')

    credentials = company.objects.get(email=email)
    applist=showApps(request)

    return render(request, 'dashboard.html', {'applist': applist})


def logout(request):
    del request.session['email']
    return redirect('newlogin')

from rest_framework import viewsets, generics

from myapi.serializers import *



class CompanyViewSet(viewsets.ModelViewSet):
    queryset = company.objects.all()
    serializer_class = CompanySerializer

class AppsViewSet(viewsets.ModelViewSet):
    queryset = APP.objects.all()
    serializer_class = AppsSerializer

class AppsViewSet(viewsets.ModelViewSet):
    queryset = APP.objects.all()
    serializer_class = AppsSerializer


# class VerifyKeyViewSet(viewsets.ModelViewSet):
#     # sequerysetApps = APP.objects.all()
#     serializer_class = AppsSerializer
#
#     def get_queryset(self):
#         """
#         Optionally restricts the returned purchases to a given user,
#         by filtering against a `username` query parameter in the URL.
#         """
#         queryset = APP.objects.all()
#         appid = self.request.query_params.get('appid', None)
#         companyid = self.request.query_params.get('companyid', None)
#         if appid is not None and companyid is not None:
#             queryset = queryset.filter(app_id=appid , company_id=companyid)
#         return queryset
#

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import HttpResponse,JsonResponse
# @api_view()
# @permission_classes([AllowAny])
def specsView(request,appid,companyid):

    queryset = APP.objects.all()
    row=None
    objApp=None
    if appid is not None and companyid is not None:
            objApp = queryset.filter(app_id=appid , company_id=companyid)


    if objApp is None:
        return JsonResponse({}, safe=False)
    data = list(objApp)
    app=objApp.first()
    import json
    from django.forms.models import model_to_dict
    obj=  model_to_dict(app)
    return JsonResponse(obj, safe=False)



