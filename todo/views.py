from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Task
from .serializers import TaskSerializer
from rest_framework.exceptions import NotAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def findAll(request):
    items = Task.objects.all()
    serializer = TaskSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createTask(request):
    user = request.user

    if not user:
        raise NotAuthenticated

    data = request.data
    data['user'] = user.id
    
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        try:
            serializer.save()
            
            return Response(serializer.data)
        except:
            return Response({"error": "Failed to create the task. Check your data."}, status=400)

    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def findTaskById(request, id):
    userId = request.user.id
    
    task = Task.findOne(id=id, user=userId)
    serializer = TaskSerializer(task)

    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateTask(request, id):
    userId = request.user.id
    data = request.data
    
    try:
        task = Task.findOne(id=id, user=userId)
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.is_completed = data.get('is_completed', task.is_completed)
        task.save()

        serializer = TaskSerializer(task)
        return Response(serializer.data)
    except:
        return Response({"error": "Failed to upadate the task. Check your data."}, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteTask(request, id):
    userId = request.user.id

    try:
        print('test')
        task = Task.findOne(id=id, user=userId)

        print('test22')

        task.delete()

        return Response({"message": "Your task deleted succuesfully."}, status=200)
    except:
        return Response({"error": "Failed to delete the task."}, status=400)