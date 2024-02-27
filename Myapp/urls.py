from django.urls import path
from Myapp import views

urlpatterns=[
    path('',views.homepage,name='my_home'),
    path('about/',views.about,name='my_about'),
    path('eventdetails/',views.eventdetails,name='event_details'),
    path('rentvenue/',views.rentvenue,name='rent_venue'),
    path('shows&events/',views.showsevents,name='shows_events'),
    path('tickets/',views.tickets,name='my_tickets'),
    path('ticketdetails',views.ticketdetails,name='ticket_details'),
]