from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queuelength.models import queue_info
from queuelength.serializers import queue_infoSerializer


@api_view(['GET', 'POST'])
def queue_list(request):
   
    if request.method == 'GET':
        queue_size = queue_info.objects.all()
        serializer = queue_infoSerializer(queue_size, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = queue_infoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)