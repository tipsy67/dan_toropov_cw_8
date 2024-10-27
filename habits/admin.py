from django.contrib import admin

from habits.models import Habit, Place, Reward


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    pass


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    pass
