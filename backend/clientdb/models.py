from django.db import models

class Client(models.Model):
    client_ref = models.CharField(max_length=10, blank=False)
    dob = models.DateField('date of birth')
    full_name = models.CharField(max_length=60)
    hk_id = models.CharField(max_length=20)
    
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
    )

    tel = models.CharField(max_length=12)
    address = models.CharField(max_length=120)
    area = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
