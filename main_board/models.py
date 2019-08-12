from django.db import models
from django.utils import timezone


class MarketIndex(models.Model):
    ticker = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'market_indices'

    def __str__(self):
        return self.ticker


class ValueUpdate(models.Model):
    market_index = models.ForeignKey(MarketIndex, on_delete=models.CASCADE)
    current_value = models.DecimalField(max_digits=10, decimal_places=2)
    points_change = models.DecimalField(max_digits=10, decimal_places=2)
    percent_change = models.DecimalField(max_digits=5, decimal_places=2)
    market_status = models.CharField(max_length=20, blank=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.market_index.name}: {self.updated_at.isoformat()}'
