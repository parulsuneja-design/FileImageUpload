from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to="img/%y")
    document = models.FileField(null=True)

    def __str__(self):
        return self.name
