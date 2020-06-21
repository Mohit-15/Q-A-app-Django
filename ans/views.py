from django.shortcuts import render,redirect
from .models import Question, Answer

# Create your views here.

def home(request):
		qwe = Question.objects.all()                     # getting all objects of Question Class and storing in qwe
		asd = Answer.objects.all()						 # getting all objects of Answer Class and storing in asd

		return render(request, 'home.html',{'ques': qwe, 'ans': asd})      # Passing the objects to the template in dictionary

def question(request):
	if request.method == 'POST':
		title = request.POST['title']							# getting values from template
		ques = request.POST['ques']
		posted_by = request.POST['posted_by']

		quest = Question(ques_title = title , ques_text = ques , posted_by = posted_by)   # creating object quest of Question Class 
		quest.save()																	  # and store the values and save it

		return redirect('/')															  # redirecting to home page
	else:
		return render(request, 'question.html')

def answer(request):
	if request.method == 'POST':
		title = request.POST['title']
		ans = request.POST['ans']
		posted_by = request.POST['posted_by']

		#if Answer.objects.filter(ans_title = title).exists():							# checking if title already exist in the db
			#azs = Answer.objects.filter(ans_title = title)								# getting object which have same title
			#azs = azs.update(ans_text = ans , posted_by = posted_by)					# updating the object with new values by keeping title as it is
			#return redirect('/')
		#else:
		anst = Answer(ans_title = title , ans_text = ans , posted_by = posted_by)   # creating a new object of Answer
		anst.save()

		return redirect('/')
	else:
		return render(request, 'answer.html')
