from django.db import models

from users.models import CustomUser


class DecimalRangeField(models.DecimalField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.DecimalField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(DecimalRangeField, self).formfield(**defaults)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    ticket_price = models.DecimalField(decimal_places=2, max_digits=5)
    rating = DecimalRangeField(min_value=0.0, max_value=10.0, decimal_places=2, max_digits=4)

    def __str__(self):
        return self.title


class Ticket(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
