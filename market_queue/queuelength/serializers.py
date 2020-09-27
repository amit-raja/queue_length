from rest_framework import serializers
from queuelength.models import queue_info


class queue_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = queue_info
        fields = '__all__'