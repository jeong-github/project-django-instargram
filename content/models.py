from django.db import models

# Create your models here.
class Feed(models.Model):
    content = models.TextField()
    image = models.TextField()
    profile_image = models.TextField()
    user_id = models.TextField()
    like_count = models.IntegerField()


'''
class Designer(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)

    def __str__(self):
        return self.name

'''

