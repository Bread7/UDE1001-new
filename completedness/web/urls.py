from django.urls import path 
from . import views

# namespace for views usage
app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("success/", views.success, name='success'),
    # path('<int:id>/', views.detail, name='detail'),

    #Auth requests
    path("register/", views.register, name="register"),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),

    #User requests
    path('authLogon/', views.logonIndex, name='authLogon'),
    path('seminar/', views.getSeminar, name='getSeminar'),
    path('postSeminar/', views.postSeminar, name='postSeminar'),
    path('activity/', views.getActivity, name='getActivity'),
    # path('postActivity/', views.postActivity, name='postActivity'),
    path('connections', views.getConnections, name='getConnections'),
]
