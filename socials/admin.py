from django.contrib import admin
from .models import Profile,SocialTweet
from django.contrib.auth.models import User

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields =["username"]
    inlines = [ProfileInline]
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(SocialTweet)
