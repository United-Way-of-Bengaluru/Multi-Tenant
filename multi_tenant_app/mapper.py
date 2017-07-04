"""Maps a request to a tenant using the first part of the hostname.

For example:
  foo.example.com:8000 -> foo
  bar.baz.example.com -> bar 

This is a simple example; you should probably verify tenant names
are valid before returning them, since the returned tenant name will
be issued in a `USE` SQL query.
"""
 
from db_multitenant import mapper
from django.conf import settings
 
class TenantMapper(mapper.TenantMapper):
    def get_tenant_name(self, request):
        """Takes the first part of the hostname as the tenant"""
        hostname = request.get_host().split(':')[0].lower()
        return hostname.split('.')[0]
 
    def get_dbname(self, request):
        SUPER_ADMIN_HOST = getattr(settings, "SUPER_ADMIN_HOST", None)
        if SUPER_ADMIN_HOST == self.get_tenant_name(request):
            dbname = getattr(settings, "SUPER_DATABASE_NAME", None)
            return dbname
        return 'tenant_%s' % self.get_tenant_name(request)
 
    def get_cache_prefix(self, request):
        return 'tenant_%s' % self.get_tenant_name(request)