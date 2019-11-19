from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}:{self.title}'
        #어떤 값이 들어간지 알려주는 코드

# Create your models here.
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    # foreignKey(어떤테이블을 참조, 그 테이블이 삭제될때 어떻게 할지)
    # models.CASCADE : 부모테이블이 삭제시 같이 삭제하는 옵션
    # models.PROTECT : 부모테이블이 삭제 될때 오류 발생.
    # models.SET_NULL : 삭제되었을 때 부모 창고 값에 NULL 값으로 채움, 단 not null
    # models.SET() :  특정 함수를 호출
    # models.DO_NOTHING : 암것도 안함.
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now_add=True) 

    

    