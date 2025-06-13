from django.db import models

# Create your models here.
class Students(models.Model):
    rollnumber = models.IntegerField()
    name =models.CharField(max_length=100)
    gender =models.CharField(max_length=25,null=True, blank=True)
    fname=models.CharField(max_length=100)
    mname=models.CharField(max_length=100)
    dob =models.DateField()
    clss =models.IntegerField()
    mobile=models.CharField(max_length=16,unique=True)
    email=models.CharField(max_length=100,unique=True)
    fee = models.FloatField()
    yrlyfee=models.FloatField(default=0.0,null=True, blank=True)
    mlyfee = models.FloatField(null=True, blank=True)
    image =models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "student"
class fee(models.Model):
    rollnumber = models.IntegerField()
    name =models.CharField(max_length=100)
    deposit = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "feedeposit"
class Attendance(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    class Meta:
        unique_together = ('student', 'date')
