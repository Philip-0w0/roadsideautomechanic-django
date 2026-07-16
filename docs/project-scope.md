# Project Scope — roadsideautomechanic

## Business objective
Replace the current Wix-based site with a custom-built workshop site 
that matches and extends its existing functionality — generating 
bookings for mechanical repairs, routine servicing, and 4x4 
modifications, while giving customers accounts, live availability, 
and service history.

## Target customers
- Existing customers migrating from the current Wix site
- Owners needing routine servicing or repairs
- 4x4 owners wanting modifications
- Touring and camping customers
- Trade / commercial vehicle owners
- Customers needing diagnostic work
- Customers wanting a pre-purchase inspection

## Primary actions
The website should get visitors to:
1. Call the workshop
2. Create an account and book a real, available time slot
3. Pay a deposit to confirm a booking
4. View services
5. View completed projects / gallery
6. Get directions
7. (Returning customers) View their saved vehicles and service history

## Success criteria (Definition of Done)
- All pages work on mobile and desktop
- A customer can register, log in, and save a vehicle to their account
- A customer can view real-time availability and book an actual open slot
- Double-booking the same slot is prevented
- A booking requires a deposit payment (via Stripe) to be confirmed
- Completed jobs can be logged against a vehicle and viewed by the 
  customer as service history
- A customer can only ever see their own vehicles and service records, 
  never another customer's — confirmed by an explicit test
- Every page has a real title and meta description
- Lighthouse performance score 90+ on mobile homepage
- Automated tests pass, including access-control tests
- Site is live on the real domain with HTTPS
- The Wix site is only retired after a full regression pass on 
  the new site confirms feature parity

## Included in Version 1 (expanded from original scope)
- Customer accounts (registration, login, password reset)
- Saved vehicles per customer
- Live calendar booking with real slot availability
- Deposit payments via Stripe for confirmed bookings
- Vehicle service history, workshop-logged and customer-viewable

## Explicitly excluded from Version 1
- Full online payment for entire jobs (deposits only — remaining 
  balance handled in person/by invoice as it is now)
- AI damage diagnosis
- Parts catalogue / inventory management
- Internal technician dashboard beyond the Django admin
- Mobile app
- Any Hafnix / lights / e-commerce content (separate project)
- Automated service-record generation on booking completion 
  (manual entry via admin for Version 1; automation is a 
  post-launch improvement once real usage patterns are known)

## Technical notes
Built with Django + PostgreSQL, deployed on Render. 
(Originally scoped in Next.js/TypeScript; switched to Django 
for better alignment with existing Python experience. Scope 
expanded from an initial 4-week static-content plan to a 
6-week plan after confirming the current live site already 
has customer accounts, calendar booking, and service history 
in active use.)

## Deposit policy
[To be finalized before Week 6, Day 35 — document here once decided:
flat amount vs. percentage, refundable vs. non-refundable, which 
service categories require a deposit.]
