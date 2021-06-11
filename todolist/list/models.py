from django.db import models


# Create your models here.
class List(models.Model):
    todo_List = models.CharField('todo_list', max_length=100)
    create_time = models.DateTimeField('create_time', auto_now_add=True)
    isDone = models.BooleanField('isDone', default=False)
    dead_Line = models.DateField('dead_Line', null=True)
