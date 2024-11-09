from django.urls import path, include
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import (
    PublishHabitsListAPIView,
    HabitsListAPIView,
    HabitsEditAPIView,
    HabitsCreateAPIView,
    RewardsViewSet,
)

app_name = HabitsConfig.name

router_rewards = DefaultRouter()
router_rewards.register(r"rewards", RewardsViewSet, basename="Reward")

router_places = DefaultRouter()
router_places.register(r"places", RewardsViewSet, basename="Place")

urlpatterns = [
    path("", PublishHabitsListAPIView.as_view(), name="published-habits"),
    path("my_habits/", HabitsListAPIView.as_view(), name="my-habits"),
    path("my_habits/<int:pk>/", HabitsEditAPIView.as_view(), name="my-habits-edit"),
    path("my_habits/create/", HabitsCreateAPIView.as_view(), name="my-habits-create"),
] + router_rewards.urls + router_places.urls
