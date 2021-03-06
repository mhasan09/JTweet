from django.db import models
from django.conf import settings
from .validators import validate_content
from django.urls import reverse

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , default=1,on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=180,validators=[validate_content])
    timestamp = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweetapp:detail" , kwargs={"pk":self.pk})
108