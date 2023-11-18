from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    division = models.TextField(max_length=200)
    wins = models.PositiveSmallIntegerField()
    losses = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
    
class Player(models.Model):
    team = models.ForeignKey(Team, on_delete = models.CASCADE,related_name = 'players')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    ir_list = models.BooleanField(default=False)

    def __str__(self):
        return self.name