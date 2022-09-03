from django.db import models
from django.contrib.auth.models import User


# Inits
LOCATIONS = (
    ("none", "none"),
    ("HABRA", "Habra"),
    ("ASHOKNAGAR", "Ashoknagar"),
    ("BARASAT", "Barasat"),
)

STATUSES = (
    ("BLACKLISTED", "BLACKLISTED"),
    ("OBJECTION", "OBJECTION"),
)


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=120, default="", blank=True)
    location = models.CharField(max_length=80, default="none", choices=LOCATIONS)
    status = models.CharField(max_length=50, default="OBJECTION", choices=STATUSES)

    lattitude = models.DecimalField(max_digits=12, decimal_places=6)
    longitude = models.DecimalField(max_digits=12, decimal_places=6)

    coordinates = [lattitude, longitude]

    
    def save(self, *args, **kwargs):
        self.coordinates = [self.lattitude, self.longitude]

        if len(self.title) == 0:
            self.title = self.location + f" - {self.status}"


        super(Board, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)



# SAMPLE
'''class Gig(models.Model):
    title = models.CharField(max_length=150, default="")

    destination = models.CharField(max_length=25, choices=countries)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    description = models.TextField()

    price = models.BigIntegerField() #In INR

    date_created = models.DateField()

    date_of_expiry = models.DateField()
    duration = models.IntegerField(default=0) # Days
    departure_date = models.DateField()
    return_date = models.DateField()

    max_people_count = models.IntegerField()

    def save(self, *args, **kwargs):
        # self.duration = (self.date_of_expiry - self.date_created).days


        super(Gig, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title + ' - ' +self.author.username)
'''