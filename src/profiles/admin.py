# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import UserPurchase

# Register your models here.

class UserPurchaseAdmin(admin.ModelAdmin):
    class Meta:
        model = UserPurchase

admin.site.register(UserPurchase, UserPurchaseAdmin)
