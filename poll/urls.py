from django.urls import path
from .views import *

urlpatterns = [
    path('GetId', GetId.as_view()),
    path('GetQuestions/', GetQuestion.as_view()),

    path('GetAnswers', GetAnswers.as_view()),
    path('GetAnswersOnId/<int:userId>', GetAnswerOnID.as_view()),
    path('PostAnswers/<int:QuestionsId>/<int:ChoiceId>/<int:UserId>/', PostAnswers.as_view()),

    path('GetChoices/<int:questionsId>', GetChoices.as_view()),
]