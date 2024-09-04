from django.db import models


class Player(models.Model):
    username = models.CharField(max_length=100, unique=True)
    first_login = models.DateTimeField(auto_now_add=True)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username


class Boost(models.Model):
    boosts = [
        ('speed', 'Speed Boost'),
        ('stamina', 'Stamina Boost'),
        ('exp', 'EXP Boost'),
    ]
    # использовал список кортежей, так как список можно дополнить, а кортежи должны оставаться неизменные

    boost_type = models.CharField(max_length=20, choices=boosts)
    player = models.ForeignKey(
        Player, related_name='boosts', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.get_boost_type_display()} ({self.amount}) for {self.player.username}"
