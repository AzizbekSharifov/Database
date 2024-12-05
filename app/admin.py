from django.contrib import admin
from .models import  Place, Week, Flight, Passenger,SimpleUser, Ticket
# Register your models here.
admin.site.register(Place)
admin.site.register(Week)
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(SimpleUser)
admin.site.register(Ticket)