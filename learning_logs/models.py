from django.db import models


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Теми'

    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Допис'
        verbose_name_plural = 'Дописи'

    def __str__(self):
        if len(self.text) <= 50:
            return self.text
        else:
            return f'{self.text[:50]}...'
