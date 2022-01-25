'''from django.db.models.signals import post_save

# create the sugnals to use
def create_profile(sender,instance,create,**kwargs):
    if created:
        user_profile = Profile(user = instance, follows=[instance])
        user_profile.save()

post_save.create(create_profile, sender=user)'''