from django.contrib import admin
from .models import ExamsType, ExamSolicitation, ExamRequests

admin.site.register(ExamsType)
admin.site.register(ExamSolicitation)
admin.site.register(ExamRequests)


