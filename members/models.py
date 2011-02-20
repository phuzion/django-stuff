from django.db import models

LICENSE_CHOICES = (
    ('NO', 'Novice'),
    ('TE', 'Technician'),
    ('GE', 'General'),
    ('EX', 'Extra'),
    ('NL', 'No License'),
)

OFFICE_CHOICES = (
    ('ME', 'Member'),
    ('AD', 'Staff Advisor'),
    ('PR', 'Club President'),
    ('VP', 'Vice President'),
    ('TR', 'Secretary/Treasurer'),
    ('LT', 'License Trustee'),
    ('SA', 'Systems Administrator'),
    ('PM', 'Prospective Member'),
    ('NA', 'Non Associate'),
    ('AS', 'Associate'),
    ('FC', 'Flux Capacitor Maintenance Dude'),
)

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name
    callsign = models.CharField(max_length=8, blank=True, help_text="If the member does not have a call sign, leave this field blank.")
    license = models.CharField(max_length=2, choices=LICENSE_CHOICES)
    office = models.CharField(max_length=2, choices=OFFICE_CHOICES)
    email = models.EmailField(max_length=75, blank=True)
    active = models.BooleanField(default=True, help_text="Is the member still active in the club?")


