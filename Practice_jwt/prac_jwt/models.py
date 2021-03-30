from django.db import models

class user_data(models.Model):
    id          = models.CharField(max_length=20, verbose_name='유저ID', primary_key=True)
    pw          = models.CharField(max_length=20, verbose_name='유저PW')
    name        = models.CharField(max_length=10, verbose_name='이름')
    create_at   = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')
    update_at   = models.DateTimeField(auto_now=True, verbose_name='마지막 수정일')

    USERNAME_FIELD = 'id'

    def __str__(self):
        return self.id
    
    class Meta:
        db_table            = 'users'
        verbose_name        = '유저'
        verbose_name_plural = '유저목록'