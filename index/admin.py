from django.contrib import admin
from .models import Home
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Home)
class HomeAdmin(SummernoteModelAdmin):

    list_display = ('title','content')
    search_fields = ['title']
    summernote_fields = ('content',)

# Register your models here.
# admin.site.register(Home)

