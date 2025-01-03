from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)  # Project title
    description = models.TextField()          # Project description
    link = models.URLField()                  # Link to the project (GitHub, live site, etc.)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.title
