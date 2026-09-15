from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import CustomUser
from accounts.serializers import RegisterSerializer


# Create your views here.
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request):
    #     users = CustomUser.objects.all()
    #     serializer = RegisterSerializer(users, many=True)
    #     return Response(serializer.data)

# class RegisterAPIView(generics.CreateAPIView):
#     serializer_class = RegisterSerializer
#     queryset = CustomUser.objects.all()
