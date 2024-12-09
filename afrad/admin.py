from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

class TypeMoshtariinline(admin.StackedInline):
    model=TypeMoshtari
    extra=1


@admin.register(Moshtari)
class MoshtariPanel(admin.ModelAdmin):
    list_display=["name", "phone", "statusphone", "status", "variz", "callButton"]
    inlines=[TypeMoshtariinline]
    list_filter=["name", "phone", "statusphone", "status", "variz"]

    @admin.display(description="تماس بگیرید")
    def callButton(self, obj):
        return format_html(f"<a href='tel:+98{obj.phone}'>تماس با شخص</a>")