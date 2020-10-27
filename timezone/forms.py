from django import forms
from .models import DateTime

class DateTimeForm(forms.ModelForm):

	class Meta:
		model = DateTime
		fields = ['User_Time_Zone', 'User_Date_Time']