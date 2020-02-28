from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Client

class ClientResource(resources.ModelResource):

    class Meta:
        model = Client
        
class ClientAdmin(ImportExportModelAdmin):
    resource_class = ClientResource

admin.site.register(Client, ClientAdmin)