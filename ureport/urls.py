from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import permission_required, login_required
from django.conf import settings
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# javascript translation packages
js_info_dict = {
    'packages': (),  # this is empty due to the fact that all translation are in one folder
}

urlpatterns = patterns('',
    url(r'^', include('ureport.public.urls')),
    url(r'^manage/', include('ureport.admins.urls')),
    url(r'^manage/', include('dash.orgs.urls')),
    url(r'^manage/', include('dash.dashblocks.urls')),
    url(r'^manage/', include('dash.stories.urls')),
    url(r'^manage/', include('ureport.polls.urls')),
    url(r'^manage/', include('dash.categories.urls')),
    url(r'^manage/', include('ureport.news.urls')),
    url(r'^manage/', include('ureport.jobs.urls')),
    url(r'^manage/', include('ureport.countries.urls')),
    url(r'^manage/', include('ureport.assets.urls')),
    url(r'^users/', include('dash.users.urls')),
    url(r'^manage/', include('smartmin.csv_imports.urls')),
    url(r'^api/$', RedirectView.as_view(pattern_name='django.swagger.base.view', permanent=False)),

    url(r'^api/v1/', include('ureport.api.urls')),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = patterns('',
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
