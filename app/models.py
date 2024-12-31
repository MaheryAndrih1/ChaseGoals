from django.db import models

# Create your models here.
class Goal(models.Model):
    id_goal=models.AutoField(primary_key=True)
    name_goal=models.CharField(max_length=250)
    
    def __str__(self):
        return self.name_goal
    