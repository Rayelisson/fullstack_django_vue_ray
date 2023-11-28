import uuid

from accounts.models import User
from django.db import models


class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_attachments')
    created_by = models.ForeignKey(
        User, related_name='post_attachments', on_delete=models.CASCADE)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)

    attachments = models.ManyToManyField(PostAttachment, blank=True)

    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)