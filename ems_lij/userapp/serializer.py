from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from userapp.models import User, Employee


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'username': {
                'min_length': 2,
                'required': True
            },
        }

    def validate(self, attrs):
        password = attrs.get('password')
        if len(password) < 6:
            raise serializers.ValidationError('密码不正确或者密码长度不能小于6')
        return attrs

    def validate_username(self, value):
        user_obj = User.objects.filter(username=value)
        if user_obj:
            raise serializers.ValidationError('用户名重复')
        return value


class EmpModelSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('emp_name', "salary", "age", "full_img", "id", "img")
        extra_kwargs = {
            "full_img": {
                "read_only": True
            },
            "img": {
                "write_only": True
            }
        }
