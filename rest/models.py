from django.db import models

# Create your models here.
class Color(models.Model):
    color_name=models.CharField(max_length=40)
    
    
    def __str__(self):
        return self.color_name
    
class Person(models.Model):
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=90)
    age=models.IntegerField()
    
    def __str__(self):
        return self.name
    
