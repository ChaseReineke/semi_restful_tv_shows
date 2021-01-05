from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = ShowManager()

class ShowManager(models.Manager):   # Come back to this later. 
    def basic_validator(self, postData):
        errors = {}
        if len(postData["title"]) < 2:
            errors["title"] = "Title must have 2 or more characters."
        if len(postData["network"]) < 3:
            errors["network"] = "Network must have 3 or more characters."
        if len(postData["description"]) < 10:
            errors["description"] = "Description have 10 or more characters." 
        return errors
