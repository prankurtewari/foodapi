from django.shortcuts import render
from django.http import JsonResponse


from .serializers import TaskSerializer

from .models import Task
# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def apiOverview(request):

	try:
		tasks = Task.objects.all().order_by('-id')
	except Task.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = TaskSerializer(tasks, many=True)
		return Response(serializer.data)



