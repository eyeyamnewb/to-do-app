from django.db import models

# Create your models here.

class Task(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	duedate = models.DateTimeField(default=13/10/2011)

	def __str__(self):
		return self.title
