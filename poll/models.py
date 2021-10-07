from django.db import models
from django.conf import settings
import datetime
from django.utils import timezone

class IdIp(models.Model):
	userId_id = models.AutoField(primary_key=True)
	IP = models.CharField(max_length=4096)

	def __str__(self):
		return str(self.userId_id)

class Question(models.Model):
	title = models.CharField(max_length=4096)
	pub_date = models.DateTimeField(auto_now_add=True)
	end_date = models.DateTimeField()
	active = models.BooleanField(default=True, editable = False)

	def save(self, *args, **kw):
		if self.end_date < timezone.now():
			self.active = False
			super(Question, self).save(*args, **kw)
		else:
			self.active = True
			super(Question, self).save(*args, **kw)

	def __str__(self):
		return self.title


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
	title = models.CharField(max_length=4096, default ='text')
	lock_other = models.BooleanField(default=False)
	on_text = models.BooleanField(default=False)

	def __str__(self):
		return self.title

class Answer(models.Model):
	userId = models.ForeignKey(IdIp, on_delete=models.DO_NOTHING)
	question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
	choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.choice.title

