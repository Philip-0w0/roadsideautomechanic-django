from django.shortcuts import render

# Create your views here.
def home(request):
    featured_services = [
        {'title': 'General Servicing', 'summary': 'Routine servicing to keep your vehicle running reliably and safely.'},
        {'title': 'Diagnostics', 'summary': 'Accurate fault-finding for warning lights, unusual noises, or performance issues.'},
        {'title': 'Brake Repairs', 'summary': 'Brake inspection, repair, and replacement for safe stopping performance.'},
    ]
    return render(request, 'core/home.html', {'featured_services': featured_services})

def services(request):
    services_list = [
        {
            'title': 'General Servicing',
            'summary': 'Routine servicing to keep your vehicle running reliably and safely.',
            'description': "Logbook and general servicing covering the checks and maintenance your vehicle needs to stay reliable, avoid costly breakdowns, and hold its value. We explain what's being done and why before any work starts.",
            'cta': 'Book a service',
        },
        {
            'title': 'Diagnostics',
            'summary': 'Accurate fault-finding for warning lights, unusual noises, or performance issues.',
            'description': 'Proper diagnostic work to identify the actual cause of an issue rather than guessing — using the right tools to check engine, electrical, and mechanical faults. You get a clear explanation of what\'s wrong before we quote any repair.',
            'cta': 'Book a diagnostic',
        },
        {
            'title': 'Brake Repairs',
            'summary': 'Brake inspection, repair, and replacement for safe stopping performance.',
            'description': 'From pad and rotor replacement to full brake system checks, we make sure your vehicle stops the way it should. Safety-critical work, done properly and explained clearly.',
            'cta': 'Book a brake check',
        },
        {
            'title': 'Battery Replacement',
            'summary': 'Battery testing and replacement to avoid unexpected breakdowns.',
            'description': 'We test battery health and replace batteries that are failing or at end of life, with the correct battery for your vehicle and usage — including higher-capacity options for vehicles running extra accessories.',
            'cta': 'Get your battery tested',
        },
        {
            'title': 'Vehicle Inspections',
            'summary': 'Thorough inspections for peace of mind, roadworthiness, or pre-purchase decisions.',
            'description': 'A full inspection covering the key mechanical, safety, and wear points of a vehicle, with a clear written summary of anything that needs attention now or in the near future.',
            'cta': 'Book an inspection',
        },
        {
            'title': 'Suspension Checks',
            'summary': 'Suspension inspection and repair for comfort, handling, and safety.',
            'description': 'We check shocks, springs, and steering components for wear or damage, particularly important for vehicles that tow, carry heavy loads, or spend time off-road.',
            'cta': 'Book a suspension check',
        },
        {
            'title': 'Minor Mechanical Repairs',
            'summary': 'General mechanical repairs for everyday issues.',
            'description': 'Practical, honest repair work for the smaller mechanical issues that come up between services — done with a clear quote up front and no work started without your approval.',
            'cta': 'Get a repair quote',
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