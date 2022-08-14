from django.urls import path
from blog.views import postlist, categorylist, postdetails

app_name = 'blog'

urlpatterns=[
   path('', postlist.as_view(), name='postlist'),
   path('category/', categorylist.as_view(), name ='category'),
   path('post/<int:pk>/', postdetails.as_view(), name='postdetails'),
   
]
