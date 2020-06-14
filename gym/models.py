from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.contrib.postgres.fields import ArrayField


class Trainer(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    #current_classes = ArrayField((Classes), blank=True)

    def __str__(self):
        return self.name + " " + self.surname


class Classes(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=250, default='class description', editable=True)
    is_favourite = models.BooleanField(default=False)


    def __str__(self):
        return '{} - {}'.format(self.name, self.description)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=500, blank=True)
    surname = models.CharField(max_length=30, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()