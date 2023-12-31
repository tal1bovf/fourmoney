from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView, ListAPIView, GenericAPIView
from rest_framework.permissions import (IsAuthenticated)
from rest_framework.response import (Response)
from rest_framework.views import (APIView)
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import (RefreshToken)

from user.models import Project
from user.serializers import AllProjectsModelSerializer, ProjectDetailModelSerializer, SendEmailSerializer, \
    UserSerializer, RegisterSerializer
from user.services import (register_service, reset_password_service, reset_password_confirm_service)
from user.tasks import send_email_customer


# Register API
class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = ()
    def post(self, request):
        response = register_service(request.data, request)
        if response['success']:
            return Response(status=201)
        return Response(response, status=405)


#  Reset Password API
class ResetPasswordAPIView(APIView):
    def post(self, request):
        responce = reset_password_service(request)
        if responce['success']:
            return Response({'message': 'sent'})
        return Response(responce, status=404)


# Reset Password Confirm API

class PasswordResetConfirmAPIView(APIView):

    def post(self, request, token, uuid):
        response = reset_password_confirm_service(request, token, uuid)
        if response['success']:
            return Response({'message': 'Password changed'})
        return Response(response, status=400)


# Logout API
class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        token = RefreshToken(request.user)
        token.blacklist()
        return Response(status=200)


class VerifyAccountAPIView(APIView):
    permission_classes = ()

    def get(self, request, uid, token):
        pk = int(urlsafe_base64_decode(uid))
        print(pk)
        user = User.objects.get(pk=pk)
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()

        return Response({
            'success': True,
            'message': 'Successfully active'
        })


class AllProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = AllProjectsModelSerializer


class ProjectDetailRetrieveAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailModelSerializer


class ProjectSearchListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'title', 'title', 'keyword', 'keyword', 'keyword']


class SendMailAPIView(GenericAPIView):
    serializer_class = SendEmailSerializer
    permission_classes = ()
    # @swagger_auto_schema(query_serializer=SendEmailSerializer, request_body=4)
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            email = serializer.validated_data.get('email')
            message = serializer.validated_data.get('message')
            name = serializer.validated_data.get('name')
            phone = serializer.validated_data.get('phone')

            my_email = ''

            send_email_customer.delay(email, message, name, phone)
        except Exception as e:
            return Response({'success': False, 'message': str(e)})

        return Response({'success': True, 'message': 'Email sent!'})