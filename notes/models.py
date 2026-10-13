from django.db import models


class Note(models.Model):
    CATEGORY_CHOICES = [
        ('python', 'Python'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('javascript', 'JavaScript'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    question = models.CharField(max_length=200)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question