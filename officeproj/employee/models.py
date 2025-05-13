from django.db import models

# Create your models here.
class department(models.Model):
    name=models.CharField(max_length=70)
    location=models.CharField(max_length=70)
    
    
    def __str__(self):
        return self.name
class role(models.Model):
    name=models.CharField(max_length=70)
    
    def __str__(self):
        return self.name
    
   
class employe(models.Model):
    f_name=models.CharField(max_length=70)
    l_name=models.CharField(max_length=70)
    dept=models.ForeignKey(department,on_delete=models.CASCADE)
    salary=models.IntegerField()
    bonous=models.IntegerField()
    role=models.ForeignKey(role,on_delete=models.CASCADE)
    phn_no=models.IntegerField()
    hire_date=models.DateField()
    
    def __str__(self):
        return "%s %s %s %s"%(self.f_name,self.l_name,self.dept,self.role)
    
    
