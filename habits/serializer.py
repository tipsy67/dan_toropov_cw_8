from rest_framework import serializers
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


class HabitListSerializer(ModelSerializer):
    place = PlaceSerializer(read_only=True)
    reward = RewardSerializer(read_only=True)
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Habit
        fields = "__all__"


class HabitSerializer(ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"

    def validate_periodicity(self, value):
        if value > 7 * 24:
            raise serializers.ValidationError(
                "Нельзя выполнять привычку реже, чем 1 раз в 7 дней"
            )
        return value

    def validate_time_to_complete(self, value):
        if value > 120:
            raise serializers.ValidationError(
                "Время выполнения должно быть не больше 120 секунд"
            )
        return value

    def check_field(self, value, field):
        result = None
        if value:
            result = self.initial_data.get(field)
            if result is None:
                if self.instance is not None:
                    result = getattr(self.instance, field)

        return result

    def check_is_nice_habit(self, value):
        if self.check_field(value, "is_nice_habit"):
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки"
            )

    def validate_is_nice_habit(self, value):
        if self.check_field(value, "linked_habit") or self.check_field(value, "reward"):
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки"
            )
        return value

    def validate_reward(self, value):
        self.check_is_nice_habit(value)
        if self.check_field(value, "linked_habit"):
            raise serializers.ValidationError(
                "Одновременный выбор связанной привычки и указания вознаграждения невозможен"
            )
        return value

    def validate_linked_habit(self, value):
        self.check_is_nice_habit(value)
        if self.check_field(value, "reward"):
            raise serializers.ValidationError(
                "Одновременный выбор связанной привычки и указания вознаграждения невозможен"
            )
        if not value.is_nice_habit:
            raise serializers.ValidationError(
                "В связанные привычки могут попадать только привычки с признаком приятной привычки"
            )
        return value
