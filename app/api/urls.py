from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import WorkflowView

router = DefaultRouter()

app_name = 'api'

urlpatterns = [
    path('xia-workflow/', WorkflowView.as_view(), name='xia_workflow'),
    path('credit-data/', views.CreditDataView.as_view(),
         name='credit-data'),
]

# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html','xml'])
