from django.db import models

CHOICES = {
    'priority': (
        ('Easy', 'Easy'),
        ('Hard', 'Hard'),
        ('Usual', 'Usual')
    ),
    'type': (
        ('PreLegend', 'PreLegend'),
        ('Legend', 'Legend'),
        ('Repeat Legend', 'Repeat Legend'),
        ('Lower A', 'Lower A'),
        ('Lower B', 'Lower B'),
        ('Upper A', 'Upper A'),
        ('Warning', 'Warning'),
        ('Paired A', 'Paired A'),
        ('Paired B', 'Paired B'),
    ),
    'status': (
        ('Finished', 'Finished'),
        ('In progress', 'In progress'),
        ('Kickback', 'Kickback'),
        ('Started', 'Started'),
        ('Suspend', 'Suspend')
    )
}


class Aircraft(models.Model):
    priority = models.CharField(max_length=15, choices=CHOICES['priority'])
    type = models.CharField(max_length=50, choices=CHOICES['type'])
    aircraft = models.CharField(max_length=150)  # что если назвать craft_model ?
    status = models.CharField(max_length=50, choices=CHOICES['status'])
    errors_count = models.IntegerField(default=0)
    info_count = models.IntegerField(default=0)

    def __str__(self):
        return self.aircraft
