from django.db import models


class Airport(models.Model):
    DIRECTION_CHOICES = (
        ('L', 'Left'),
        ('R', 'Right'),
    )

    airport_name = models.CharField(max_length=100)
    airport_code = models.CharField(max_length=10, unique=True)
    position = models.CharField(max_length=1, choices=DIRECTION_CHOICES)
    duration = models.IntegerField()

    left = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='left_node'
    )
    right = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='right_node'
    )

    def __str__(self):
        return f"{self.airport_name} ({self.airport_code})"

    