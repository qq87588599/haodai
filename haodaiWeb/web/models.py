from __future__ import unicode_literals

from django.db import models


class Pros(models.Model):
    avatar_img = models.CharField(max_length=512, blank=True, null=True)
    url_loc = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    money_type = models.CharField(max_length=512, blank=True, null=True)
    product_url = models.CharField(max_length=512, blank=True, null=True)
    starts = models.CharField(max_length=512, blank=True, null=True)
    all_cost = models.CharField(max_length=512, blank=True, null=True)
    supply = models.CharField(max_length=512, blank=True, null=True)
    rate = models.CharField(max_length=512, blank=True, null=True)
    instruction = models.CharField(max_length=512, blank=True, null=True)
    cid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pros'


class Details(models.Model):
    kid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=512, blank=True, null=True)
    money = models.CharField(max_length=100, blank=True, null=True)
    money_range = models.CharField(max_length=100, blank=True, null=True)
    deadline_range = models.CharField(max_length=100, blank=True, null=True)
    supply_type = models.CharField(max_length=100, blank=True, null=True)
    give_type = models.CharField(max_length=512, blank=True, null=True)
    deadline = models.CharField(max_length=100, blank=True, null=True)
    give_permonth = models.CharField(max_length=100, blank=True, null=True)
    total_cost = models.CharField(max_length=100, blank=True, null=True)
    cost_des = models.CharField(max_length=100, blank=True, null=True)
    bank_title = models.CharField(max_length=100, blank=True, null=True)
    type_title = models.CharField(max_length=100, blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    product_url = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'details'