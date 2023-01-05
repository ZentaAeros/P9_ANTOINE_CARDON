from django.test import TestCase

class Ticket:
    def __init__(self, title):
        self.title = title
    
    def __str__(self):
        return self.title

class Review:
    def __init__(self, review):
        self.review = review
    
    def __str__(self):
        return self.review
alltickets = []
review1 = Review('Ma première review')
review2 = Review('Ma seconde review')
ticket1 = Ticket('Le titre ici')
ticket2 = Ticket('Mon ticket 2')
myticket1 = {'ticket': ticket1, 'review':review1}
myticket2 = {'ticket': ticket2, 'review':review2}

alltickets.append(myticket1)
alltickets.append(myticket2)

for ticket in alltickets:
    print(ticket["ticket"])
    print(ticket["review"])
# Create your tests here.
def get_tickets_user_follows(user):
    users_followed = get_followed_user(user)
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
            pass
    return posts

def get_followed_user(user):
    users = UserFollows.objects.filter(user=user)
    followed_users = []
    for follower in users:
        followed_users.append(follower.followed_user)
    
    return followed_users