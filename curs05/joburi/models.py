from django.db import models


# Create your models here.

class Joburi(models.Model):
    type = models.IntegerField()
    # url = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.CharField(max_length=100)
    currency = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.title} -> {self.city}"

# class Log(models.Model):
#     action_choices = (('created', 'created'),
#                       ('updated', 'updated'),
#                       ('refresh', 'refresh'))
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
#     action = models.CharField(max_length=10, choices=action_choices)
#     url = models.CharField(max_length=100)
