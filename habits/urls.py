from django.urls import path, include

from habits.apps import HabitsConfig
from habits.views import PublishHabitsListAPIView, HabitsListAPIView, HabitsEditAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('', PublishHabitsListAPIView.as_view(), name='published_habits'),
    path('my_habits/', HabitsListAPIView.as_view(), name='my_habits'),
    path('my_habits/<int:pk>/', HabitsEditAPIView.as_view(), name='my_habits_edit'),

]