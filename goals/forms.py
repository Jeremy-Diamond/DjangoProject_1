from django import forms
from .  import models

class CreateGoalForm(forms.ModelForm):
    class Meta:
        model = models.Goal
        fields = ['title', 'details', 'image']