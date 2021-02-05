from django.contrib import admin
from .models import Horse, Jockey, Outcome, Profile, Experience

# Register your models here.
admin.site.register(Horse)
admin.site.register(Jockey)
admin.site.register(Outcome)
admin.site.register(Experience)
admin.site.register(Profile)