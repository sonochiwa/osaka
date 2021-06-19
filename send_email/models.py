from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.email