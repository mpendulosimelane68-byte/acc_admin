from django.db import models
import random
import string

def generate_code():
    return "ACC-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=3)) + "-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))

class Report(models.Model):
    code = models.CharField(max_length=20, unique=True, default=generate_code, editable=False)
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code