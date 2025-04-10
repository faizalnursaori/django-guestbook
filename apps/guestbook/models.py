from django.db import models

from core.models import BaseModel
from core.utils import generate_id


# Create your models here.
class Guest(BaseModel):
    id = models.CharField(
        primary_key=True, max_length=100, default=generate_id, editable=False
    )
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    purpose = models.TextField()
    visit_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
