from django.urls import path
from appone import views
#from django.conf.urls import url

app_name = 'appone'

urlpatterns=[
    path('',views.index,name='index'),
    path('cuisines',views.cuisines,name='cuisines'),
    path('restaurants',views.restaurants,name='restaurants'),
    path('top',views.top_cuisines,name='top'),
    path('dgrph',views.dgraph,name='dgraph'),
    path('rgraph',views.rgraph,name='rgraph'),
    path('avg_cost',views.avg_cost,name='avg_cost'),
    path('avg_cost2',views.avg_cost2,name='avg_cost2'),
    path('pie_chart',views.pie_chart,name='pie_chart'),
    path('about',views.about,name='about'),
    path('my_model',views.my_model,name='my_model'),
    path('form_page',views.form_page,name='form_page'),
    path('form2',views.form2,name='form2'),
    path('login',views.login,name='login'),
]
