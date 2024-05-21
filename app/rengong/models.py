from django.db import models

# Create your models here.
class ren(models.Model):
    name = models.CharField(max_length=100,verbose_name="名称")
    pub_data = models.DateField(verbose_name='时间',null=True)





    def __str__(self):
        return self.name

    class Meta:
        verbose_name ='人工名称'
        verbose_name_plural =verbose_name
        db_table ='human'
