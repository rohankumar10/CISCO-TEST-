from django.db import models

# Create your models here.
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
