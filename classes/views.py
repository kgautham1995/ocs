from django.contrib import messages
from django.shortcuts import render,redirect

from classes.models import CourseModel, StudentModel


def showIndex(request):
    return render(request,"index.html")


def admin_login(request):
    return render(request,"admin_login.html")


def login_check(request):
    un = request.POST.get('t1')
    ps = request.POST.get('t2')
    if un == 'George' and  ps == 'George':
        return render(request,"admin.html",{'message':"Welcome Admin"})
    else:
        return render(request,"admin_login.html",{'messages':'Invalid credentials'})


def admin_logout(request):
    return render(request,"index.html")


def schedule_course(request):
    return render(request,"schedule_course.html")


def save_course(request):
    cna = request.POST.get('s1')
    cfa = request.POST.get('s2')
    cda = request.POST.get('s3')
    cti = request.POST.get('s4')
    cfe = request.POST.get('s5')
    cdu = request.POST.get('s6')

    CourseModel(cname=cna,cfaculty=cfa,cdate=cda,ctime=cti,cfee=cfe,cduration=cdu).save()
    return render(request,"admin.html",{"message":"Data saved Sucessfully"})


def view_course(request):
    res = CourseModel.objects.all()
    return render(request,"view_course.html",{'data':res})


def update_course(request):
    id = request.POST.get('no')
    res = CourseModel.objects.get(cid=id)
    return render(request,"update_course.html",{'data':res})


def update(request):
    id = request.POST.get('t1')
    na = request.POST.get('t2')
    fna = request.POST.get('t3')
    da = request.POST.get('t4')
    ti = request.POST.get('t5')
    fee = request.POST.get('t6')
    dur = request.POST.get('t7')
    CourseModel.objects.filter(cid=id).update(cname=na,cfaculty=fna,cdate=da,ctime=ti,cfee=fee,cduration=dur)
    return redirect("view_course")


def delete_record(request):
    id = request.GET.get('no')
    CourseModel.objects.get(cid=id).delete()
    return redirect("view_course")


def view_online_course(request):
    res = CourseModel.objects.all()
    return render(request,"view_online_course.html",{'data':res})


def stu_login(request):
    return render(request,"stu_log.html")


def save_student(request):
    na = request.POST.get('n1')
    cno = request.POST.get('n2')
    em = request.POST.get('n3')
    pa = request.POST.get('n4')
    co = request.POST.get('n5')
    st = StudentModel(name=na,contact_no=cno,email=em,password=pa)
    st.save()
    st.courses.set(co)
    messages.success(request,'Data Saved')
    return redirect('save_student')


def stu_reg(request):
    return render(request,"stu_reg.html")


def student_login(request):
    ema=request.post.get('e1')
    pw=request.post.get('e2')
    if ema in StudentModel.email:
        if pw in StudentModel.password:
            return redirect(request,"student_home.html")
    else:
        messages.success(request, 'Invalid Login Credentials')
        return redirect(request, "stu_login.html")