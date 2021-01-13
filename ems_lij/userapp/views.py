
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from userapp.models import User, Employee
from userapp.serializer import UserModelSerializer, EmpModelSerializer
from rest_framework.generics import  GenericAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, ListModelMixin, CreateModelMixin, \
    DestroyModelMixin


class UserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        serializer = UserModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        save = serializer.save()
        return Response({
            'result': UserModelSerializer(save).data,
        }, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        pwd = request.GET.get('password')
        rst = User.objects.filter(username=username, password=pwd).first()
        print(rst)
        if rst:
            data = UserModelSerializer(rst).data
            return Response({
                'result': data,
                'message': True
            }, status=status.HTTP_200_OK)
        return Response({
            'result': "登录参数有误",
            'message': False
        }, status=status.HTTP_400_BAD_REQUEST)


class EmpAPIView(UpdateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 CreateModelMixin,
                 GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpModelSerializer

    def get(self, request, *args, **kwargs):
        print(request)
        if "pk" in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
