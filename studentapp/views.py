from django.shortcuts import render,redirect
from studentapp.models import Student
# Create your views here.
def add_student(request):
    return render(request,'add_student.html')

def add_student_details(request):
    if request.method=="POST":
        name=request.POST.get('student_name')
        address=request.POST.get('address')
        age=request.POST.get('age')
        email=request.POST.get('email')
        date=request.POST.get('date')
        qualification=request.POST.get('qualification')
        gender=request.POST.get('gender')
        mobile=request.POST.get('mobileno')
        student=Student(StudentName=name,Address=address,Age=age,Emailid=email,JoiningDate=date,Qualification=qualification,Gender=gender,Mobileno=mobile)
        student.save()
        return redirect('show_student')
    
def show_student(request):
    student=Student.objects.all()
    return render(request,'show_student.html',{'students':student})   

def show_student_details(request,pk):
    student=Student.objects.get(id=pk)
    return render(request,'show_student_details.html',{'students':student})

def edit_page(request,pk):
    student=Student.objects.get(id=pk)
    return render(request,'edit.html',{'students':student})

def edit_details(request,pk):
    if request.method=='POST':
        student=Student.objects.get(id=pk)
        student.StudentName=request.POST.get('sname')
        student.Address=request.POST.get('address')
        student.Age=request.POST.get('age')
        student.Emailid=request.POST.get('email')
        student.JoiningDate=request.POST.get('jdate')
        student.Qualification=request.POST.get('qualification')
        student.Gender=request.POST.get('gender')
        student.Mobileno=request.POST.get('mobileno')
        student.save()
        return redirect('show_student')
    return render(request,'edit.html')
def delete_page(request,pk):
    student=Student.objects.get(id=pk)
    student.delete()
    return redirect('show_student')
def addcourse(request):
    return render(request,'add_course.html')