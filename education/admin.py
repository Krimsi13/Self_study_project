from django.contrib import admin

from education.models import Section, Material


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'owner')


@admin.register(Material)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'section', 'owner')
