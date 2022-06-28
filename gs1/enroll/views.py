from django.views.generic import ListView
from django.http import HttpResponse, JsonResponse

from urllib import response
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from requests import request
from django.core.files.storage import FileSystemStorage 
from .models import Signup, img_table, multi_file, qur
from django.core.paginator import Paginator
# Create your views here.
from .models import Employee
from .serializers import EmployeeSerializer
from enroll import serializers
from enroll.forms import StudentForm
def show_details(request):
    return render(request,'enroll/home.html')


def profile(request):
    return render(request,'enroll/profile.html')    

def sign(request):
    if(request.method=="POST"):
        un=request.POST.get('txtUserName','')
        pwd=request.POST.get('txtPassword','')
        em=request.POST.get('txtEmail','')
        dob=request.POST.get('txtDOB','')
        rec=Signup(username=un,password=pwd,email=em,dob=dob)
        rec.save()
        return redirect('signin')
    return render(request,'enroll/home.html')

def signin(request):
    response=render(request,'enroll/signin.html')
    if request.method == "POST":
        un=request.POST['txtUserName']
        pwd=request.POST['txtPassword']
        try:
            d1=Signup.objects.get(username=un,password=pwd)
        except Signup.DoesNotExist:
            return render(request,'enroll/signin.html')
        else:  
            request.session['uid'] = d1.id
            return redirect("profile")
    else:
        return render(request,'enroll/signin.html')

  

def users(request):
    if(request.session.get('uid')):
        allusers=Signup.objects.all()
        return render(request, 'enroll/users.html',{'allusers':allusers})
    else:
       return redirect('signin')

def logout(request):
    return redirect("detail")


def contact(request):
    #uiid=request.session['uid']
    if request.method =='POST':
       data1=request.POST.get('nm','')    
       data2=request.POST.get('em','')  
       data3=request.POST.get('sb','')  
       data4=request.POST.get('ms','')  
       song_obj = qur( username = data1, email=data2, subject = data3, message = data4)  
       song_obj.save()
       subject = data3
       message = data4
       email_from = data2
       recipient_list = ['chiragsaxena001@gmail.com']
       #send_mail(subject, message,email_from, recipient_list )
       send_mail(subject, message, email_from, recipient_list)
       return redirect("hm")
    return render(request,'enroll/contact.html',{})

def multi_docs(request):
        uiid=request.session['uid']
        if request.method=='POST':
            f1=request.FILES.get('file1',None)
            f2=request.FILES.get('file2',None)
            f3=request.FILES.get('file3',None)
            f4=request.FILES.get('file4',None)
            fs=FileSystemStorage()
            if f1==None:
                fi1=None
            else:
                fi1 = fs.save(f1.name, f1)
            if f2==None:
                fi2=None
            else:
                fi2 = fs.save(f2.name, f2)
            if f3==None:
                fi3=None
            else:
                fi3 = fs.save(f3.name, f3)
            if f4==None:
                fi4=None
            else:
                fi4 = fs.save(f4.name, f4)
            print(fi1,fi2,fi3,fi4)
            try:
                ss=multi_file.objects.get(userid=uiid)
                if fi1==None:
                    ss.file1=ss.file1
                else:
                    ss.file1=fi1
                if fi2==None:
                    ss.file2=ss.file2
                else:
                    ss.file2=fi2
                if fi3==None:
                    ss.file3=ss.file3
                else:
                    ss.file3=fi3
                if fi4==None:
                    ss.file4=ss.file4
                else:
                    ss.file4=fi4
                    
                ss.save()

            except multi_file.DoesNotExist:
                dd=multi_file(userid=uiid,file1=fi1,file2=fi2,file3=fi3,file4=fi4)
                dd.save()
        
            return redirect("pro")
        else:
            return render(request,'enroll/multi_docs_upload.html',{})
        return render(request,'enroll/multi_docs_upload.html',{})

def upload(request):
    if (request.method == 'POST'):

        f1 = request.FILES.get('f',None)
        
        fs = FileSystemStorage()
        if f1==None:
            file1=None
            # print(file1)
        else:
            file1 = fs.save(f1.name, f1)
            print(file1)
        data1=request.POST.get('nm','')
        data2=request.POST.get('em','')
        data3=request.POST.get('ps','')
        song_obj=img_table(username=data1,email=data2,password=data3,img=file1)
        song_obj.save()
        #-------------
        ss=img_table.objects.all()
        context={'all_data':ss}
        #----------
        return render(request, 'enroll/showimage.html',context)
    else:
        return render(request, 'enroll/uploadimage.html')
    return render(request, 'enroll/uploadimage.html') 

class ContactListView(ListView):
          paginate_by = 2
          model = qur
def paginate(request):
    contact_list = qur.objects.all()
    paginator = Paginator(contact_list, 2) # Show 2 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'enroll/user_list.html', {'page_obj': page_obj})   


def employeeListView(request):
    employees=Employee.objects.all()
    serializer=EmployeeSerializer(employees,many=True)
    return JsonResponse(serializer.data,safe=False)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		content = {'message': 'Hello, GeeksforGeeks'}
		return Response(content)


# def hello(request):
#         return HttpResponse("hello")     
# 

def index(request):  
    student = StudentForm()  
    return render(request,"enroll/form.html",{'form':student})   


    