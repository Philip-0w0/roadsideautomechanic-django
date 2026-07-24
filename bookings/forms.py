from django import forms
from .models import BookingRequest
from accounts.models import Vehicle

class BookingForm(forms.ModelForm):
    vehicle = forms.ModelChoiceField(
        queryset=Vehicle.objects.none(),
        required=False,
        empty_label="+ Add a new vehicle",
        label="Vehicle",
    )
    consent = forms.BooleanField(required=True, label="I consent to being contacted about this request")

    class Meta:
        model = BookingRequest
        fields = [
            'customer_name', 'email', 'phone', 'vehicle_make', 'vehicle_model',
            'vehicle_year', 'registration', 'service_category', 'preferred_date', 'description',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.show_vehicle_dropdown = False
        if user is not None and user.is_authenticated and user.vehicles.exists():
            self.fields['vehicle'].queryset = user.vehicles.all()
            self.show_vehicle_dropdown = True
        else:
            del self.fields['vehicle']

        if self.show_vehicle_dropdown:
            self.fields['vehicle_make'].required = False
            self.fields['vehicle_model'].required = False
            self.fields['vehicle_year'].required = False