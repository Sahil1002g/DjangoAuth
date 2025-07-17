from django.db import models
from django.conf import settings

CATEGORY_CHOICES = [
    ('mental', 'Mental Health'),
    ('heart', 'Heart Disease'),
    ('covid', 'Covid19'),
    ('immune', 'Immunization'),
]

class BlogPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def truncated_summary(self):
        words = self.summary.split()
        return ' '.join(words[:15]) + '...' if len(words) > 15 else self.summary