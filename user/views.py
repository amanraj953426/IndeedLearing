from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def index(request):
    sdata=slider.objects.all().order_by('-id')
    nbdata=newbatches.objects.all().order_by('-id')
    mydict={"sd":sdata,"nbdata":nbdata}
    return render(request, 'user/index.html',mydict)

def about(request):
    return render(request, 'user/about.html')

def contact(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('mobile')
        c=request.POST.get('email')
        d=request.POST.get('msg')
        contactus(name=a,mobile=b,email=c,message=d).save()
        return (HttpResponse("<script>alert('Thanks for contacting us');location.href='/user/contact'</script>"))
    return render(request, 'user/contact.html')

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        x=signup.objects.filter(passwd=passwd,email=email).count()
        if x==1:
            request.session['user']=email
            y=signup.objects.filter(email=email,passwd=passwd)
            request.session['userpic']=str(y[0].profile)
            request.session['username']=str(y[0].name)
            request.session['batchid']=str(y[0].batchid)

            return HttpResponse("<script>location.href='/student/index'</script>")
        else:
            return HttpResponse("<script>alert('username or password is incorrecr..');location.href='/user/login'</script>")
    return render(request, 'user/login.html')

def signin(request):
    bdata=studentbatch.objects.all()
    md={"bdata":bdata}
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        passwd=request.POST.get('passwd')
        college=request.POST.get('college')
        course=request.POST.get('course')
        picture=request.FILES['fu']
        pyear=request.POST.get('pyear')
        batch=request.POST.get('batch')
        x=signup.objects.filter(email=email).count()
        if x==0:
            signup(name=name,email=email,mobile=mobile,college=college,course=course,pyear=pyear,profile=picture,passwd=passwd,status='Pending',batchid=batch).save()
            return HttpResponse("<script>alert('You are Registered successfully');location.href='/user/signin'</script>")
        else:
            return HttpResponse("<script>alert('You are already registered...');location.href='/user/signin'</script>")

    return render(request, 'user/registration.html',md)

def mynewbatches(request):
    batchdata=newbatches.objects.all().order_by('-id')
    md={"bdata":batchdata}
    return render(request, 'user/batches.html',md)

def facility(request):
    return render(request, 'user/facility.html')
def stories(request):
    clg = request.GET.get('college')
    year = request.GET.get('college')
    if clg is not None and year is not None:
        pdata = placement.objects.filter(college=clg, session=year)
    else:
        pdata = placement.objects.all()

    collegedata=college.objects.all().order_by('-id')
    sdata=session_year.objects.all().order_by('-id')


    md={"cdata":collegedata,"sdata":sdata,"pdata":pdata}
    return render(request, 'user/stories.html',md)

def feedback(request):
    return render(request, 'user/feedback.html')