from django.db import models

from model_utils.models import TimeStampedModel
from model_utils import Choices


class Divisa(TimeStampedModel):
    precio = models.DecimalField(max_digits=1000, decimal_places=3)

    class Meta:
        abstract = True

    def __unicode__(self):
        return "{}: {}".format(self.created, self.precio)


class TipoDivisa(Divisa):
    nombre = models.CharField(blank=True, max_length=100)
