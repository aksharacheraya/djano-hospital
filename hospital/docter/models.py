from django.db import models

class Department(models.Model):
    dep_name=models.CharField(max_length=20)
    dep_desc=models.TextField(max_length=100)
    def __str__(self):
        return self.dep_name
class Doctor(models.Model):
    doc_name=models.CharField(max_length=20)
    doc_spec=models.TextField(max_length=50)
    
    doc_image = models.ImageField(upload_to='doctors/')
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.doc_name
class Booking(models.Model):
    p_name=models.CharField(max_length=100)
    p_email=models.EmailField()
    p_phone=models.CharField(max_length=100)
    doc_name=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Booking_date=models.DateField()
    booked_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.doc_name)