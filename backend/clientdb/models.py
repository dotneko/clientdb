from django.db import models
from django.urls import reverse

class Client(models.Model):
    client_ref = models.CharField(max_length=10, blank=False)
    dob = models.DateField('date of birth', blank=True, null=True)
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

    tel = models.CharField(max_length=12, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)
    area = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-client_ref',)

    def __str__(self):
        return '{} | {} - {}'.format(
            self.client_ref, self.full_name, self.hk_id
        )
    
    def get_absolute_url(self):
        return reverse('clientdb:ClientDetail', kwargs={'pk': self.pk})