from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    info = models.CharField(max_length=150)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('female', 'Female'),
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=now())
    # models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']