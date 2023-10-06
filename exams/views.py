from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def request_exams(request):
    #return HttpResponse('Here is where you can request exams.')
    if request.method == 'GET':
        return render(request,'request_exams.html')
