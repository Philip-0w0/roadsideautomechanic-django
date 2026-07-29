from django import forms
from .models import BookingRequest, AvailabilitySlot
from accounts.models import Vehicle

class BookingForm(forms.ModelForm):
    vehicle = forms.ModelChoiceField(
        queryset=Vehicle.objects.none(),
        required=False,
        empty_label="+ Add a new vehicle",
        label="Vehicle",
    )
    slot = forms.ModelChoiceField(
        queryset=AvailabilitySlot.objects.none(),
        required=True,
        label="Choose a time",
        empty_label="Select an available time",
    )
    consent = forms.BooleanField(required=True, label="I consent to being contacted about this request")

    class Meta:
        model = BookingRequest
        fields = [
            'customer_name', 'email', 'phone', 'vehicle_make', 'vehicle_model',
            'vehicle_year', 'registration', 'service_category', 'description',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, user=None, available_slots=None, **kwargs):
        super().__init__(*args, **kwargs)

        if available_slots is not None:
            self.fields['slot'].queryset = available_slots

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