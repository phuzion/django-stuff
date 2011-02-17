from django.conf.urls.defaults import *
from django.views.generic import list_detail
from members.models import Member
from links.models import Link

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

member_info = {
    "queryset" : Member.objects.all(),
}

link_info = {
    "queryset" : Link.objects.all(),
}

urlpatterns = patterns('',
    # Example:
    # (r'^w8updbeta/', include('w8updbeta.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^links/$', list_detail.object_list, link_info),
#    (r'^members', 'members.views.index'),
    (r'^members/$', list_detail.object_list, member_info)
)
