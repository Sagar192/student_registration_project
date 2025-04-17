from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('new-student/', views.CreateNewStudent.as_view(), name='new_student'),
    path('new-admission/', views.CreateAdmission.as_view(),name='new_admission'),
    path('fee-data/', views.CreateFeePaid.as_view(),name='fee_data'),
    path('admission-list/',views.AdmissionListView.as_view(),name='admission_list'),
    path('student-details/<str:pk>/',views.StudentDetailView.as_view(),name='student_detail'),
    path('student-report/<int:pk>/', views.StudentPaymentDetailView.as_view(), name='student_report'),
    path('update/<str:pk>/',views.UpdateDetailsView.as_view(),name='update_details'),
    path('student/<str:student_pk>/add-fee/', views.FeePaidCreateView.as_view(), name='add_fee'),
    path('admission/<int:pk>/delete/', views.AdmissionDeleteView.as_view(), name='admission_delete')
]