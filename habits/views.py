from unittest.mock import patch

from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from habits.models import Habit, Reward, Place
from habits.paginators import HabitsPagination

from habits.serializer import HabitSerializer, RewardSerializer, HabitListSerializer, PlaceSerializer


class PublishHabitsListAPIView(ListAPIView):
    queryset = Habit.objects.filter(is_published=True)
    serializer_class = HabitListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = HabitsPagination


class HabitsListAPIView(ListAPIView):
    serializer_class = HabitListSerializer
    pagination_class = HabitsPagination
    # queryset = Habit.objects.all()

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Habit.objects.none()
        return Habit.objects.filter(owner=self.request.user)

class HabitsEditAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    # queryset = Habit.objects.all()

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Habit.objects.none()
        return Habit.objects.filter(owner=self.request.user)


class HabitsCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        # reward_pk = self.request.data.get("reward")
        # if reward_pk is not None:
        #     reward = Reward.objects.filter(pk=reward_pk).first()

        serializer.save(owner=self.request.user)


class RewardsViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer

class PlacesViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
