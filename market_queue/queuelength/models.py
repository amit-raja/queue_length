from django.db import models

# Create your models here.


class queue_info(models.Model):
	queue_length=models.IntegerField()
	updated_time=models.DateTimeField( auto_now_add=True)