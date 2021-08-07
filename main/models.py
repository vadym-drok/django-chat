from django.db import models

class Message(models.Model):
    """Model for create categories of Ads"""

    text = models.TextField()
    user = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    roomname = models.CharField(max_length=50)

    def __str__(self) -> str:
        return 'Message: %s' % self.text