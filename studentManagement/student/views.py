from django.shortcuts import render
from .form import *
from .models import *

# Create your views here.
def upload(request):
    if request.method == "POST":
        form=StudentForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            upload=form.instance
            return render(request, "upload.html",{"upload":upload})
    else:
        form =StudentForm()
    student=Student.objects.all()
    context={
        "form":form,
        "student":student
    }
    return render(request,"upload.html",context)