from django.db import models
from django.conf import settings
# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , default=1,on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=180)
    timestamp = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return str(self.content)