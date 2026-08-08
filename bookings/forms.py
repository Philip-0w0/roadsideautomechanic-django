from django import forms
from .models import BookingRequest, AvailabilitySlot
from accounts.models import Vehicle

SERVICE_CHOICES = [
    ('', 'Select a service'),
    ('Logbook Service', 'Logbook Service'),
    ('Diagnostics', 'Diagnostics'),
    ('General Repairs', 'General Repairs'),
    ('Battery Replacement', 'Battery Replacement'),
    ('Vehicle Inspections', 'Vehicle Inspections'),
    ('Vehicle Purchase Inspection', 'Vehicle Purchase Inspection'),
    ('Minor Mechanical Repairs', 'Minor Mechanical Repairs'),
    ('Caravan and Trailer Maintenance', 'Caravan and Trailer Maintenance'),
    ('Roadside Assistance', 'Roadside Assistance'),
    ('Lift Kits', '4x4 — Lift Kits'),
    ('Bull Bars', '4x4 — Bull Bars'),
    ('Snorkels', '4x4 — Snorkels'),
    ('Roof Racks', '4x4 — Roof Racks'),
    ('Other', 'Other'),
]


class BookingForm(forms.ModelForm):
    service_category = forms.ChoiceField(choices=SERVICE_CHOICES, label='Service')

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

        # Only name, email, phone are genuinely required — everything else optional
        self.fields['vehicle_make'].required = False
        self.fields['vehicle_model'].required = False
        self.fields['vehicle_year'].required = False
        self.fields['registration'].required = False
        self.fields['description'].required = False

    def clean(self):
        cleaned_data = super().clean()
        service = cleaned_data.get('service_category')
        description = cleaned_data.get('description')

        if service == 'Other' and not description:
            self.add_error('description', 'Please briefly describe what you need.')

        return cleaned_data