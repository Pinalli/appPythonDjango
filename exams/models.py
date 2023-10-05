from django.db import models
from django.contrib.auth.models import User

class ExamsType(models.Model):
    CHOICES =(
        ('I', 'Exam of image'),
        ('B', 'Exam of blood')  
    )    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=CHOICES)
    price = models.FloatField()
    available = models.BooleanField(default=True)
    hour_init = models.IntegerField()
    hour_final = models.IntegerField()

    def __str__(self):
        return self.name
    

class ExamSolicitation(models.Model):
    CHOICE_STATUS = (
    ('W', 'Waiting'),
    ('U', 'Under review'),
    ('F', 'Finalized')
    ) 
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)#add null=True, blank=True for existing data in model
    exam = models.ForeignKey(ExamsType, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=2, choices=CHOICE_STATUS)
    result = models.FileField(upload_to="results", null=True, blank=True)    
    requires_password = models.BooleanField(default=False)
    password = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f'{self.user} | {self.exam.name}'
    

class ExamRequests(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    exams = models.ManyToManyField(ExamSolicitation)   
    scheduled = models.BooleanField(default=True)
    data = models.DateField()  

    def __str__(self):
        return f'{self.user} | {self.data}'