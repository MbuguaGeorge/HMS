from django.contrib import admin
from .models import Profile, Room, Block, Hostel_Manager, Caretaker, Hostel

# Register your models here.
admin.site.register(Profile)
admin.site.register(Room)
admin.site.register(Hostel)
admin.site.register(Hostel_Manager)
admin.site.register(Caretaker)
admin.site.register(Block)