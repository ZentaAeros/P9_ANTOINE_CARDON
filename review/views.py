from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from review.forms import TicketForm, ReviewForm
from review.models import Ticket, Review
from review.utils import get_tickets, get_reviews
# Create your views here.

@login_required
def feed(request):
    tickets = get_tickets(request.user, user_follows=True)
    return render(request, 'review/feed.html', context={'tickets':tickets})

@login_required
def myposts(request):
    tickets = get_tickets(request.user)
    reviews = get_reviews(request.user)
    return render(request, 'review/tickets.html', context={'tickets':tickets, 'user':request.user, 'reviews':reviews})

@login_required
def create_ticket(request):
    form = TicketForm()
    if request.method == 'POST':
        if request.FILES:
            form = TicketForm(request.POST, request.FILES)
        else:
            form = TicketForm(request.POST)
        if form.is_valid:
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('feed')
    return render(request, 'review/ticket_create.html', context={'form' : form})

@login_required
def update_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    form = TicketForm(instance=ticket)
    if request.method == 'POST':
        if request.FILES:
            form = TicketForm(request.POST, request.FILES, instance=ticket)
        else:
            form = TicketForm(request.POST, instance=ticket)

        if form.is_valid():
            form.save()
            return redirect('tickets')
    return render(request, 'review/ticket_update.html', context={'form':form})

@login_required
def delete_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('feed')
    return render(request, 'review/ticket_delete.html', context={'ticket':ticket})

@login_required
def create_review_on_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.ticket = ticket
            form.user = request.user
            form.save()
            return redirect('feed')
    return render(request, 'review/create_review.html', context={'form':form})

@login_required
def update_review(request, id):
    review = Review.objects.get(id=id)
    form = ReviewForm(instance=review)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('feed')
    return render(request, 'review/update_review.html', context={'form':form})

@login_required
def delete_review(request, id):
    review = Review.objects.get(id=id)
    if request.method == 'POST':
        review.delete()
        return redirect('feed')
    return render(request, 'review/delete_review.html', context={'review':review})

@login_required
def create_ticket_and_review(request):
    ticketForm = TicketForm()
    reviewForm = ReviewForm()
    if request.method == 'POST':
        if request.FILES:
            ticketForm = TicketForm(request.POST, request.FILES)
            reviewForm = ReviewForm(request.POST)
        else:
            ticketForm = TicketForm(request.POST)
            reviewForm = ReviewForm(request.POST)
        
        if ticketForm.is_valid() & reviewForm.is_valid():
            ticketForm = ticketForm.save(commit=False)
            reviewForm = reviewForm.save(commit=False)
            ticketForm.user = request.user
            reviewForm.user = request.user
            reviewForm.ticket = ticketForm
            ticketForm.save()
            reviewForm.save()
            return redirect('feed')
    return render(request, 'review/create_review_and_ticket.html', context={'ticketForm':ticketForm, 'reviewForm':reviewForm})