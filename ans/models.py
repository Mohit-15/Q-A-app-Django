from django.db import models

# Create your models here.

class Question(models.Model):
	ques_title = models.CharField(max_length= 50)
	ques_text = models.CharField(max_length= 200)
	posted_by = models.CharField(max_length= 20)

	def __str__(self):                                  # object name of Question Class
		return self.ques_title[:10]						# object name is the question title with 0 to 9th index

class Answer(models.Model):
	ans_title = models.CharField(max_length= 50)
	ans_text = models.CharField(max_length= 200)
	posted_by = models.CharField(max_length= 20)

	def __str__(self):                                  # object name of Answer Class
		return self.ans_title[:10]						# object name is the answer title with 0 to 9th index
