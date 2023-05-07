from django.contrib import admin

from app.models import JobPost, Author, Location, Skills

# Register your models here.
admin.site.register(JobPost)
admin.site.register(Author)
admin.site.register(Location)
admin.site.register(Skills)