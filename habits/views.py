from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from habits.models import Habit
from habits.serializer import HabitSerializer


class PublishHabitsListAPIView(ListAPIView):
    queryset = Habit.objects.filter(is_published=True)
    serializer_class = HabitSerializer
    permission_classes = (AllowAny,)


class HabitsListAPIView(ListAPIView):
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)

class HabitsEditAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


