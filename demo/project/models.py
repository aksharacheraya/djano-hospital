from django.db import models

GENDER = [
    ("Male","Male"),
    ("Female","Female")
]

class Student(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField()
    gender=models.CharField(max_length=10,choices=GENDER)
    phone=models.CharField(max_length=12)
    def __str__(self):
        return self.name
class Mark(models.Model):
    name=models.ForeignKey(Student, on_delete=models.CASCADE)
    eng=models.IntegerField()
    mal=models.IntegerField()
    maths=models.IntegerField()
    def __str__(self):
        return str(self.name)
class Fees(models.Model):
    name=models.ForeignKey(Student,on_delete=models.CASCADE)
    fees=models.IntegerField()
    date=models.DateField()
    def __str__(self):
        return str(self.name)