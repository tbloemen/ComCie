import email
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.utils import timezone

# Create your models here.


class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self) -> str:
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


class Role(models.Model):
    name = models.CharField()

    def __str__(self) -> str:
        return self.name


class Person(models.Model):
    name = models.CharField()
    email = models.CharField(blank=True)
    tel = models.CharField(blank=True)
    roles: models.ManyToManyField = models.ManyToManyField(Role)

    def __str__(self):
        return self.name


class Instrument(models.Model):
    name = models.CharField()

    def __str__(self) -> str:
        return self.name


class Musician(Person):
    instrument = models.ManyToManyField(Instrument)
    is_in_artiestenverloningen = models.BooleanField(default=False)

    def __str__(self):
        return super().__str__() + f" on the {self.instrument}"


class Combo(models.Model):
    COMBO_TYPES = [
        ('GrCo', 'Groovercombo'),
        ('VeCo', 'Verenigingscombo'),
        ('HoCo', 'Hopend combo'),
        ('GeCo', 'Gelegenheidscombo'),
    ]

    name = models.CharField(max_length=100)
    combo_type = models.CharField(
        max_length=4, choices=COMBO_TYPES, default='GrCo')
    is_active = models.BooleanField(default=True)
    contact = models.ManyToManyField(Person)
    email = models.CharField()
    tel = models.CharField()
    musicians = models.ManyToManyField(Musician)
    price = models.CharField()
    style = models.CharField()
    demos = models.CharField()

    def __str__(self) -> str:
        return self.name


class Gig(models.Model):

    GIG_STATUS = [
        ("US", "Unsigned"),
        ("S", "Signed"),
        ("B", "Billed"),
        ("A", "At Artiestenverloningen"),
        ("CO", "To collect"),
        ("P", "Payed"),
        ("D", "Done"),
        ("CAB", "Cancelled due to budget"),
        ("CAA", "Cancelled due to unavailability"),
        ("CAO", "Cancelled due to having found another combo"),
        ("CAR", "Cancelled due to no response"),
        ("CAM", "Cancelled due to a miscellaneous reason"),
        ("NA", "Not Applicable"),
        ("IR", "Instruments reservation"),
        ("IB", "Instruments billed"),
        ("IC", "Instruments cancelled"),
        ("ICC", "Instruments reservation committee"),
        ("AL", "At Lars"),
        ("PL", "Payed through Lars")
    ]

    date = models.DateField(blank=True, null=True)
    name = models.CharField()
    last_updated = models.DateTimeField(default=timezone.now())
    status = models.CharField(max_length=3, choices=GIG_STATUS, default="US")
    handler: Person = models.ForeignKey(Person, on_delete=models.CASCADE)
    gig_type = models.CharField()
    # TODO implement gigtype enum
    city = models.CharField()
    length = models.IntegerField()
    starting_time = models.TimeField()
    contact = models.ForeignKey(Person, on_delete=CASCADE)
    billing_credentials = models.TextField()
    address = models.CharField()
    gage = models.IntegerField()
    afdracht = models.IntegerField()
    instruments = models.TextField()
    comments = models.TextField()

    def save(self, *args, **kwargs):
        # Might not work
        if self.handler.roles.all().filter(name="ComCie").exists():
            return
        if self.contact.roles.all().filter(name="Client").exists():
            return
        return super().save(*args, **kwargs)
