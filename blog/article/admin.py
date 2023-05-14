from django.contrib import admin
from .models  import Article,Comment

# Register your models here.

admin.site.register(Comment)

@admin.register(Article)
class ArtcileAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"] #satırda başlık yazar ve tarihi ekleme
    list_display_links = ["title","created_date"] # title ve tarihi link türüne geçirme
    search_fields = ["title"] #title bilgisine göre arama çubuğu ekleme
    list_filter = ["created_date"] #filtreleme yapıp sayfaya eklenen zaman göre süzgeç yapar.
    
    class Meta:
        model = Article





