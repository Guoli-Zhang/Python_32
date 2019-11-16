from django.contrib import admin
from person.models import BookInfo, HeroInfo

# Register your models here.

admin.site.register(BookInfo)
admin.site.register(HeroInfo)
admin.site.site_header = '传智书城'
admin.site.site_title = '传智书城MIS'
admin.site.index_title = '欢迎使用传智书城MIS'

@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    list_per_page = 2
    actions_on_top = True
    actions_on_bottom = False
    list_display = ['id', 'btitle', 'bpub_date', 'bread', 'bcomment']


@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_per_page = 4
    actions_on_top = True
    actions_on_bottom = False
    list_display = ['hname', 'hgender', 'hcomment', 'hbook']

# admin.site.register(BookInfo, BookInfoAdmin)
# admin.site.register(HeroInfo, HeroInfoAdmin)









