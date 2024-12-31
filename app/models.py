from django.db import models

# Create your models here.
class Goal(models.Model):
    id_goal=models.AutoField(primary_key=True)
    name_goal=models.CharField(max_length=250)
    is_achieved=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name_goal
    