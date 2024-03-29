from django.urls import path
from . import views

urlpatterns=[
    path('cgo_homepage',views.cgo_homepage,name='cgo_homepage'),
    path('cgo_login',views.cgo_login,name='cgo_login'),
    path('desk_homepage',views.cgo_desk_homepage,name='cgo_desk_homepage'),
    path('desk_importspecialcgo_upload',views.cgo_desk_importspecialcgo_upload,name='desk_importspecialcgo_upload'),
    path('desk_importspecialcgo_result',views.cgo_desk_importspecialcgo_result,name='desk_importspecialcgo_result'),
    path('fr_homepage',views.cgo_fr_homepage,name='cgo_fr_homepage'),
    path('fr_cargosalesreport_upload',views.cgo_fr_cargosalesreport_upload,name='fr_cargosalesreport_upload'),
    path('fr_cargosalesreport_result',views.cgo_fr_cargosalesreport_result,name='fr_cargosalesreport_result'),
    path('traffic_homepage',views.cgo_traffic_homepage,name='cgo_traffic_homepage'),
    path('traffic_scsforotherairlines_upload',views.cgo_traffic_scsforotherairlines_upload,name='cgo_traffic_scsforotherairlines_upload'),
    path('traffic_scsforotherairlines_result',views.cgo_traffic_scsforotherairlines_result,name='cgo_traffic_scsforotherairlines_result'),
    path('desk_uldstorage_result',views.cgo_desk_uldstorage_result,name='desk_uldstorage_result'),
    path('ic_homepage',views.cgo_ic_homepage,name='ic_homepage'),
    path('ic_crosscheck_upload',views.cgo_ic_crosscheck_upload,name='ic_crosscheck_upload'),
    path('ic_crosscheck_result',views.cgo_ic_crosscheck_result,name='ic_crosscheck_result'),
    path('traffic_notallowedcargo_upload',views.cgo_traffic_notallowedcargo_upload,name='traffic_notallowedcargo_upload'),
    path('traffic_notallowedcargo_result',views.cgo_traffic_notallowedcargo_result,name='traffic_notallowedcargo_result'),
    path('fr_cargosalesreport_pdfexcel_upload',views.cgo_fr_cargosalesreport_pdfexcel_upload,name='fr_cargosalesreport_pdfexcel_upload'),
    path('fr_cargosalesreport_pdfexcel_result',views.cgo_fr_cargosalesreport_pdfexcel_result,name='fr_cargosalesreport_pdfexcel_result'),
    path('fr_cargosalesreport_excelexcel_upload',views.cgo_fr_cargosalesreport_excelexcel_upload,name='fr_cargosalesreport_excelexcel_upload'),
    path('fr_cargosalesreport_excelexcel_result',views.cgo_fr_cargosalesreport_excelexcel_result,name='fr_cargosalesreport_excelexcel_result'),
    path('fr_awbdistribution_upload',views.cgo_fr_awbdistribution_upload,name='fr_awbdistribution_upload'),
    path('fr_awbdistribution_result',views.cgo_fr_awbdistribution_result,name='fr_awbdistribution_result'),
]