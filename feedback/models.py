from django.db import models


class Feedback(models.Model):
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'