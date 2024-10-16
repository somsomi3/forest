from django.db import models

# Create your models here.
from django.db import models

class FireRiskForecast(models.Model):
    REGION_RISK_LEVEL_CHOICES = [
        ('low', '낮음'),
        ('medium', '중간'),
        ('high', '높음'),
    ]
    
    region_name = models.CharField(max_length=100)  # 지역 이름
    risk_level = models.CharField(max_length=10, choices=REGION_RISK_LEVEL_CHOICES)  # 위험 수준 (낮음, 중간, 높음 등)
    forecast_date = models.DateField()  # 예보 날짜
    temperature = models.FloatField()  # 온도
    humidity = models.FloatField()  # 습도
    wind_speed = models.FloatField()  # 풍속
    precipitation = models.FloatField()  # 강수량

    def __str__(self):
        return f'{self.region_name} - {self.risk_level} ({self.forecast_date})'

class Feedback(models.Model):
    # 사용자와 관련된 필드
    name = models.CharField(max_length=100, verbose_name="Name")  # 사용자 이름
    email = models.EmailField(verbose_name="Email", blank=True, null=True)  # 이메일 (선택 사항)

    # 피드백 내용 관련 필드
    subject = models.CharField(max_length=200, verbose_name="Subject")  # 피드백 주제
    message = models.TextField(verbose_name="Message")  # 피드백 내용
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")  # 피드백 작성 날짜
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")  # 수정 날짜

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
        ordering = ['-created_at']  # 최신 피드백이 먼저 오도록 정렬

    def __str__(self):
        return f"{self.name} - {self.subject}"