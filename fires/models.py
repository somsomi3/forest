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
