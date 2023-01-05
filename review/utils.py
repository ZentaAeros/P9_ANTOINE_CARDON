from authentication.models import User, UserFollows
from review.models import Ticket, Review
def get_tickets(user, user_follows=False):
    if user_follows == True:
        users_followed = get_followed_user(user)
    else:   
        users_followed = []
    users_followed.append(user)
    tickets = Ticket.objects.filter(user__in=users_followed)
    reviews = Review.objects.all()
    posts = []
    tickets = sorted(tickets, key=lambda ticket:ticket.time_created, reverse=True)
    for ticket in tickets:
        try:
            review = Review.objects.get(ticket=ticket.id)
            post = {'ticket': ticket, 'review':review}
            posts.append(post)
        except Review.DoesNotExist:
            review = None
            post = {'ticket': ticket, 'review':review}
            posts.append(post)
    return posts

def get_reviews(user, user_follows=False):
    if user_follows == True:
        users_followed = get_followed_user(user)
    else:   
        users_followed = []
    users_followed.append(user)
    reviews = Review.objects.filter(user__in=users_followed)
    posts = []
    reviews = sorted(reviews, key=lambda ticket:ticket.time_created, reverse=True)
    return reviews
    
def get_followed_user(user):
    users = UserFollows.objects.filter(user=user)
    user_owned = User.objects.get(id=user.id)
    followed_users = []
    for follower in users:
        followed_users.append(follower.followed_user)
    
    return followed_users