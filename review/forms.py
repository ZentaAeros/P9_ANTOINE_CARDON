from django import forms
from review.models import Ticket, Review

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'headline', 'body']

class SearchUser(forms.Form):
    user = forms.CharField(max_length=250, label="Saisissez le nom d'utilisateur ")