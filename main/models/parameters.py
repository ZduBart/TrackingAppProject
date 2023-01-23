from django.db import models


class Parameters(models.Model):
    param_id = models.IntegerField(primary_key=True)
    param_desc = models.TextField(max_length=50)

    def __str__(self):
        return f"ID:{self.param_id} | {self.param_desc}"
