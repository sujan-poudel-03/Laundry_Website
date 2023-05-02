from django.urls import path
from laundry_app import views

urlpatterns = [
    path('', views.laundryHome , name='laundryIndexPage' ),
    path('pricing/', views.pricing, name='pricing'),
    path('branches/', views.branches, name='branches'),
    path('contact/', views.contact, name='contact'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
]

