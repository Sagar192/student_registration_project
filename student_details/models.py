from django.db import models
from django.utils import timezone


# Create your models here.
g_choice = (
    ("Male","Male"),
    ("Female","Female")
)
e_choices=(
    ("10th","10th"),
    ("12th","12th"),
    ("Polytechnic","Polytechnic"),
    ("B.Tech","B.tech"),
    ("B.Com","B.Com"),
    ("B.Sc","B.Sc")
)
c_choice = (
    ("Python","Python"),
    ("Java","Java"),
    ("DataScience","DataScience"),
    ("SAP","SAP")
)

c_status = (
    ("Ongoing","Ongoing"),
    ("Completed","Completed")

)

p_choices = (
    ("UPI","UPI"),
    ("Wired Transfer","Wired Transfer"),
    ("Cash","Cash")
)

t_choices = (
    ("Sanjit","Sanjit"),
    ("Salim","Salim")
)
class Students(models.Model):
    name = models.CharField(max_length=200,primary_key=True)
    contact_no = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    gender = models.CharField(choices=g_choice,max_length=50,default="Male")
    highest_education= models.CharField(choices=e_choices,max_length=50,default="10th")



    #to remove s
    class Meta:
        verbose_name_plural = 'Students'
    def __str__(self):
        return str(self.name)


class Admission(models.Model):
    student = models.OneToOneField(Students,on_delete=models.CASCADE)
    course_joined = models.CharField(choices=c_choice, max_length=50, default="--Select--")
    joining_date = models.DateField(default=timezone.now)
    completion_date = models.DateField(default=timezone.now)
    course_status = models.CharField(choices=c_status, max_length=20,default="Ongoing")
    course_fee = models.IntegerField()



    class Meta:
        verbose_name_plural = 'Admission'

    def __str__(self):
        return str(self.student)

class FeePaid(models.Model):
    admission = models.ForeignKey(Admission,on_delete=models.CASCADE)
    fee_paid = models.IntegerField()
    payment_mode = models.CharField(choices=p_choices,max_length=50,default="UPI")
    paid_to = models.CharField(choices=t_choices,max_length=50,default="Sanjit")
    fee_paid_date = models.DateField(default=timezone.now)


    class Meta:
        verbose_name_plural = 'FeePaid'

    def __str__(self):
        return str(self.admission)