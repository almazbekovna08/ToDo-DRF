from rest_framework import serializers

from apps.todo.models import User, Todo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'created_at', 'age')

    def validate(self, attrs):
        if '+996' not in attrs['phone_number']:
            raise serializers.ValidationError("Номер телефона должен быть в формате +996XXXXXXXXX")
        return attrs
    
    def create(self, values):
        user = User.objects.create(
            username=values['username'], phone_number=values['phone_number'],
            email=values['email'],
        )
        user.save()
        return user
    
class TodoSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'image', 'user']
        read_only_fields = ['created_at']