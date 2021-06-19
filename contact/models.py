from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class Mailing(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Рассылки'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        return self.title
