from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Profile(models.Model):
    CHOICES_ROLES = [
        ("C", "Cashier"),
        ("M", "Manager"),
        ("S", "Supervisor"),
        ("SL", "Shift Lead"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.IntegerField(default=1, validators=[MaxValueValidator(10)])
    role = models.CharField(max_length=2, choices=CHOICES_ROLES ,default='C')

    def __str__(self):
        return str(self.user.id)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_notifications")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="sent_notifications")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.sender} to {self.user}: {self.message[:50]}"

