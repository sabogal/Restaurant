from rest_framework import serializers
from apps.user.models import User
from django.contrib.auth.models import Group


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['password', 'username', 'name', 'last_name' ,'document','number_phone']


    def validate_name(self, value):
        return value.lower()
        
    def validate_last_name(self, value):
        return value.lower()
    
    def validate_username(self, value):
        return value.lower()
    
    def to_representation(self, instance):
       
        return {
            'id': instance.id,
            'name': instance.name,
            'last_name': instance.last_name,
            'email': instance.username,
            'phone': instance.number_phone,
            'document': instance.document,
        }
    
    def create(self,validated_data):
       create_user = User(**validated_data)
       create_user.set_password(validated_data['password'])
       create_user.save()
       return create_user

    def update(self, instance, validated_data):
        updated_user = super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user
    
class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        # fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'last_name': instance.last_name,
            'username': instance.username,
            'phone': instance.number_phone,
            'document': instance.document,
            'groups': str(instance.groups.first())
        }
    
class ActivateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('token')
        
class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=50, min_length=6, write_only=True)
    re_password = serializers.CharField(max_length=50, min_length=6, write_only=True)

    def validate(self, data):
        if data['password'] != data['re_password']:
            raise serializers.ValidationError(
                {'password':'Debe ingresar ambas contraseñas iguales'}
            )
        return data

class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)

    