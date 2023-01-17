from django.db import models

class Item(models.Model):
    item=models.CharField(max_length=100)
    image=models.CharField(max_length=200)
    price=models.IntegerField()
    discription=models.TextField(max_length=150)
    def __str__(self):
        return self.item




    

