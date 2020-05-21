from django.db import models
# Create your models here.


class ImageId(models.Model):
    image_id = models.IntegerField(default=1, unique=True, verbose_name="题目ID")
    image_name = models.CharField(max_length=20, verbose_name="题目名称")


class ImageInfo(models.Model):
    uuid = models.CharField(max_length=100, verbose_name='会话 uuid')
    skey = models.CharField(max_length=100, verbose_name='会话 Skey')
    image_path = models.CharField(max_length=200, verbose_name="画作路径")
    imageKey = models.ForeignKey('ImageId', on_delete=models.CASCADE, verbose_name="画作题目")

