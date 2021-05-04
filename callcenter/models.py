from django.db import models

class CallLogs(models.Model):
    call_time = models.CharField(max_length=30)
    caller_id = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    ringing = models.CharField(max_length=15)
    talking = models.CharField(max_length=15)
    reason = models.CharField(max_length=200)
    totals = models.URLField(max_length=200)

    def __str__(self):
        return self.call_time