from django import forms
from jobportal.models import JobApply

class JobApplyForm(forms.ModelForm):
    class Meta:
        model = JobApply
        fields = ['job']