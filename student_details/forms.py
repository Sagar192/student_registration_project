from django import forms
from .models import Students, Admission, FeePaid

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        exclude = ['student']


class FeePaidForm(forms.ModelForm):
    class Meta:
        model = FeePaid
        exclude = ['admission']