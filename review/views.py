from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from review.forms import ticketForm
from review.models import Ticket
# Create your views here.
@login_required
def home(request):
    return render(request, 'review/home.html')

@login_required
def create_ticket(request):
    form = ticketForm()
    if request.method == 'POST':
        form = ticketForm(request.POST, request.FILES)
        if form.is_valid:
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('home')
    return render(request, 'review/ticket_create.html', context={'form' : form})

@login_required
def tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'review/tickets.html', context={'tickets':tickets, 'user':request.user})

@login_required
def ticket_delete(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('tickets')
    return render(request, 'review/ticket_delete.html', context={'ticket':ticket})

@login_required
def ticket_update(request, id):
    ticket = Ticket.objects.get(id=id)
    form = ticketForm(instance=ticket)
    if request.method == 'POST':
        form = ticketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('tickets')
    return render(request, 'review/ticket_update.html', context={'form':form})