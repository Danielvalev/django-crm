from django.urls import path
from .views import lead_list, lead_detail, lead_create, lead_update, lead_delete, LeadListView, LeadDetailView, \
    LeadCreateView, LeadUpdateView, LeadDeleteView, AssignAgentView, CategoryListView

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),  # CBV
    # path('', lead_list, name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),  # CBV
    # path('<int:pk>/', lead_detail, name='lead-detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),  # CBV
    # path('<int:pk>/update/', lead_update, name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),  # CBV
    # path('<int:pk>/delete/', lead_delete, name='lead-delete'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),  # CBV
    # path('create/', lead_create, name='lead-create'),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='assign-agent'),
    path('category-list/', CategoryListView.as_view(), name='category-list'),

]
