from django.db import models
from django.utils import timezone
from account.models import User

# Create your models here.
class Message(models.Model):
    #보내는 사람
    sender = models.ForeignKey(User, related_name="message_sender", on_delete=models.CASCADE)
    #받는 사람
    recipient = models.ForeignKey(User, related_name="message_receiver", on_delete=models.CASCADE)
    #보낸 시간
    sentAt = models.DateTimeField(auto_now_add=True)
    #내용
    content = models.TextField(max_length=150)
    #읽었는지
    isRead = models.BooleanField(default=False)

    objects = models.Manager()

    def save(self, **kwargs):
        if not self.id:
            self.sentAt = timezone.now()
        super(Message, self).save(**kwargs)

    class Meta:
        ordering = ['-sentAt']

    def __str__(self):
        return self.content

    def summary(self):
        return self.content[:20]

class Remessage(models.Model):
    #메세지
    message = models.ForeignKey(Message, related_name="remessage", on_delete=models.CASCADE)
    #보내는 사람
    sender = models.ForeignKey(User, related_name="remessage_sender", on_delete=models.CASCADE)
    #받는 사람
    recipient = models.ForeignKey(User, related_name="remessage_receiver", on_delete=models.CASCADE)
    #보낸 시간
    sentAt = models.DateTimeField(auto_now_add=True)
    #내용
    content = models.TextField(max_length=150)
    #읽었는지
    isRead = models.BooleanField(default=False)

    objects = models.Manager()

    def save(self, **kwargs):
        if not self.id:
            self.sentAt = timezone.now()
        super(Message, self).save(**kwargs)

    class Meta:
        ordering = ['-sentAt']

    def __str__(self):
        return self.content

    def summary(self):
        return self.content[:20]