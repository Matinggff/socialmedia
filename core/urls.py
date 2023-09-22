from django.urls import path
from core import views

app_name = "core"
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('upload/', views.upload, name='upload'),
    path('logout/', views.log_out, name='log_out'),
    path('like-post/<post_id>', views.like, name='like'),
    path('comment', views.comment, name='comment'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('setting/', views.setting, name='setting'),
    path('delete/<post_id>', views.delete, name='delete'),
]
