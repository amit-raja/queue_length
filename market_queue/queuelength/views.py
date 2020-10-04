from rest_framework import status
from datetime import datetime, timezone, timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queuelength.models import queue_info
from queuelength.serializers import queue_infoSerializer
import time


@api_view(['GET', 'POST'])
def queue_list(request):
    queue_size= queue_info
    queue_size = queue_info.objects.all().last()
    if request.method == 'GET':
        queue_size = queue_info.objects.all().last()
        #queue_length=request.data['queue_size']
        #print(queue_size)
        serializer = queue_infoSerializer(queue_size)
        return Response(serializer.data)

    elif request.method == 'POST':
        #finding last entry of row
        #print(queue_size.queue_length)
        new_queue_length=request.data
        #print(lastupdated_queue)
        time_now=datetime.now(timezone.utc)
        last_updated_time=queue_size.updated_time
        time_threshold = last_updated_time + timedelta(minutes=5)
        
        #print(queue_size.updated_time)
        
          if(new_queue_length < (queue_size.queue_length)-50 and time_now > time_threshold):
              return JsonResponse({"Invalid" : "queue_length"})
          else:
                  serializer = queue_infoSerializer(data=request.data)
                  if serializer.is_valid():
                  serializer.save()
                   return Response(serializer.data, status=status.HTTP_201_CREATED)
                   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
               
