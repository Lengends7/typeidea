from django.contrib import admin

from .models import Link, SideBar

# Register your models here.typeidea/typeidea/config/models.py

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')

    def save_model(self, request, obj, change):
        obj.user = request.user
        return super(LinkAdmin, self).save_model(self, request, obj, change)


@admin.register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_type', 'content','created_time')
    fields = ('titie', 'display_type', 'content')

    def save_model(self, request, obj, change):
       obj.user = request.user
       return super(SideBarAdmin, self).save_model(self, request, obj, change) 