from django.db import models
from phone_field import PhoneField



# Create your models here.
class UserManagement(models.Model):
    ROLE_CHOICES = [('U','User'),('A','Admin')]
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
    """Testing blank=True on role. If any problems arise, let Ed know."""
    role = models.CharField(choices=ROLE_CHOICES, max_length=5, blank=True)

    """Enables admin to view data other than "User object" within admin screen."""
    #def __str__(self):
        #return self.first_name, self.last_name, self.email, self.password, self.role


class EventManagement(models.Model):
    EVENT_CHOICES = [('Con', 'Conference'),
                     ('Sem', 'Seminar'),
                     ('Pres', 'Presentation')
                     ]
    Event = models.CharField(max_length=35)
    e_description = models.TextField(max_length=255)
    Category = models.CharField(choices=EVENT_CHOICES, max_length=4)
    Start_date = models.DateField()
    End_date = models.DateField()
    e_start_time = models.DateTimeField()
    e_end_time = models.DateTimeField()
    Location = models.CharField(max_length=50)
    """Clarification on registrants required...-Ed"""
    registrants = models.BooleanField()
    """Testing image field height and width. -Ed"""
    e_image = models.ImageField()
    e_adult_price = models.DecimalField(max_digits=5, decimal_places=2)
    e_child_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return u'%s' % self.Event

def change_button(self, obj):
    return format_html('<a class="btn" href="/admin/my_app/my_model/{}/change/">Change</a>', obj.id)

def delete_button(self, obj):
    return format_html('<a class="btn" href="/admin/my_app/my_model/{}/delete/">Delete</a>', obj.id)

list_display = ('__str__', 'change_button', 'delete_button')