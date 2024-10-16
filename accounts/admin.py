from django.contrib import admin
from fires.models import Feedback

# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')  # 목록에서 보일 필드
    search_fields = ('name', 'email', 'subject')  # 검색 가능한 필드

admin.site.register(Feedback, FeedbackAdmin)