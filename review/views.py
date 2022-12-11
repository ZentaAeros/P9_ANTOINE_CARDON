from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from review.forms import ticketForm
from review.models import Ticket
# Create your views here.
@login_required
def home(request):
    return render(request, 'review/home.html')

def create_ticket(request):
    form = ticketForm()
    if request.method == 'POST':
        form = ticketForm(request.POST)
        form.save()
        return redirect('home')
    return render(request, 'review/ticket_create.html', context={'form' : form})

def tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'review/tickets.html', context={'tickets':tickets})