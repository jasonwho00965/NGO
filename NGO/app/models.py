from django.db import models


# Create your models here.
class User(models.Model):
    ROLE_CHOICES = [('A', 'Admin'), ('U', 'User')]
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    """Testing blank=True on role. If any problems arise, let Ed know."""
    role = models.CharField(choices=ROLE_CHOICES, max_length=1, blank=True)

    """Enables admin to view data other than "User object" within admin screen."""
    def __str__(self):
        return self.first_name, self.last_name, self.email, self.role


class Event(models.Model):
    EVENT_CHOICES = [('Con', 'Conference'),
                     ('Sem', 'Seminar'),
                     ('Pres', 'Presentation'),
                     ]
    e_name = models.CharField(max_length=35)
    e_description = models.TextField(max_length=255)
    e_category = models.CharField(choices=EVENT_CHOICES, max_length=4)
    e_start_date = models.DateField()
    e_end_date = models.DateField()
    e_start_time = models.DateTimeField()
    e_end_time = models.DateTimeField()
    e_location = models.CharField(max_length=50)
    """Clarification on registrants required...-Ed"""
    registrants = models.BooleanField()
    """Testing image field height and width. -Ed"""
    e_image = models.ImageField(height_field=60, width_field=60)
    e_adult_price = models.DecimalField(max_digits=5, decimal_places=2)
    e_child_price = models.DecimalField(max_digits=5, decimal_places=2)

