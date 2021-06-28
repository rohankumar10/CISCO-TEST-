from django.db import models


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Router(models.Model):
    id = models.AutoField(primary_key=True)
    host_name = models.CharField(max_length=200)
    sap_id = models.CharField(max_length=200)
    loopback_id = models.CharField(max_length=200)
    ipv4 = models.CharField(max_length=200)
    mac_address = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'router_info'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
