from django.db.models import signals
from django.contrib.auth.models import User
from advisor.models import Profile
from advisor.models import Preferences
from advisor.models import Privacy
from advisor.models import Plan

def create_user_related_records(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Preferences.objects.create(user=instance)
        Privacy.objects.create(user=instance)
        Plan.objects.create(user=instance)

signals.post_save.connect(create_user_related_records, sender=User)