from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    # 길이가 제한된 문자
    title = models.CharField(max_length=200)
    # 길이가 제한되지 않은, 무한인 문자
    text = models.TextField(blank=True)
    # 작성일 값 생성
    created_date = models.DateTimeField(default=timezone.now)
    # 저장한 일자 값 생성
    published_date = models.DateTimeField(blank=True)

    # 현재시각을 넣은다음 저장해준다.
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title