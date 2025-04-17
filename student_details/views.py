from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import Students,Admission,FeePaid
from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from .forms import StudentForm,AdmissionForm, FeePaidForm
from django.views.generic import (CreateView,
                                  ListView,
                                  TemplateView,
                                  DeleteView
                                  )
def home(request):
    return render(request,'student_details/home.html')

class CreateNewStudent(CreateView):
    model = Students
    fields = ["name","contact_no","address","gender","highest_education"]


    def form_valid(self, form):
        student=form.save()
        messages.success(self.request,f'student data of {student.name} is created succesfully..')
        return redirect('home')


class CreateAdmission(CreateView):
    model = Admission
    fields = ["student","course_joined","joining_date","completion_date","course_status","course_fee",]

    def form_valid(self, form):
        admiss = form.save()
        messages.success(self.request,f"Admission details of {admiss.student} is created succesfully..")
        return redirect('home')

class CreateFeePaid(CreateView):
    model = FeePaid
    fields = ["admission","fee_paid","payment_mode","paid_to","fee_paid_date"]

    def form_valid(self, form):
        student=form.save()
        messages.success(self.request,f'Fee data of {student.admission} is created succesfully..')
        return redirect('home')

class AdmissionListView(ListView):
    model = Admission
    template_name = 'student_details/admission_list.html'
    context_object_name = 'admissions'


    def get_queryset(self):
        return Admission.objects.select_related('student').all()

    # def get(self, request, *args, **kwargs):
    #     messages.info(request, "This is a test message from the list view.")
    #     return super().get(request, *args, **kwargs)



class StudentDetailView(View):
    template_name = 'student_details/student_detail.html'

    def get(self, request, pk):
        student = get_object_or_404(Students, pk=pk)
        admission = get_object_or_404(Admission, student=student)
        context = {
            'student': student,
            'admission': admission
        }
        return render(request, self.template_name, context)


class StudentPaymentDetailView(TemplateView):
    template_name = 'student_details/student_report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        admission_id = self.kwargs.get('pk')

        # Getting the admission object with respective student
        admission = get_object_or_404(Admission.objects.select_related('student'), pk=admission_id)
        student = admission.student

        # Get fee records of the respective admission student
        fee_records = FeePaid.objects.filter(admission=admission).order_by('fee_paid_date')
        total_fee_paid = fee_records.aggregate(total=Sum('fee_paid'))['total'] or 0
        remaining_amt_to_pay = max(0, admission.course_fee - total_fee_paid)

        context.update({
            'student': student,
            'admission': admission,
            'fee_record_details': fee_records,
            'total_fee_paid': total_fee_paid,
            'remaining_amt_to_pay': remaining_amt_to_pay,
            'title': "Student Payment History"
        })

        return context



class UpdateDetailsView(View):
    template_name = 'student_details/update_details.html'

    def get(self, request, pk):
        # Getting student and admission instance
        student = get_object_or_404(Students, pk=pk)
        admission = Admission.objects.get(student=student)

        #we pass the student details to their respective forms (instance= 'it is used to get pre fetched details')
        student_form = StudentForm(instance=student)
        admission_form = AdmissionForm(instance=admission)

        #rendering the current data to the template
        return render(request, self.template_name, {
            'student_form': student_form,
            'admission_form': admission_form,
        })

    def post(self, request, pk):
        student = get_object_or_404(Students, pk=pk)
        admission = Admission.objects.get(student=student)

        #binding the submitted data to forms and to the object using instances
        student_form = StudentForm(request.POST, instance=student)
        admission_form = AdmissionForm(request.POST, instance=admission)

        # save the data to model if it is valid
        if student_form.is_valid() and admission_form.is_valid():
            student_form.save()
            admission_form.save()
            messages.success(request, "Student and admission details updated successfully.")
            return redirect('home')  # Or redirect to student detail page

        return render(request, self.template_name, {
            'student_form': student_form,
            'admission_form': admission_form,
        })

class FeePaidCreateView(View):
    template_name = 'student_details/add_fee.html'

    def get(self, request, student_pk):
        student = get_object_or_404(Students, pk=student_pk)
        admission = get_object_or_404(Admission, student=student)
        form = FeePaidForm()
        return render(request, self.template_name, {'form': form, 'student': student})

    def post(self, request, student_pk):
        student = get_object_or_404(Students, pk=student_pk)
        admission = get_object_or_404(Admission, student=student)

        form = FeePaidForm(request.POST)
        if form.is_valid():
            fee_paid = form.save(commit=False)
            fee_paid.admission = admission
            fee_paid.save()
            messages.success(request, "Fee payment recorded successfully.")
            return redirect('home')

        return render(request, self.template_name, {'form': form, 'student': student})





class AdmissionDeleteView(DeleteView):
    model = Admission
    template_name = 'student_details/admission_confirm_delete.html'
    success_url = reverse_lazy('admission_list')  # Redirect after deletion
    success_message = "Admission for %(student_name)s deleted successfully"  # Success message format

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        student_name = self.object.student.name
        messages.success(self.request, self.success_message % {'student_name': student_name})
        return super(AdmissionDeleteView, self).delete(request, *args, **kwargs)

