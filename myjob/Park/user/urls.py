from . import views
from django.conf.urls import url

app_name = 'user'
urlpatterns = [
    url(r'^$', views.park_base, name='park_base'),
    url(r'^park_result/$', views.park_result, name='park_result'),
    url(r'^park_base_result_yuhua/$', views.park_base_result_yuhua, name='park_base_result_yuhua'),
    url(r'^park_base_result_pukou/$', views.park_base_result_pukou, name='park_base_result_pukou'),
    url(r'^park_base_result_gulou/$', views.park_base_result_gulou, name='park_base_result_gulou'),
    url(r'^result_del_all/$', views.result_del_all, name='result_del_all'),
    url(r'^result_sum/$', views.result_sum, name='result_sum'),
    url(r'^result_del/(?P<a_id>\d+)/$', views.result_del, name='result_del'),
    url(r'^message/$', views.message, name='message'),
    url(r'^message1/$', views.message1, name='message1'),
    url(r'^message2/$', views.message2, name='message2'),
    url(r'^message3/$', views.message3, name='message3'),

]
