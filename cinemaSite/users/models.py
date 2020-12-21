from django.db import models


class RestUser:

    email = models.EmailField(gettext_lazy('email address'), unique=True)
    name = models.CharField(max_length=150, unique=True)