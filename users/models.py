from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.utils import timezone

from users.managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    objects = CustomUserManager()

    username = models.CharField(
        max_length=300, unique=True,
        validators=[RegexValidator(regex = '^[a-zA-Z0-9.+-_]*$',
                                   message='Username must be alphanumeric or contain numbers',
                                   code='invalid_username')
                    ])

    email = models.EmailField(max_length=255, unique=True, verbose_name='email address')
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    LOCATIONS = (
        ('LHR', 'Lahore'),
        ('ISL', 'Islamabad'),
        ('KHI', 'Karachi'),
        ('PEW', 'Peshawar'),
        ('QTA', 'Quetta'),
    )

    first_name = models.CharField(max_length=50, blank=True, default='')
    last_name = models.CharField(max_length=50, blank=True, default='')
    bio = models.TextField(max_length=500, blank=True, default='')
    location = models.CharField(max_length=3, choices=LOCATIONS, default='LHR')
    birth_date = models.DateField(null=True, blank=True, default=timezone.now)
    user_number = models.IntegerField(default=0)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if self.user_number == 0:
            self.user_number = CustomUser.objects.count() + 1
            self.save()
        super(CustomUser, self).save(*args, **kwargs)


@receiver(post_save, sender=CustomUser)
def save_custom_user(sender, instance, created, **kwargs):
    if created:
        print("custom user record save successfully!!")
    else:
        print("custom user record updated successfully!!")
