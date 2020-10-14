from django.db import models

# Create your models here.
class UserInfo(models.Model):
    cert_id = models.CharField(max_length=32)
    cert_no = models.CharField(max_length=20)
    cert_name = models.CharField(max_length=20)
    # db_column是数据表中字段，verbose_name是admin页面展示
    pub_date = models.DateField(db_column='insert_date', verbose_name='日期')
    objects = models.Manager()

    def __str__(self):
        return "cert_id:{0}, cert_no:{1}, cert_name:{2}, insert_date:{3}".format(self.cert_id, self.cert_no, self.cert_name, self.pub_date) # 中文需要utf8编码

    class Meta:
        db_table = 'userinfo'  # 用户数据表
        verbose_name = '用户信息'  # admin页面显示的表
        verbose_name_plural = '用户信息'  # admin页面显示的表复数，中文的一般与单数一致