from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from users.models import UserProfile


@receiver(post_delete, sender=UserProfile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Удалить файл из FS, когда удаляется объект."""
    if instance.photo:
        instance.photo.delete(save=False)


@receiver(pre_save, sender=UserProfile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    При обновлении: если меняется файл, удалить старый.
    Работает, только если у instance уже есть pk в базе.
    """
    if not instance.pk:
        return
    try:
        old = sender.objects.get(pk=instance.pk).photo
    except sender.DoesNotExist:
        return
    new = instance.photo
    # если старый файл отличен от нового и старый не пустой
    if old and old != new:
        old.delete(save=False)
