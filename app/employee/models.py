from django.db import models

class Employee(models.Model):

    MALE = 'MALE'
    FEMALE = 'FEMALE'

    GENDER_CHOICES = [
        (MALE,'Male'),(FEMALE,'Female'),
    ]

    employee_id  = models.IntegerField(max_length=10, unique=True)
    employee_name = models.CharField(max_length=100)
    employee_mobile = models.CharField(max_length=16)
    employee_email = models.EmailField(max_length=100, null=True, blank=True)
    salary = models.PositiveIntegerField(max_length=6, default=0)
    Date_Of_Birth = models.DateField()
    image_file = models.ImageField(upload_to='employee/images')
    cv_file = models.FileField(upload_to='employee/docs')
    joining_date = models.DateField()
    employee_hight = models.DecimalField(max_digits=3,decimal_places=1)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    is_positive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)
    update_at = models.DateTimeField(auto_now_add=False, auto_now=True,editable=False)

    def __str__(self) -> str:
        return self.employee_name + " " + self.employee_mobile

