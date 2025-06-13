from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
<<<<<<< HEAD
from .models import Students, fee, Attendance
=======
from .models import Students, fee
>>>>>>> bb4b90d81983599a451be09786355518a470b682
from datetime import datetime
from django.contrib import messages
from django.db import transaction
from django.db.models import Sum
from datetime import datetime
<<<<<<< HEAD
#from dateutil.relativedelta import relativedelta
from datetime import date
=======
from dateutil.relativedelta import relativedelta
>>>>>>> bb4b90d81983599a451be09786355518a470b682

# Create your views here.
def home(request):
    return render (request, 'home.html')

def addstudent(request):
    
    roll = random.randint(100000,999999)
    rollnumber = {'roll': roll}
    return render (request, 'student.html',rollnumber)
def submit(request):
    if request.method == "POST":
            rollnumber = request.POST['rollNumber']
            name = request.POST['studentName']
            gender = request.POST['gender']
            fname = request.POST['fatherName']
            mname = request.POST['motherName']
            dob = request.POST['dob']
            clss = request.POST['class']
            fee = request.POST['fee1']
            fee1 = float(fee)
            mlyfee = fee1/12
            mlyfee1= float("{:.2f}".format(mlyfee))
            mobile= request.POST['mobile']
            email = request.POST['email']
            TIME_ZONE = 'Asia/Kolkata'
            USE_TZ = True
            date = datetime.now().date()
            img = request.FILES['image']
            insert = Students(rollnumber=rollnumber,name=name, fname=fname, mname=mname, dob=dob, clss=clss, fee=fee1, yrlyfee=fee1,mobile=mobile,email=email,created_at=date, image=img,gender=gender,mlyfee=mlyfee1)
            insert.save()
<<<<<<< HEAD
            messages.success(request, "🎉 Success! Your data was Saved.")
=======
            messages.success(request, "🎉 Success! Your data was saved.")
>>>>>>> bb4b90d81983599a451be09786355518a470b682
            return redirect("/viewstudent/")
        
            
    else:
       return redirect("/") 

def viewstudent(request):
    viewdata = Students.objects.all()
    return render(request,'viewstudent.html',{'studentdata':viewdata})
def edit(resquest,id):
     editstudent = Students.objects.get(id=id)
     return  render(resquest,'studentedit.html',{'editstudent':editstudent})
def update(request,id):
            newrollnumber = request.POST['rollNumber']
            newname = request.POST['studentName']
            newfname = request.POST['fatherName']
            newmname = request.POST['motherName']
            newdob = request.POST['dob']
            newclss = request.POST['class']
            newmobile= request.POST['mobile']
            newemail = request.POST['email']
            update = Students.objects.get(id=id)
            update.rollnumber = newrollnumber
            update.name = newname
            update.fname = newfname
            update.mname = newmname
<<<<<<< HEAD
            update.dob = newdob
=======
            update.dob = newdob;
>>>>>>> bb4b90d81983599a451be09786355518a470b682
            update.clss = newclss
            update.mobile = newmobile
            update.email = newemail
            update.save()
            messages.success(request, "🎉 Success! Your data was Updated.")
            return redirect("/viewstudent/")      
def delete(request,id):
        deletedata = Students.objects.get(id=id)
        deletedata.delete()
        messages.error(request, " Delete! Your data was Deleted.")
        return redirect("/viewstudent/")
   
def feedeposit(request):
    studata = Students.objects.all()
    return  render(request,'feedeposit.html',{'studata':studata})

def feesubmit(request):
    
    try:
        with transaction.atomic():
            rollnumber = request.POST['rollnumber']
            name = request.POST['name']
            amount =int(request.POST['amount'])
            # Get the customer
            customer = Students.objects.get(rollnumber=rollnumber)

            # Check if customer has enough balance
            if amount>customer.fee:
                 messages.error(request, " Invalid! Amount is Grater than Dues Amount.")
                 return redirect("/feedeposit/") 
                #raise ValueError("Invalid Amount")

            # Create a new order
            order = fee.objects.create(
                rollnumber=rollnumber,
                name=name,
                deposit=amount            )

            # Update customer's balance
            customer.fee -= amount
            customer.save()
            messages.success(request, "🎉 Success! Your fee has been deposited.")
            return redirect("/feedeposit/") 

    except Students.DoesNotExist:
        messages.error(request, " Invalid! Roll Number Not Found.")
        return redirect("/statement1/")
    except Exception as e:
        print("Error:", e)

def alldeposits(request):
      depositdata = fee.objects.all()
      return  render (request,'alldeposit.html',{'deposit':depositdata})

def printreceipt(request,id):
      printdata = fee.objects.get(id=id)
      return render (request,'receipt.html',{'printdata':printdata})

def statement(request):
     return render(request,'statement.html')

def statement1(request):
    rollnumber = request.POST['rollnumber']
    try:
        stmt = fee.objects.filter(rollnumber=rollnumber)
        return render(request, 'statement1.html', {'stmt': stmt})
    except fee.DoesNotExist:
        messages.error(request, " Invalid! Roll Number Not Found.")
        return redirect("/statement/")

def registration(request,id):
    registration = Students.objects.get(id=id)

<<<<<<< HEAD
    return render (request,'registration.html',{'registration':registration})
def attendance(request):
    studata = Students.objects.all()
    return render(request, 'attendance.html', {'studata': studata})

def mark_attendance(request):
    students = Students.objects.all()
    if request.method == 'POST':
        already_marked = []
        for student in students:
            status = request.POST.get(str(student.id))
            # Check if attendance already exists for this student and date
            if not Attendance.objects.filter(student=student, date=date.today()).exists():
                Attendance.objects.create(
                    student=student,
                    date=date.today(),
                    status=status
                )
                messages.success(request, "Attendance marked successfully!")
                return redirect('/attendance/')
            else:
                already_marked.append(student.rollnumber)
        if already_marked:
            messages.warning(request, f"Attendance already marked for roll numbers: {', '.join(map(str, already_marked))}.")
        
    else:
        messages.error(request, "Invalid Credintials! Please try again.")
        return redirect('/attendance/')
def view_all_attendance(request):
    # Order by date descending and student's rollnumber
    attendance_records = Attendance.objects.select_related('student').order_by('-date', 'student__rollnumber')
    return render(request, 'all_attendance.html', {
        'attendance_records': attendance_records
    })
=======
    return render (request,'registration.html',{'registration':registration})
>>>>>>> bb4b90d81983599a451be09786355518a470b682
