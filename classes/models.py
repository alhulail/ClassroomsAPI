from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	teacher = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})
