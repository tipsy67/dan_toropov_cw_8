from rest_framework import viewsets
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from habits.models import Habit, Place, Reward
from habits.paginators import HabitsPagination
from habits.serializer import (
    HabitListSerializer,
    HabitSerializer,
    PlaceSerializer,
    RewardSerializer,
)
from habits.src.celery_cmd import delete_task, start_task


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
        if getattr(self, "swagger_fake_view", False):
            return Habit.objects.none()
        return Habit.objects.filter(owner=self.request.user)


class HabitsEditAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    # queryset = Habit.objects.all()

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Habit.objects.none()
        return Habit.objects.filter(owner=self.request.user)

    def perform_destroy(self, instance):
        delete_task(instance)
        instance.delete()

    def perform_update(self, serializer):
        instance = serializer.save()
        start_task(instance)


class HabitsCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        instance = serializer.save(owner=self.request.user)
        start_task(instance)


class RewardsViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer


class PlacesViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
