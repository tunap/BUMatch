from django.db import models
from django.utils import timezone

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=10)
    user_my_gender = models.IntegerField()
    user_ur_gender = models.IntegerField()
    user_description = models.CharField(max_length=20)

    user_login_id = models.CharField(max_length=20)
    user_login_pw = models.CharField(max_length=20)
    user_phone_no = models.CharField(max_length=20)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Favor(models.Model):
    favor_key = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    favor_id = models.IntegerField()
    favor_value = models.IntegerField()
    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Gachi(models.Model):
    gachi_key = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    gachi_id = models.IntegerField()
    gachi_value = models.TextField()
    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Match(models.Model):
    user_id_stt = models.IntegerField() #foreignKey..
    user_id_end = models.IntegerField()
    is_watched = models.BooleanField(default=False)
    score = models.IntegerField()
    is_picked = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
