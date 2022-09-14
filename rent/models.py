from sqlite3 import Date
from django.db import models
from account.models import User


class rent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rent_date = models.DateField(auto_now_add=True)
    rentmonth = models.CharField(max_length=30)
    rent_amount = models.FloatField()
    bijli_bill = models.FloatField()
    other_amount = models.FloatField(blank=True, default=0.00,)
    other_commnet = models.CharField(blank=True, max_length=200)

    @property
    def total_amount(self):
        return self.rent_amount + self.bijli_bill + self.other_amount
    