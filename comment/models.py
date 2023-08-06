from django.db import models

class Comment(models.Model):
    desc = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
