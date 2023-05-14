from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete= models.CASCADE, verbose_name="Yazar") # Bu kodda on_delete=models.CASCADE kullanarak, bir müşteri kaydı silindiğinde, bu müşteriye bağlı olan tüm siparişler de otomatik olarak silinecektir. 
    title = models.CharField(max_length=50,verbose_name="Başlık") #verbose_name model alanının okunabilir adını belirlemek için kullanılır ve kodunuzu daha anlaşılır hale getirmenize yardımcı olur.
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşuturlma Tarihi")
    article_image = models.FileField(blank = True, null = True, verbose_name="Makaleye Fotoğraf Ekleyin", upload_to='media/')
    def __str__(self):
        return self.title 
    class Meta:
        ordering =['-created_date']




class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="İsim")
    comment_content = models.CharField(max_length= 200,verbose_name="Yorum:")
    comment_date = models.DateTimeField(auto_now_add = True)
    def __Str__(self):
        return self.comment_content
    class Meta:
        ordering =['-comment_date']
    
