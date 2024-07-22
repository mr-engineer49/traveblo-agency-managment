from django.db import models

# Create your models here.

class Action(models.Model):
    ACTIVE_COLORS = {
        'Active': 'bg-green-600',
        'Edit/On Hold': 'bg-yellow-600',
        'Remove/Pause': 'bg-red-500',   
    }

    actions = models.CharField(max_length=100)
    
    def __str__(self):
        return self.actions
    
    def get_actions_color(self):
        return self.ACTIVE_COLORS.get(self.actions, '')
