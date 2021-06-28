import json

from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .models import Router

from .serializers import RouterDetailsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status

from django.contrib.auth.decorators import login_required

from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class RouterDetail(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        # Getting the data from the DB
        queryset = Router.objects.filter(status=False)
        print(({'router_data': queryset}))
        return Response({'router_data': queryset})

    def delete(self, request, *args, **kwargs):
        # Deleting based on ID of ROUTER
        data = Router.objects.get(id=kwargs['router_id'])
        data.status=True
        data.save()
        return Response({'message': 'Data has been deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class RouterData(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home/details.html'

    def get(self, request, *args, **kwargs):
        # Getting the data from the DB
        queryset = Router.objects.get(id=kwargs['router_id'])
        return Response({'data' : queryset})

    def put(self, request, *args, **kwargs):
        # Getting the data of specific ROUTER based on ID from the DB
        snippet = Router.objects.get(id=kwargs['router_id'])
        data = json.loads(request.body)
        serializer = RouterDetailsSerializer(snippet, data=data)
        # Saving to DB only if the data is correct(FULL)
        if serializer.is_valid():
            serializer.save()
            print('Record Saved')
            return Response({'message' : 'Record has been updated successfully'}, status=status.HTTP_200_OK)
        return Response({'message' : 'Record cannot be updated'})

class AddData(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home/add.html'

    def get(self, request):
        return Response({'message' : 'Add new data'})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        print(data)
        serializer = RouterDetailsSerializer(data=data)
        # Saving to DB only if the data is correct(FULL)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Record has been inserted successfully'}, status=status.HTTP_200_OK)
        return Response({'message' : 'Record cannot be added'})

@csrf_exempt
def add_many(request):
    if request.method == 'POST':
        response = {'status': '200',
                    'message': 'success',
                    'data': 'data received'}

        data = json.loads(request.body)
        print(data)
        for val in data.keys():
            data_value = data[val]
            obj = Router()
            obj.host_name = data_value['host_name']
            obj.sap_id = data_value['sap_id']
            obj.loopback_id = data_value['loopback_id']
            obj.ipv4 = data_value['ipv4']
            obj.mac_address = data_value['mac_address']
            obj.save()
        response = {'status': '200',
                    'message': 'success',
                    'data': 'data received'}
        return JsonResponse(response)
    else:
        return render(request, 'home/add_many.html')


@csrf_exempt
class LoginView(APIView):
    """Class based view loggin in user and returning Auth Token."""

    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        """Check if user exists, return token if it does."""
        data = JSONParser().parse(request)
        serializer_obj = LoginObjectSerializer(data=data)
        if serializer_obj.is_valid():
            user = authenticate(username=serializer_obj.data['username'], password=serializer_obj.data['password'])
            if not user:
                return Response({'error': 'Invalid Credentials'}, status=404)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=200)

        return JsonResponse(serializer_obj.errors, status=400)
