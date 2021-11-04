from django.http.response import HttpResponseRedirect
from django.shortcuts import render , HttpResponse
from .forms import StudentRegistration
from .models import user



#add and show
def add_show(request):


    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
    else:

        fm=StudentRegistration()
    stud=user.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm ,
    'stu':stud})



#update


def update_data(request,id):
    if request.method=='POST':
     pi=user.objects.get(pk=id)
     fm=StudentRegistration(request.POST,instance=pi)
     if fm.is_valid():
         fm.save()
    else:
        pi=user.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)

    return render(request,'enroll/updatestudent.html',{'form':fm})

#delete


def delete_data(request,id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


# Create your views here.
