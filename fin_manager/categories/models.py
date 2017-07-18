from datetime import datetime

from django.db import models

from fin_manager.users.models import User


class Category(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name='categories')
    description = models.TextField()

    def __str__(self):
        return '%s' % self.title


class Entry(models.Model):
    category = models.ForeignKey(Category, related_name='entries')
    date = models.DateField(default=datetime.now)
    amount = models.FloatField()


