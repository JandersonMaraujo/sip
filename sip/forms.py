from django import forms
from sip.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_date', 'user', 'product', 'amount', 'unit_price', 'notes'] 