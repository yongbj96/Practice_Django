from django.db import models

class Member(models.Model):
    username = models.CharField(max_length=20)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table            = 'members' # 데이터베이스에 저장되는 테이블명
        verbose_name        = '회원' # 해당 테이블을 불러오는 이름
        verbose_name_plural = '회원목록' # 해당 테이블을 불러오는 그룹이름