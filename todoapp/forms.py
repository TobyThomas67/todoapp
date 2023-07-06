from todoapp.models import todoapp

from django import forms

class dateinput(forms.DateInput):
    input_type="date"
class todoform(forms.ModelForm):
    class Meta:
        model=todoapp
        fields="__all__"

