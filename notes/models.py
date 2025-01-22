from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Note(models.Model):
    topic = models.ForeignKey(Topic, related_name="notes", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    related_notes = models.ManyToManyField("Note", blank=True, null=True)

    def __str__(self):
        return self.title
    