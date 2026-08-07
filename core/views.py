from django.shortcuts import render

# Create your views here.
def home(request):
    featured_services = [
        {'title': 'Logbook Service', 'summary': "Manufacturer-schedule servicing to keep your warranty and vehicle history intact."},
        {'title': 'Diagnostics', 'summary': 'Accurate fault-finding for warning lights, unusual noises, or performance issues.'},
        {'title': 'General Repairs', 'summary': 'Mechanical repairs covering suspension, brakes, and everyday issues in one visit.'},
    ]
    return render(request, 'core/home.html', {'featured_services': featured_services})

    
def services(request):
    services_list = [
        {
            'title': 'Logbook Service',
            'summary': "Manufacturer-schedule servicing to keep your warranty and vehicle history intact.",
            'description': "Logbook servicing carried out to your vehicle's manufacturer schedule, covering the checks and maintenance required to keep your service history complete and warranty valid.",
            'cta': 'Book a logbook service',
        },
        {
            'title': 'Diagnostics',
            'summary': 'Accurate fault-finding for warning lights, unusual noises, or performance issues.',
            'description': "Proper diagnostic work to identify the actual cause of an issue rather than guessing — using the right tools to check engine, electrical, and mechanical faults. You get a clear explanation of what's wrong before we quote any repair.",
            'cta': 'Book a diagnostic',
        },
        {
            'title': 'General Repairs',
            'summary': 'Mechanical repairs covering suspension, brakes, and everyday issues in one visit.',
            'description': 'General mechanical repair work, from brake pads and suspension components to the smaller issues that come up between services — one straightforward repair visit instead of separate bookings for each fault.',
            'cta': 'Book a repair',
        },
        {
            'title': 'Battery Replacement',
            'summary': 'Battery testing and replacement to avoid unexpected breakdowns.',
            'description': 'We test battery health and replace batteries that are failing or at end of life, with the correct battery for your vehicle and usage — including higher-capacity options for vehicles running extra accessories.',
            'cta': 'Get your battery tested',
        },
        {
            'title': 'Vehicle Inspections',
            'summary': 'Thorough inspections for peace of mind or roadworthiness.',
            'description': 'A full inspection covering the key mechanical, safety, and wear points of a vehicle, with a clear written summary of anything that needs attention now or in the near future.',
            'cta': 'Book an inspection',
        },
        {
            'title': 'Vehicle Purchase Inspection',
            'summary': "An independent pre-purchase check before you buy.",
            'description': "A dedicated inspection for a vehicle you're considering buying, checking for hidden mechanical issues, prior damage, and upcoming maintenance costs — so you can negotiate or walk away with confidence.",
            'cta': 'Book a pre-purchase inspection',
        },
        {
            'title': 'Minor Mechanical Repairs',
            'summary': 'General mechanical repairs for everyday issues.',
            'description': 'Practical, honest repair work for the smaller mechanical issues that come up between services — done with a clear quote up front and no work started without your approval.',
            'cta': 'Get a repair quote',
        },
        {
            'title': 'Caravan and Trailer Maintenance',
            'summary': 'Servicing and repairs for caravans, trailers, and towing setups.',
            'description': 'Maintenance and repair for caravans and trailers, including wheel bearings, brakes, suspension, and towing electrical connections — important checks that are easy to overlook until something fails on the road.',
            'cta': 'Book caravan or trailer maintenance',
        },
        {
            'title': 'Roadside Assistance',
            'summary': "On-the-spot help when your vehicle won't start or won't move.",
            'description': "Roadside support for breakdowns — battery issues, minor mechanical faults, and get-you-going repairs — so you're not always stuck waiting for a tow truck.",
            'cta': 'Request roadside assistance',
        },
    ]
    return render(request, 'core/services.html', {'services': services_list})

def modifications(request):
    modifications_list = [
        {
            'title': 'Lift Kits',
            'summary': 'Suspension lift kit supply and installation for 4x4 vehicles.',
            'description': "Lift kits fitted to suit your vehicle's intended use — towing, touring, load-carrying, or off-road performance — with attention to how the change affects ride quality, alignment, and handling.",
            'cta': 'Ask about a lift kit',
        },
        {
            'title': 'Bull Bars',
            'summary': 'Bull bar supply and fitting for protection and accessory mounting.',
            'description': 'Bull bars fitted for front-end protection and to support mounted accessories like lighting and recovery points, matched to your specific vehicle.',
            'cta': 'Ask about bull bar fitting',
        },
        {
            'title': 'Snorkels',
            'summary': 'Snorkel fitting for improved water fording depth and cleaner air intake.',
            'description': 'Snorkels fitted to raise the air intake point, useful for water crossings and reducing dust ingestion in harsh off-road conditions.',
            'cta': 'Ask about snorkel fitting',
        },
        {
            'title': 'Roof Racks',
            'summary': 'Roof rack supply and fitting for extra storage and touring capacity.',
            'description': "Roof racks fitted securely and rated for your intended load, whether that's recovery gear, camping equipment, or general touring storage.",
            'cta': 'Ask about roof rack fitting',
        },
        {
            'title': 'Other Requests',
            'summary': 'Have something specific in mind? Ask us.',
            'description': "If you're after a 4x4 modification not listed here, get in touch and describe what you need — we'll let you know if it's something we can help with.",
            'cta': 'Ask about your modification',
        },
    ]
    return render(request, 'core/modifications.html', {'modifications': modifications_list})

def gallery(request):
    projects = [
        {
            'title': 'Example Project',
            'vehicle': '2020 Toyota Hilux',
            'summary': 'Suspension upgrade and touring setup.',
            'image': 'core/images/placeholder-1.jpg',
        },
        # Add real entries here as photos become available.
        # Each needs: title, vehicle, summary, and an image path
        # relative to your static/ folder.
    ]
    return render(request, 'core/gallery.html', {'projects': projects})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def privacy(request):
    return render(request, 'core/privacy.html')

def terms(request):
    return render(request, 'core/terms.html')