from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('home',views.home,name='home'),
    path('women',views.women,name='women'),
    path('men',views.men,name='men'),
    path('arrivals',views.arrivals,name='arrivals'),
    path('arrivaladd',views.add,name='arrivaladd'),
    path('arrivaledit/<int:id>',views.edit,name='arrivaledit'),
    path('arrivaldel/<int:id>',views.remove,name='arrivaldel'),
    path('login',views.loginuser,name='login'),
    path('menoffice',views.menoffice,name='menoffice'),
    path('menwallet',views.menwallet,name='menwallet'),
    path('detail/<name>',views.detail,name='detail'),
    path('wallet',views.wallet,name='wallet'),
    path('sling',views.sling,name='sling'),
    path('tote',views.tote,name='tote'),
    path('backpack',views.backpack,name='backpack'),
    path('office',views.office,name='office')
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)