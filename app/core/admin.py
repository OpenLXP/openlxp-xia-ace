from django.contrib import admin

from .models import (ReceiverEmailConfiguration, SenderEmailConfiguration,
                     XIAConfiguration, XISConfiguration)

# Register your models here.


@admin.register(XIAConfiguration)
class XIAConfigurationAdmin(admin.ModelAdmin):
    list_display = (
        'publisher',
        'source_metadata_schema',
        'source_target_mapping',
        'target_metadata_schema',
        'source_file',)
    fields = ['publisher',
              'source_metadata_schema',
              ('source_target_mapping',
               'target_metadata_schema',
               'source_file')]


@admin.register(XISConfiguration)
class XISConfigurationAdmin(admin.ModelAdmin):
    list_display = ('xis_api_endpoint',)
    fields = ['xis_api_endpoint']


@admin.register(ReceiverEmailConfiguration)
class ReceiverEmailConfigurationAdmin(admin.ModelAdmin):
    list_display = ('email_address',)


@admin.register(SenderEmailConfiguration)
class SenderEmailConfigurationAdmin(admin.ModelAdmin):
    list_display = ('sender_email_address',)