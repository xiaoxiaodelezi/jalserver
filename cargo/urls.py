from django.urls import path
from . import views

urlpatterns=[
    path('',views.cgo_homepage,name='cgo_homepage'),
    path('desk_homepage',views.cgo_desk_homepage,name='cgo_desk_homepage'),
    path('desk_importspecialcgo_upload',views.cgo_desk_importspecialcgo_upload,name='desk_importspecialcgo_upload'),
    path('desk_importspecialcgo_result',views.cgo_desk_importspecialcgo_result,name='desk_importspecialcgo_result'),
    path('fr_homepage',views.cgo_fr_homepage,name='cgo_fr_homepage'),
    path('fr_cargosalesreport_upload',views.cgo_fr_cargosalesreport_upload,name='fr_cargosalesreport_upload'),
    path('fr_cargosalesreport_result',views.cgo_fr_cargosalesreport_result,name='fr_cargosalesreport_result'),
    path('traffic_homepage',views.cgo_traffic_homepage,name='cgo_traffic_homepage'),
    path('traffic_scsforotherairlines_upload',views.cgo_traffic_scsforotherairlines_upload,name='cgo_traffic_scsforotherairlines_upload'),
    path('traffic_scsforotherairlines_result',views.cgo_traffic_scsforotherairlines_result,name='cgo_traffic_scsforotherairlines_result'),

]