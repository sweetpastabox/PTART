from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^flag/(?P<pk>[0-9]+)/$', views.flag),
    url(r'^flag/(?P<pk>[0-9]+)/complete/$', views.markFlagAsDone),
    url(r'^flags/$', views.flags),
    url(r'^hit/(?P<pk>[0-9]+)/$', views.hit),
    url(r'^hit/(?P<pk>[0-9]+)/cvss/$', views.cvss_hit),
    url(r'^hit/(?P<pk>[0-9]+)/comments/$', views.comments),
    url(r'^hits/$', views.hits),
    url(r'^label/(?P<pk>[0-9]+)/$', views.label),
    url(r'^labels/$', views.labels),
    url(r'^comment/(?P<pk>[0-9]+)/$', views.comment),
    url(r'^screenshot/(?P<pk>[0-9]+)/$', views.screenshot),
    url(r'^screenshot/png/(?P<pk>[0-9]+)/$', views.screenshot_raw),
    url(r'^screenshots/$', views.screenshots),
    url(r'^attachment/(?P<pk>[0-9]+)/$', views.attachment),
    url(r'^attachment/raw/(?P<pk>[0-9]+)/$', views.attachment_raw),
    url(r'^attachments/$', views.attachments),
    url(r'^host/(?P<pk>[0-9]+)/$', views.host),
    url(r'^hosts/$', views.hosts),
    url(r'^service/(?P<pk>[0-9]+)/$', views.service),
    url(r'^services/$', views.services),
    url(r'^cvss/$', views.cvss),
    url(r'^assessment/(?P<pk>[0-9]+)/$', views.assessment),
    url(r'^assessments/$', views.assessments),
    url(r'^project/(?P<pk>[0-9]+)/$', views.project),
    url(r'^project/(?P<pk>[0-9]+)/burp$', views.project_burp_configuration),
    url(r'^project/(?P<pk>[0-9]+)/xlsx$', views.project_xlsx),
    url(r'^projects/$', views.projects),
    url(r'^template/(?P<pk>[0-9]+)/$', views.template),
    url(r'^templates/$', views.templates),
    url(r'^case/(?P<pk>[0-9]+)/$', views.case),
    url(r'^cases/$', views.cases),
    url(r'^module/(?P<pk>[0-9]+)/$', views.module),
    url(r'^module/(?P<pk>[0-9]+)/load/(?P<assessmentId>[0-9]+)/$', views.load_module),
    url(r'^modules/$', views.modules),
    url(r'^methodology/(?P<pk>[0-9]+)/$', views.methodology),
    url(r'^methodologies/$', views.methodologies),
]
urlpatterns = format_suffix_patterns(urlpatterns)
