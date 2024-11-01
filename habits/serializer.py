from rest_framework.serializers import ModelSerializer

from habits.models import Habit, Place, Reward


class PlaceSerializer(ModelSerializer):

    class Meta:
        model = Place
        fields = "__all__"


class RewardSerializer(ModelSerializer):

    class Meta:
        model = Reward
        fields = "__all__"


class HabitSerializer(ModelSerializer):

    place = PlaceSerializer()
    reward = RewardSerializer()

    class Meta:
        model = Habit
        fields = "__all__"

