from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Vote
from apps.accounts.models import Profile

@receiver(post_save, sender=Vote)
def update_reputation_on_vote(sender, instance, created, **kwargs):
    owner = instance.content_object.author
    
    profile, _ = Profile.objects.get_or_create(user=owner)

    # update reputation based on vote value
    if instance.value == 1:
        profile.reputation += 10
    elif instance.value == -1:
        profile.reputation -= 2

    profile.save()