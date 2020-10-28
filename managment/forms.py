from django.forms import ModelForm
from .models import *

class PatientForm(ModelForm):
    class Meta:
        model = Patient_info
        fields = ['name','age','address','phone','email']

class TreatmentForm(ModelForm):
    class Meta:
        model = Treatment
        fields = ['add_treat']


class HistoryForm(ModelForm):
    class Meta:
        model = History
        fields = ['add_history']
