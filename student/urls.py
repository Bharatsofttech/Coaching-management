from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('submit/', views.submit, name='submit'),
    path('viewstudent/',views.viewstudent, name="viewstudent"),
    path('edit/<int:id>', views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('feedeposit/',views.feedeposit,name="feedeposit"),
    path('feesubmit/',views.feesubmit,name="feesubmit"),
    path('alldeposits/',views.alldeposits,name="alldeposits"),
    path('printreceipt/<int:id>',views.printreceipt,name="printreceipt"),
    path('statement/',views.statement,name="statement"),
    path('statement1/',views.statement1,name="statement1"),
    path('registration/<int:id>',views.registration,name="registration"),
]