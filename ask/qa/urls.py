from django.conf.urls import url, include

from qa.views import test, new_questions_list, popular_questions_list, question_details, ask, answer_add

urlpatterns = [
    url(r'^$', new_questions_list, name='home'),
    url(r'^login/$', test, name='login'),
    url(r'^signup/$', test, name='signup'),
    url(r'^question/(\d+)/$', question_details, name='question'),
    url(r'^ask/$', ask, name='ask'),
    url(r'^popular/$', popular_questions_list, name='popular'),
    url(r'^new/$', new_questions_list, name='new_questions_list'),
    url(r'^answer/$', answer_add, name='answer'),
]
