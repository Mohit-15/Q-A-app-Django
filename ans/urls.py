from django.urls import path
from . import views                         	# access all methods of views.py

urlpatterns = [
	path('', views.home, name='home'),                            # url of first page and which function to call
	path('question' , views.question , name='question'),          # url of question page and which function to call from views
	path('answer' , views.answer , name= 'answer'),               # url of answer page and function call
]
