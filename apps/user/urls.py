from django.conf.urls import url
from user import views
from user.views import RegisterView
from user.views import ActiveView
from user.views import LoginView, UserInfoView, UserOrderView, AddressView
from django.contrib.auth.decorators import  login_required
urlpatterns = [
    # url(r'^register$', views.register, name='register'),
    # url(r'^register_handle$', views.register_handle, name='register_handle')
    url(r'^register$', RegisterView.as_view(), name='register'),  # 注册
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^$', UserInfoView.as_view(), name='user'),
    url(r'^order&', UserOrderView.as_view(), name='order'),
    url(r'^address$', AddressView.as_view(), name='address')
]
