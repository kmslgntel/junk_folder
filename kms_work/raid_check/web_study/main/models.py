from django.db import models

# Create your models here.
# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()

    created_at = models.DataTimeField()

    # 게시글의 제목(postname)이 Post object 대신하기
    def __str__(self):
        return self.postname



# class test(models.Model):
#     postname = models.CharField(max_length=50)
#     contents = models.TextField()

#     # 게시글의 제목(postname)이 Post object 대신하기
#     # 이게 뭐라고?
#     def __str__(self):
#         return self.postname