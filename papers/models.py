from django.db import models

    
class ResearchPaper(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    summary = models.TextField()

    class Meta:
        """Return a list of objects in ascending order."""
        ordering = ['title']

    def __str__(self):
        """This makes your admin page more descriptive."""
        return self.title
