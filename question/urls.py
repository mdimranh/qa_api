from django.urls import path

from .views import QuestionCreate, QuestionDetails, Questions

urlpatterns = [
    path("all", Questions.as_view()),
    path("add", QuestionCreate.as_view()),
    path("<int:id>", QuestionDetails.as_view())
]
