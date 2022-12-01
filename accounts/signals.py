from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import User, UserProfile


@receiver(post_save, sender=User)  
def Post_save_create_profile_signal(sender, instance, created, **kwargs):
    if created is True:
        UserProfile.objects.create(user=instance)
    else:
        try:
            updated_profile = UserProfile.objects.get(user=instance)
            updated_profile.save()
        except:
            # create user profile if not exist
            UserProfile.objects.create(user=instance)
    

# post_save.connect(post_save_create_profile_signal, sender=User)