from django.db import models
from django.contrib.auth import get_user_model


class Photo(models.Model):
    image = models.ImageField(upload_to='photos', null=False, blank=False)
    signature = models.CharField(max_length=250, null=False, blank=False,)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='User', null=False, blank=False)
    user_favorite = models.ManyToManyField(get_user_model(), related_name='like_publications', blank=True)


    def __str__(self):
        return self.signature