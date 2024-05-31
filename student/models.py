from django.db import models

# Create your models here.
class mysoftware(models.Model):
    software_tittle=models.CharField(max_length=100,null=True)
    software_description=models.TextField(null=True)
    software_picture=models.ImageField(upload_to='static/software/',null=True)
    software_date=models.DateField()



