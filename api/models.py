from django.db import models
from django.utils import timezone

class Record(models.Model):
    record_id = models.AutoField(primary_key=True)
    player = models.CharField(max_length=45)
    highscore = models.IntegerField()
    record_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.player + ' ' + self.highscore