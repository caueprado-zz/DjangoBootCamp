from django.contrib import admin

# Register your models here.
from evolution_app.models import Topic, Webpage, AccessRecord, User

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(User)
