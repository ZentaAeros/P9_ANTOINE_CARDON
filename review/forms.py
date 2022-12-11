from django import forms
from review.models import Ticket
class ticketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'