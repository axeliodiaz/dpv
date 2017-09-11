from model_utils.models import TimeStampedModel, StatusModel
from django.db import models


class Divisa(TimeStampedModel, StatusModel):
    STATUS = Choices('bolivar', 'peso')

    precio = models.DecimalField()

    def __unicode__(self):
        return "{}: {}".format(self.created, self.precio)
