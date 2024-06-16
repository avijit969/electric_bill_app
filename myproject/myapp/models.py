from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ElectricBill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    createdAt = models.DateTimeField(default=timezone.now, verbose_name="Created At")
    updatedAt = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    meterReading = models.PositiveIntegerField(verbose_name="Meter Reading")
    BLSStaffNo = models.PositiveIntegerField(verbose_name="BLS Staff Number")
    quatreNO = models.PositiveIntegerField(verbose_name="Quarter Number")
    image = models.ImageField(upload_to='bills/', verbose_name="Bill Image")

    def __str__(self):
        return f'{self.user.username} - Bill {self.createdAt.strftime("%Y-%m-%d %H:%M:%S")}'

    class Meta:
        verbose_name = "Electric Bill"
        verbose_name_plural = "Electric Bills"
        ordering = ['-createdAt']
