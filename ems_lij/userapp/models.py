from django.db import models

# Create your models here.
class User(models.Model):
    sex_choices=(
        (0,'male'),
        (1,'female')
    )
    username=models.CharField(max_length=128)
    password=models.CharField(max_length=64)
    re_name=models.CharField(max_length=64)
    sex=models.SmallIntegerField(choices=sex_choices,default=0)
    status=models.BooleanField(default=True)
    register_time=models.DateField(auto_now_add=True)


    class Meta:
        db_table='bz_user'
        verbose_name='用户表'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.username

class Employee(models.Model):
    emp_name=models.CharField(max_length=128)
    salary=models.DecimalField(max_digits=8,decimal_places=2)
    age=models.SmallIntegerField()
    img=models.ImageField(upload_to='img',default='img/1.jpg')

    @property
    def full_img(self):
        return "%s%s%s"%("http://127.0.0.1:8000/","media/",self.img)

    class Meta:
        db_table='bz_emp'
        verbose_name='员工表'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.emp_name


