from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views

from fin_manager.categories.views import entry_editor, category_editor, categories_list, \
    delete_category, update_entry, delete_entry, expenses_by_month

urlpatterns = [
    url(r'^$', entry_editor, name='home'),
    url(r'^category_editor/new_category/$', category_editor, name='category_editor'),
    url(r'^category_editor/(?P<category_id>[0-9]+)/$', category_editor, name='category_editor'),
    url(r'^update_entry/(?P<entry_id>[0-9]+)/$', update_entry, name='update_entry'),
    url(r'^delete_category/(?P<category_id>[0-9]+)/$', delete_category, name='delete_category'),
    url(r'^delete_entry/(?P<entry_id>[0-9]+)/$', delete_entry, name='delete_entry'),
    url(r'^info_manager/$', categories_list, name='info_manager'),
    url(r'^api/expenses_by_month', expenses_by_month, name='expenses_by_month'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('fin_manager.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
