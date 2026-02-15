from django.db import models
import uuid

class ReciepeData(models.Model):
    reciepe_id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    reciepe_name = models.CharField(max_length=150)
    reciepe_description = models.TextField()
    rating = models.PositiveIntegerField()
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.reciepe_name