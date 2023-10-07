from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import ExamsType,  ExamRequests, ExamSolicitation
from datetime import datetime


@login_required
def request_exams(request):
    #return HttpResponse('Here is where you can request exams.')
    types_exams = ExamsType.objects.all()   
    if request.method == 'GET':      
          return render(request,'request_exams.html', {'types_exams': types_exams})
    elif request.method == 'POST':
        exams_id = request.POST.getlist('exams')
        solicitation_exams = ExamsType.objects.filter(id__in=exams_id)       
       
        price_total = 0
        for i in solicitation_exams:
            if i.available:            
                price_total += i.price

        return render(request,'request_exams.html', {'types_exams': types_exams, 
                                                     'solicitation_exams': solicitation_exams,
                                                       'price_total': price_total})
def close_order(request):
    exams_id = request.POST.getlist('exams')
    solicitation_exams = ExamsType.objects.filter(id__in=exams_id)

    examRequest =  ExamRequests(
        user = request.user,      
        data = datetime.now(),
    )
    examRequest.save()# save in the database

    for exam in solicitation_exams:
        examSolicitation = ExamSolicitation(
            user = request.user,
            exam = exam,
            status = 'W'           
        )
        examSolicitation.save()
        examRequest.exams.add(examSolicitation)
    examRequest.save()
    return HttpResponse('Here is where you can close your order.')