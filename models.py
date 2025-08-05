from django.db import models

# Create your models here.
class Login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    password=models.TextField()
    Usertype=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_login'

class Batch(models.Model):
    b_id=models.AutoField(primary_key=True)
    batch=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_batch'

class Department(models.Model):
    d_id=models.AutoField(primary_key=True)
    department=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_department'

class Course(models.Model):
    c_id=models.AutoField(primary_key=True)
    course=models.CharField(max_length=50)
    d=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table='tbl_course'

class Student_register(models.Model):
    sr_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    contact_number=models.BigIntegerField()
    email=models.CharField(max_length=50)
    address=models.TextField()
    image = models.TextField(null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE, null=True)
    login=models.ForeignKey(Login, on_delete=models.CASCADE, null=True)
    batch=models.ForeignKey(Batch, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table='tbl_student_register'

class Position(models.Model):
    p_id=models.AutoField(primary_key=True)
    position = models.CharField(max_length=255)
    class Meta:
        db_table='tbl_position'

class Notification(models.Model):
    nt_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=50,null=True)
    notification_date=models.DateField(null=True)
    last_nomination_date=models.DateField(null=True)
    polling_date=models.DateField(null=True)
    counting_date=models.DateField(null=True,)
    status=models.CharField(max_length=50,null=True)
    election_year=models.CharField(max_length=50,null=True)
    position=models.ForeignKey(Position,on_delete=models.CASCADE,null=True)   
    class Meta:
        db_table='tbl_notification'

class Nomination(models.Model):
    n_id=models.AutoField(primary_key=True)
    status=models.CharField(max_length=50)
    notification=models.ForeignKey(Notification, on_delete=models.CASCADE, null=True)
    student=models.ForeignKey(Student_register, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table='tbl_nomination'

class Polling(models.Model):
    p_id=models.AutoField(primary_key=True)
    candidate=models.ForeignKey(Nomination,on_delete=models.CASCADE, null=True)
    notification=models.ForeignKey(Notification,on_delete=models.CASCADE, null=True)
    student=models.ForeignKey(Student_register,on_delete=models.CASCADE, null=True)
    class Meta:
        db_table='tbl_polling'



