from rest_framework import serializers
from callcenter.models import CallLogs

class Callserializer(serializers.ModelSerializer):
    class Meta:
        model = CallLogs
        fields = ('call_time','caller_id','destination','status','ringing','talking','reason','totals')