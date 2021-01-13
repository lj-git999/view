from django.urls import path

from userapp import views

urlpatterns=[
    path('users/',views.UserAPIView.as_view()),
    path('emps/',views.EmpAPIView.as_view()),
    path('emps/<str:pk>/',views.EmpAPIView.as_view()),
]