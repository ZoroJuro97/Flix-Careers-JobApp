from django.urls import path
from app.views import job_detail, job, hello

urlpatterns = [
    path('job/<int:id>', job_detail, name='job_detail'),
    path('', job, name='jobs_home'),
    path('hello/', hello, name='hello'),
]