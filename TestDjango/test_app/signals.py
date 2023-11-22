from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from .models import Author

@receiver(post_save, sender=Author)
def author_created(sender, instance, created, **kwargs):
    if created:
        print(f"Добавлен новый писатель: {instance}")
        # Здесь вы можете выполнять другие действия или отправлять уведомления
