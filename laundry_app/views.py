from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from laundry_app.models import Catogary_name, Item_detail, person
from laundry_app.models import *

from django.contrib.auth import authenticate

from . import forms
# Create your views here.

def laundryHome(request):
    session_value = request.session.get('session_name')
    cookies = request.COOKIES.get('username')
    if cookies != None:
        print('Cookies consist value')
        return render(request, 'laundry/index.html', {'cookies':cookies} )
    elif session_value != None:
        print('Session Value : '+session_value)
        return render(request, 'laundry/index.html', {'session':session_value } )
    else:
        print('Empty Cookies and Session')
        return render(request, 'laundry/index.html' )

def pricing(request):
    session_value = request.session['session_name']
    cookies = request.COOKIES.get('username') 
    catogary_list = Catogary_name.objects.order_by('catg_name')
    price_list = Item_detail.objects.order_by('Item_name')
    price_dict = { 'item_details' : price_list, 'category' : catogary_list, 'cookies': cookies, 'session':session_value }
    return render(request, 'laundry/pricing.html', context=price_dict)

def branches(request):
    session_value = request.session['session_name']

    cookies = request.COOKIES.get('username') 
    branches_list = Branch.objects.order_by('Name')
    branches_dict = { 'branches' : branches_list, 'cookies':cookies, 'session':session_value }
    return render(request, 'laundry/branches.html', context=branches_dict)

def contact(request):
    session_value = request.session['session_name']
    cookies = request.COOKIES.get('username') 
    return render(request, 'laundry/contact.html', {'cookies':cookies, 'session':session_value})

def aboutus(request):
    session_value = request.session['session_name']
    cookies = request.COOKIES.get('username') 
    return render(request, 'laundry/aboutus.html', {'cookies':cookies, 'session':session_value})

def client(request):
    pass

def signup(request):

    # Receiving form input on views.py file    
    if request.method == 'POST':
        Firstname = request.POST['firstname']
        Lastname = request.POST['lastname']
        Address = request.POST['address']
        Subscription = request.POST['subscription']
        Phone = request.POST['phone']
        Email = request.POST['email']
        Passwd = request.POST['password']
        ConformPassword = request.POST['conformpassword']

        signup_obj = ClientDetail( First_Name = Firstname, Last_Name = Lastname, Address = Address, Subscription_Package = Subscription, Phone = Phone, Email = Email, Password = Passwd, Conform_Password = ConformPassword )
        signup_obj.save()

        print('FirstName : ' +Firstname)
        print('Subscription: ' +Subscription)
        return HttpResponseRedirect('signin')

    return render(request,'laundry/signup.html')


def signin(request):
    if request.method == 'POST':
        uname = (request.POST['username']).strip()
        Password = (request.POST['password']).strip()
        remember_me = request.POST.get('remember', False)
        print('Username :{}'.format(uname))
        print('Password :'+Password)
        print('Remember Me :'+str(remember_me))

    client_list = ClientDetail.objects.all()
    
    if (uname == ' ' or uname == None ):
        print('Username empty')

    if (Password == ' ' or Password == None ):
        print('Username empty')


    for i in client_list:       
        print(i.Phone,i.Email,i.Password)
        if i.Phone==uname or i.Email==uname and i.Password==Password:
            print('Login Successful')
            client_name = i.First_Name +"    "+ i.Last_Name
            if remember_me == 'checked': 
                request.session['session_name'] = client_name
                print('Session is set')
                return redirect('laundryIndexPage')
            else:
                print('Unchecked Remember me')
                response = redirect('laundryIndexPage')
                response.set_cookie('username',client_name)
                return response
        else:
            LoginError = "Error: username and password doesn't match. Please try again"
            print('Username Password doesnot match')
            response = render(request,'laundry/signup.html',{'message':LoginError})
            return response
    
    return render(request, 'laundry/signup.html' )
    
           
def logout(request):
    if request.COOKIES.get('username'):     
        response = redirect('laundryIndexPage')
        response.delete_cookie('username')
    elif request.session.has_key('session_name'):
        request.session.flush()
        response = redirect('laundryIndexPage')
    else:
        response = redirect('laundryIndexPage')
    
    return response


# Learn Section

def index(request):
    return HttpResponse('<h1>Hello Beautiful People</h1>')

def learn(request):

    user_list = person.objects.order_by('firstName')

    Form = forms.formExample()      # using form
    ModelFormExample = forms.personForm()  # using ModelForm 

    if request.method == 'POST':
        ModelFormExample = forms.personForm(request.POST)
        try:
            if ModelFormExample.is_valid():
                ModelFormExample.save(commit = True)
                return render(request, 'other.html' )
        except:
            print('Something went wrong')


    # Check to see if we get a POST back
    if request.method == 'POST':
        # IN which case we pass in that request.
        form = forms.formExample(request.POST)

        # Check to see form is valid
        if form.is_valid():
            # Do Something
            print("Form Validation Success. Prints in console")
            print("Name :" +form.cleaned_data['name'])
            print("Email :" +form.cleaned_data['email'])
            print("Message :" +form.cleaned_data['text'])
    
    Session = " "
    Session = request.session.get('user_name')    
    if Session == None:
        Session = " "
            
    user_Dict = { 'user_details' : user_list, 'form':Form, 'ModelForm': ModelFormExample, 'SessionName':Session }
    
    return render(request, 'learn.html', context = user_Dict )

def other(request):
    return render(request, 'other.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['password']
        print(uname)
        print(password)

    loginCheck = registeration.objects.filter(Username=uname, Password=password)
    if loginCheck:
        request.session['user_name'] = uname        
        return redirect('learnPage')
    else:
        return redirect('other')
    return render(request,'laundry/learn.html')

def register(request):
    
    if request.method=='POST':
        UserName = request.POST['Username']
        Passwd = request.POST['Password']
        CPasswd = request.POST['CPassword']
 
    object1 = registeration( Username = UserName, Password=Passwd, CPassword=CPasswd)
    object1.save()

    return redirect('login')    

def userAuth(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.userProfileInfo(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES :
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True
         
        else:
            print(user_form.errors, profile_form.errors)
    
    else:
        user_form = forms.UserForm()
        profile_form = forms.userProfileInfo()

    return render(request, 'userAuth.html', {'userForm': user_form, 'profile_form': profile_form, 'registered':registered } )

def userLogin(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passKey = request.POST.get('password')

        user = authenticate(username=uname, password=passKey)
        print(uname)
        print(passKey)
        if user:
            return redirect('learnPage')
        else:
            return redirect('userLogin')
    return render(request,'userLogin.html')

def userLogout(request):
    logout(request)
    return redirect('learnPage')

# FILE UPLOAD TUTORIAL
def fileUpload(request):
    if request.method == 'POST':
        htmlUploadFile = request.FILES['html']
        print(htmlUploadFile.name)
        print(htmlUploadFile.size)
        upload_object = uploadFile(htmlupload = htmlUploadFile)
    try:
       upload_object.save()
    except:
        print('Upload Error')
    return render(request,'fileupload.html')

def crud(request):
    if request.method == 'POST':
        Id = request.POST['sId']
        Name = request.POST['sName']
        Phone = request.POST['sPhone']
        Birthday = request.POST['birthdate']

        if Id == '' or Id == None and Name == None or Name =='' and Phone == None or Phone == '' and Birthday == None or Birthday == '':
            print('Empty Field')
        else:
            crud_object = CRUD(StudentId=Id, StudentName=Name, StudentPhone=Phone, Birthday=Birthday)
            crud_object.save()
            print(Id +"   "+ Name +"   "+ Phone +"   "+Birthday)
            return redirect('crud')
    
    Student = CRUD.objects.all()
    return render(request, 'crud.html', {'Student':Student})

def edit(request):
    if request.method == 'POST':
        updateID = request.POST['sId']
        updateName = request.POST['sName']
        updatePhone = request.POST['sPhone']
        updateBirthday = request.POST['birthdate']        

        delObject = CRUD.objects.filter(StudentId=updateID)
        delObject.delete()
        
        updateObject = CRUD(StudentId=updateID, StudentName=updateName, StudentPhone=updatePhone, Birthday=updateBirthday)
        updateObject.save()
        
        return redirect('crud')


class next(View):
    def one(request):
        return HttpResponse('<b>This is next from class</b>')
    