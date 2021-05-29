from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
#class とはモデルのこと。postというモデルを作ること。
class Post(models.Model):
    #ForeignKeyは別のモデル(会員登録されてる人とか)と繋げる
    #modelsの中のForeignKeyをautherの中に設定
    #on_delete
    #
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    #textとcharフィールドの違いは？→無し。慣例的にはcharの方が短い内容が入る
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        #selfのpublishd_date にtimezone.nowを代入する。published_dateをいじる
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    #python manage.py makemigrations blog　では、変更したことをdjangoに記憶させる

