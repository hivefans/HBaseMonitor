from HBaseMonitor import settings
from HBaseMonitor.view import index, tableTps, tableStorageInfo, getTableTps, \
    getTableStorageInfo, showMasterInfo, showRegionServerLoad, getClusterAttr, \
    getClusterTps, getRegionServerInfo, getRegionInfo, getRegionList
from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HBaseMonitor.views.home', name='home'),
    # url(r'^HBaseMonitor/', include('HBaseMonitor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'css/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.STATICFILES_DIRS+'/css'}),
    url(r'js/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.STATICFILES_DIRS+'/js'}),
    url(r'img/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.STATICFILES_DIRS+'/img'}),
    url(r'fonts/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.STATICFILES_DIRS+'/fonts'}),
    ('^index/$',index),
    ('^show_table_tps/$',tableTps),
    ('^show_table_storage_info/$',tableStorageInfo),
    ('^show_master_info/$',showMasterInfo),
    ('^show_regionserver_load/$',showRegionServerLoad),
    
    ('^get_table_tps/$',getTableTps),
    ('^get_table_storage_info/$',getTableStorageInfo),
    ('^get_cluster_attr/$',getClusterAttr),
    ('^get_cluster_tps/$',getClusterTps),
    ('^get_regionserver_info/$',getRegionServerInfo),
    ('^get_region_info/$',getRegionInfo),
    ('^get_region_list/$',getRegionList),
)
