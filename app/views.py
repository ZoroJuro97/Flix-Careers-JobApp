from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from app.models import JobPost
# from django.template import loader

# Create your views here.

job_list = ['First Job', 'Second Job', 'Third Job']
job_desc = ['First job desc', 'Second job desc', 'Third job desc']

class TempClass:
    x=5

def hello(request):
    is_auth = True
    temp = TempClass()
    #template = loader.get_template('app/hello.html')
    list = ["alpha", "beta"]
    context = {"name":"Abhi", "age":25, "first_list":list, "temp_object":temp, "is_auth":is_auth}
    #return HttpResponse(template.render(context, request))
    return render(request, "app/hello.html", context)

def job(request):
    jobs = JobPost.objects.all()
    context = {"jobs" : jobs}
    return render(request, "app/index.html", context)

def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        job = JobPost.objects.get(id=id)
        context = {"job" : job}
        return render(request, "app/job_detail.html", context)
    except:    
        return HttpResponse("Not found")