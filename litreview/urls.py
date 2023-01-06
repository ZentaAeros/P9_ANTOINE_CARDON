"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from authentication.forms import UserLoginForm
import authentication.views
import review.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
            template_name='authentication/login.html',
            authentication_form=UserLoginForm,
            redirect_authenticated_user=True),
        name='login'),
    path('logout/', authentication.views.logout_view, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('ticket/add/', review.views.create_ticket, name='create_ticket'),
    path('myposts/', review.views.myposts, name='myposts'),
    path('ticket/delete/<int:id>', review.views.delete_ticket, name='ticket_delete'),
    path('ticket/update/<int:id>', review.views.update_ticket, name='ticket_update'),
    path('subscription/', authentication.views.follow_user, name='followers'),
    path('subscription/unfollow_user/<int:id>', authentication.views.unfollow_user, name='unfollow_user'),
    path('feed/', review.views.feed, name='feed'),
    path('review/add/<int:id>', review.views.create_review_on_ticket, name='add_review'),
    path('review/update/<int:id>', review.views.update_review, name='update_review'),
    path('review/delete/<int:id>', review.views.delete_review, name='delete_review'),
    path('review/add/', review.views.create_ticket_and_review, name='create_ticket_and_review')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
