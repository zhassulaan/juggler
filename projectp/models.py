from django.db import models

class Project(models.Model):
   projid = models.CharField(max_length=4)
   title = models.CharField(max_length=30)
   deadline = models.DateField()
   completed = models.BooleanField()

class Task(models.Model):
   projid = models.ForeignKey(Project, on_delete=models.CASCADE)
   name = models.CharField(max_length=20)
   description = models.CharField(max_length=80)
   done = models.BooleanField()