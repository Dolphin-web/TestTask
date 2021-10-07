from .serializers import QuestionSerializer, AnswerSerializer, IdSerializer, ChoicesSerializer
from django.views.generic import ListView, CreateView, UpdateView
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question, IdIp, Answer, Choice
from datetime import datetime

class GetQuestion(APIView):
	def get(self, request, format=None):
		questions = Question.objects.filter(active = True)
		serializer = QuestionSerializer(questions, many=True)
		return Response({'Questions' : serializer.data})

class GetAnswers(APIView):
	def get(self, request, format=None):
		answers = Answer.objects.all()
		serializer = AnswerSerializer(answers, many=True)
		return Response({'Answers' : serializer.data})


class PostAnswers(GenericAPIView):
	serializer_class = AnswerSerializer
	def get(self, request, QuestionsId, UserId):
		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')

		userId = IdIp.objects.get(userId_id = UserId)
		if userId.IP == ip:
			question = Question.objects.get(id = QuestionsId)
			choice = Choice.objects.get(id = ChoiceId)
			answer = Answer(userId = userId, question = question, choice = choice,)
			answer.save()
			serializer = AnswerSerializer(answer)
			return Response({'Answers':serializer.data})
		else: 
			return Response('Ваш ip адресс не совпадает с IP владельца')

class GetAnswerOnID(APIView):
	def get(self, request, userId):
		foundAnswers = []
		answers = Answer.objects.filter(userId = userId)
		serializer = AnswerSerializer(answers, many=True)
		return Response({'Answers': serializer.data})

class GetChoices(APIView):
	def get(self, request, questionsId):
		Choices = Choice.objects.filter(question_id = questionsId)
		serializer = ChoicesSerializer(Choices, many=True)
		return Response({'Choices': serializer.data})

class GetId(APIView):
	def get(self, request, format=None):
		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')
		
		try:
			IdIp.objects.get(IP = ip)
		except:
			idip = IdIp(IP = ip)
			idip.save()
		
		Id = IdIp.objects.get(IP = ip)
		serializer = IdSerializer(Id, many=False)
		return Response({'Id': serializer.data})
