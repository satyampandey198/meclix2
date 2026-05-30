import os
import re

workspace_dir = r"c:\Users\Admin\Desktop\meclix2"

def get_icon(name):
    name_l = name.lower()
    if any(k in name_l for k in ['employee', 'user', 'driver', 'visitor', 'technician', 'contractor']):
        # User icon
        return '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'
    elif any(k in name_l for k in ['security', 'compliance', 'audit', 'ehs', 'safety']):
        # Shield icon
        return '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.66 9.7a1 1 0 0 1-.68 0C7.5 20.5 4 18 4 13V6a1 1 0 0 1 .76-.97l8-2a1 1 0 0 1 .48 0l8 2A1 1 0 0 1 20 6v7z"/></svg>'
    elif any(k in name_l for k in ['finance', 'procurement', 'dollar']):
        # Dollar icon
        return '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" x2="12" y1="2" y2="22"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>'
    elif any(k in name_l for k in ['architect', 'consultant', 'designer']):
        # Compass icon
        return '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m16.2 7.8-2 2-2.8 2.8-2 2 4 4 2-2 2.8-2.8 2-2-4-4z"/></svg>'
    else:
        # Briefcase icon
        return '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="7" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>'

def get_slug(name):
    slug = name.lower()
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    return slug.strip('-')

def apply_footer(content):
    # Clean up any legacy or duplicate footer comments first
    content = re.sub(r'\s*<!--\s*={5,}\s*FOOTER.*?\s*={5,}\s*-->', '', content, flags=re.DOTALL | re.IGNORECASE)

    footer_html = """  <!-- ==========================================================================
       FOOTER
       ========================================================================== -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="logo-link" style="margin-bottom: 20px;">
            <img src="assets/images/new_logo.png" alt="Meclix Mechatronix" style="max-height: 48px; width: auto; display: block;">
          </div>
          <p>Meclix Mechatronix delivers access-controlled storage and asset management solutions for modern enterprises. Backed by Smarti Electronics Systems Pvt. Ltd., with over 25 years of experience.</p>
          <div class="footer-social-icons" style="margin-top: 20px; display: flex; gap: 12px;">
            <a href="https://www.facebook.com" target="_blank" style="width: 36px; height: 36px; background: #ffffff; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #086ad8; transition: all 0.3s ease;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-facebook"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
            <a href="https://www.instagram.com" target="_blank" style="width: 36px; height: 36px; background: #ffffff; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #086ad8; transition: all 0.3s ease;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-instagram"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/></svg></a>
            <a href="https://www.linkedin.com" target="_blank" style="width: 36px; height: 36px; background: #ffffff; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #086ad8; transition: all 0.3s ease;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-linkedin"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/></svg></a>
          </div>
        </div>
        <div class="footer-col">
          <h5>Useful Links</h5>
          <ul class="footer-links">
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="lockers.html">ArcaKnox System</a></li>
            <li><a href="keyknox.html">KeyKnox System</a></li>
            <li><a href="javascript:void(0);" class="btn-consultation-trigger">Contact Us</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Our Products</h5>
          <ul class="footer-links">
            <li><a href="lockers.html">ArcaKnox System Smart Locker</a></li>
            <li><a href="keyknox.html">KeyKnox - Key Management</a></li>
            <li><a href="software.html">ArcaKnox Shield and KeyKnox Shield</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Contact Information</h5>
          <ul class="footer-links-contact" style="list-style: none;">
            <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 10px;">
              <span style="color: #086ad8; display: flex; align-items: center; min-width: 16px;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-phone"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg></span>
              <a href="tel:+919876543210" style="color: rgba(255, 255, 255, 0.6); font-size: 0.9rem;">+91 98765 43210</a>
            </li>
            <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 10px;">
              <span style="color: #086ad8; display: flex; align-items: center; min-width: 16px;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-mail"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg></span>
              <a href="mailto:info@meclix.in" style="color: rgba(255, 255, 255, 0.6); font-size: 0.9rem;">info@meclix.in</a>
            </li>
            <li style="margin-bottom: 12px; display: flex; align-items: start; gap: 10px;">
              <span style="color: #086ad8; display: flex; align-items: center; min-width: 16px; margin-top: 4px;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-map-pin"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg></span>
              <a href="https://maps.google.com/?q=Bangalore,Karnataka,India" target="_blank" style="color: rgba(255, 255, 255, 0.6); font-size: 0.9rem; line-height: 1.4;">Bangalore, Karnataka, India</a>
            </li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Meclix Mechatronix. All rights reserved. Backed by Smarti Electronics Systems Pvt. Ltd.</p>
        <p>India-First · SEO Optimised · AI Optimised</p>
      </div>
    </div>
  </footer>"""

    # Replace colophon/Elementor footer structure first (for index.html)
    if '<footer id="colophon"' in content:
        start_idx = content.find('<footer id="colophon"')
        end_idx = content.find('</footer>', start_idx)
        # Find outer footer closing tag
        end_idx = content.find('</footer>', end_idx + 9) + 9
        if start_idx != -1 and end_idx != -1:
            return content[:start_idx] + footer_html + content[end_idx:]

    # Replace standard footer
    if '<footer class="site-footer">' in content:
        start_idx = content.find('<footer class="site-footer">')
        end_idx = content.find('</footer>', start_idx) + 9
        if start_idx != -1 and end_idx != -1:
            return content[:start_idx] + footer_html + content[end_idx:]

    return content

# Clean benefits from Draft content mapping
benefits_data = {
    "employee": [
        ("Employees", 
         "Self-service access via Card, Biometric, PIN or Mobile App — eliminating dependency on staff assistance. Consistent locker availability across shift through automated allocation. Reduces reliance on padlock keys or shared combinations. Personal belongings are securely stored for the duration of use, with tamper alerts for continuous monitoring."),
        ("HR/Admin / Facility Managers",
         "Automated locker allocation eliminates manual assignment requests. Provides a real time digital record of locker usage per employee removing need for manual logging. Release of lockers on employee exit or end of contract minimizes the need for physical key collection during exit / off-boarding. Enables real-time visibility of locker status across floor and locations. Generates alerts for tampering, forced-access, and non-released lockers."),
        ("Finance & Compliance",
         "Eliminates recurring costs associated with lost keys, damaged locks, and emergency lock replacements. Asset usage reports support internal audits and compliance requirements. Reduces risk exposure from unaccounted access to employee storage areas. Maintains a chain-of-custody for all stored assets."),
        ("Senior Management",
         "Provides operational visibility across all locations through a centralised management platform. Strengthens access control governance through secure and accountable storage systems. Supports organisational efficiency through standardised processes and reduced manual intervention. Scales efficiently with organisational growth, without a proportional increase in administrative effort."),
        ("Architects, Interior Designers & Consultants",
         "Vertical locker configurations optimise floor space, enabling flexible and open layout planning without compromising storage capacity. Clean, modular locker systems integrate seamlessly into modern office environments, with configurable finishes and dimensions that align with the overall design language. Eliminates the need to design dedicated, oversized storage rooms by making efficient use of corridor walls, lobby recesses, and underutilised vertical surfaces. Locker layouts can be reconfigured and scaled as workplace requirements evolve, extending the functional lifespan of the design without structural modifications.")
    ],
    "it": [
        ("Employees / End Users",
         "Self-service access to devices anytime, faster pickup and return, and equipment that is often pre-charged or ready for use."),
        ("IT asset managers",
         "Real-time visibility of device allocation and usage, automated checkout and return logs, reduced incidents of lost or misplaced assets, and lower dependency on manual tracking. Improved inventory control, audit trails, easier planning for repairs and replacements, with stronger control during audits."),
        ("Security team",
         "Access control through role-based permissions, reduced unauthorized access, and a complete record of every transaction."),
        ("Finance / procurement",
         "Reduced replacement costs and over-purchasing through improved asset utilization along with lower losses and damage-related claims."),
        ("Compliance / audit teams",
         "Detailed logs, timestamped transactions, providing verifiable records of asset control for internal and external audits."),
        ("Leadership / business owners",
         "Improved operational efficiency, reduced downtime, strengthened governance, and enhanced protection of organisational assets."),
        ("Architects, Interior Designers & Consultants",
         "Supports efficient planning of locker zones within workplace layouts with secure and accessible storage integration. Enables integration of lockers into interior concepts with appropriate materials and finishes, maintaining visual consistency and functional alignment.")
    ],
    "visitor": [
        ("Visitors",
         "Secure storage for personal belongings, enabling faster entry into the premises and reducing the need to carry items into operational or restricted areas."),
        ("Reception / front desk",
         "Reduced congestion at entry points, simplified handling of visitor belongings, and improved efficiency in check-in and check-out processes."),
        ("Security team",
         "Improved control over visitor belongings, reduced risk of unauthorised item movement, and access to digital records of locker usage and access activity."),
        ("Admin / Facility Management",
         "Better control over shared visitor storage areas, support for compliance and monitoring requirements, and access to reports for incident review and audits."),
        ("Senior Management",
         "Improved protection of visitor assets, reduced operational risk exposure, enhanced visitor experience, and a more structured reception environment."),
        ("Architects, Interior designers & Consultants",
         "Enables efficient planning of locker zones within building layouts, supporting secure storage areas and structured movement flow at entry points. Allows integration of locker systems within reception and lobby design, maintaining visual consistency while supporting functional storage requirements.")
    ],
    "tool": [
        ("Tool users / Technicians",
         "Quick access to assigned tool kits, reduced time spent searching for tools, safer handling of shared resources, and simplified return processes after use."),
        ("Maintenance Team",
         "Improved control over tool kit availability, reduced instances of missing tools, faster issue and return cycles, and support for minimising downtime during maintenance activities."),
        ("Site Supervisors / Line Managers",
         "Visibility into tool kit allocation and usage, improved accountability, and better coordination across shifts and job sites."),
        ("Stores / Inventory Team",
         "Tracking of tool kit movement and usage, streamlined reconciliation processes, reduced dependency on manual records, and improved planning for replacements or servicing. Controlled access to valuable tools and improved audit traceability of issuance and return activity."),
        ("Operations Team",
         "More efficient workflows, less asset loss, better utilization of shared kits, and fewer interruptions caused by unavailable tools."),
        ("Finance / Procurement",
         "Reduced replacement costs and shrinkage, improved utilisation of tool assets, and better support for procurement and budgeting decisions."),
        ("Compliance / Audit teams",
         "Time-stamped usage records and traceability of tool kit allocation, supporting audit and safety requirements."),
        ("Facility / Plant Managers",
         "Centralised visibility of tool kit usage across departments, enabling better operational oversight and support for maintenance planning."),
        ("Contractors / Temporary Workers",
         "Controlled access to shared tool kits with clear allocation, supporting faster onboarding and improved accountability for issued equipment."),
        ("Project Team / Consultants",
         "Enables planning of locker zones within facility layouts to support efficient tool access and movement. Facilitates integration of locker infrastructure during project execution, reducing the need for post-installation modifications.")
    ],
    "fleet": [
        ("Fleet managers",
         "Full visibility into who has which vehicle key, faster allocation, fewer manual sign-outs, and better control across locations."),
        ("Drivers",
         "Quick and secure access to assigned vehicles, less waiting time, and a smoother start to shifts or trips."),
        ("Operations team",
         "Better coordination, lower downtime, improved vehicle rotation, and more efficient day-to-day fleet movement."),
        ("Security team",
         "Controlled access, reduced risk of lost or stolen keys, and a clear audit trail for every key transaction. Time-stamped records, stronger accountability, and easier reporting for internal audits and regulatory checks."),
        ("Finance team",
         "Lower replacement and rekeying costs, reduced losses, and improved fleet asset protection."),
        ("Maintenance team",
         "Easier control over service vehicles, clearer handover records, and fewer delays in vehicle availability."),
        ("Senior management",
         "Higher productivity, better fleet utilization, reduced liability, and stronger governance over company assets.")
    ],
    "server": [
        ("IT administrators",
         "Faster access to racks during troubleshooting, maintenance, and hardware replacement, with clear accountability for every key usage."),
        ("Data Center managers",
         "Better control over rack access, improved oversight across teams, and stronger operational discipline in sensitive areas. Less downtime, smoother handovers between shifts, and faster response during urgent service needs."),
        ("Security teams",
         "Reduced unauthorized access, stronger physical protection of infrastructure, and a complete transaction history."),
        ("Facilities teams",
         "Easier coordination of access for maintenance work, less dependence on manual key handling, and better infrastructure control."),
        ("Compliance teams",
         "Time-stamped logs, stronger traceability, and better support for internal audits and security policies."),
        ("Finance teams",
         "Lower replacement costs for lost keys, better protection of expensive IT assets, and reduced risk exposure."),
        ("Leadership",
         "Stronger governance, better business continuity, and reduced risk to mission-critical systems and services.")
    ],
    "premise": [
        ("Facility & Admin Managers",
         "Visibility into key usage across the workplace — including which keys are issued, to whom, and for how long. Alerts and system records help reduce manual follow-up on returns. Key-related administrative effort is reduced, and lost key incidents are documented with traceability."),
        ("IT & Security Teams",
         "Controlled access to server room, network room, and data centre keys based on defined permissions for authorised personnel. Access logs are maintained for all key usage related to sensitive infrastructure areas. Access permissions can be updated or revoked as part of administrative workflows."),
        ("HR & Operations Teams",
         "Key access provisioning and revocation can be managed in line with employee lifecycle processes. Reduces dependency on manual key collection during onboarding and off-boarding. Contractor and vendor access can be configured with defined usage controls and time-bound permissions."),
        ("Reception & Front Desk Teams",
         "Key issuance for visitors and contractors is supported through a structured system, reducing reliance on manual registers. Improves visibility into key allocation and reduces the need for manual tracking and follow-up."),
        ("Finance & Compliance Teams",
         "Documented audit trails for key access support internal audits and compliance reviews. Key-related incidents are recorded with usage history. Contractor access logs provide traceability for third-party key usage."),
        ("Senior Management",
         "Improved control over physical access to sensitive areas such as executive offices, finance rooms, IT infrastructure, and document storage. Supports better governance of physical access and helps reduce risks associated with untracked key usage.")
    ],
    "plant": [
        ("Maintenance Technicians",
         "Access to keys aligned with defined roles and job requirements, helping reduce the risk of incorrect key usage during operations. Shift handovers are supported with time-stamped records, improving clarity of key custody. Access history is recorded and available for reference when required."),
        ("Maintenance Supervisors",
         "Visibility into key usage across teams — including allocation and duration. Shift activity records support reconciliation during handovers. Outstanding key usage can be identified through system reports, helping improve follow-up and accountability."),
        ("Plant & Operations Managers",
         "Improved control over access to critical plant areas across shifts and contractor teams. Key usage records provide visibility into access patterns, helping reduce operational delays associated with untracked keys and improving overall coordination."),
        ("Environment, Health & Safety (EHS) Teams",
         "Access to keys for critical areas — such as chemical stores, electrical rooms, and confined spaces — can be configured with controlled access workflows to strengthen governance. Key access records support incident investigations, safety reviews, and regulatory inspections. Alignment with permit and operational processes improves visibility into access control practices."),
        ("Contractors & Third-Party Teams",
         "Access to keys can be configured based on defined scope and duration aligned with approved work. Reduces dependency on manual key handling by site personnel, while ensuring that activity is recorded for traceability and review."),
        ("HR & Compliance Teams",
         "Key access records for employees and contractors are available for audit, investigation, and compliance review purposes. Contractor access logs support traceability of third-party activity. Access can be managed based on defined authorisation criteria to ensure controlled usage of keys in sensitive area."),
        ("Senior Management & Leadership",
         "A structured, system-supported approach to managing physical access to critical plant areas. Improves governance of key usage and helps reduce risks associated with untracked access. Supports internal reporting and operational oversight.")
    ]
}

# Recovered specs table layouts
locker_specs_html = """
                <!-- Integrated Technical & Software Specifications (Tabbed) -->
                <div class="specs-tabs-wrapper">
                  <div class="specs-tab-nav">
                    <button class="specs-tab-btn active" data-tab="specs-hw-locker">Hardware</button>
                    <button class="specs-tab-btn" data-tab="specs-sw-locker">Software</button>
                  </div>
                  <div class="specs-tab-content">
                    <!-- Hardware Specs -->
                    <div class="specs-tab-pane active" id="specs-hw-locker">
                      <div class="spec-table-block card-panel" style="padding: 30px; background: #ffffff; border-radius: 12px; border: 1px solid var(--border-light); max-width: 900px; margin: 0 auto; box-shadow: var(--shadow-normal);">
                        <h4 style="font-size: 1.2rem; color: var(--color-navy); margin-top: 0; margin-bottom: 20px; font-family: var(--font-secondary); border-bottom: 2px solid var(--border-light); padding-bottom: 12px; font-weight: 700;">Hardware & Physical Specifications</h4>
                        <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; line-height: 1.8;">
                          <tbody>
                            <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Cabinet Material</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">CRCA Powder-Coated Steel</td></tr>
                            <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Dimensions (Std Panel)</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">462 mm (W) x 414 mm (H) x 191 mm (D)</td></tr>
                            <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Power Supply Input</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">230 V AC, 50 Hz</td></tr>
                            <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Operating Voltage</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">12 V DC</td></tr>
                            <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Max Power Draw</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">2 Amp</td></tr>
                            <tr><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Mounting Options</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">Wall-mounted or Floor-standing</td></tr>
                          </tbody>
                        </table>
                      </div>
                    </div>

                    <!-- Software Specs -->
                    <div class="specs-tab-pane" id="specs-sw-locker">
                      <div class="spec-table-block card-panel" style="padding: 30px; background: #ffffff; border-radius: 12px; border: 1px solid var(--border-light); max-width: 900px; margin: 0 auto; box-shadow: var(--shadow-normal);">
                        <h4 style="font-size: 1.2rem; color: var(--color-navy); margin-top: 0; margin-bottom: 20px; font-family: var(--font-secondary); border-bottom: 2px solid var(--border-light); padding-bottom: 12px; font-weight: 700;">Software & System Specifications</h4>
                        <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; line-height: 1.8;">
                          <tbody>
                            <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Locker Allocation</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">Dynamic & Fixed Assignment (Auto-scheduled)</td></tr>
                            <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Access Modes</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">RFID Cards, Biometrics, PIN Pad, Mobile App (NFC/BLE)</td></tr>
                            <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Access Levels</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">Up to 5-tier role-based access control</td></tr>
                            <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">System Integration</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">REST APIs, Active Directory, HRMS & ITSM</td></tr>
                            <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Operational Mode</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">Online with full Standalone Offline fallback mode</td></tr>
                            <tr><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Real-Time Tracking</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">Tamper notifications, status alerts, audit-ready logs</td></tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                </div>
"""

keyknox_specs_html = """
            <!-- Integrated Technical & Software Specifications (Tabbed) -->
            <div class="specs-tabs-wrapper">
              <div class="specs-tab-nav">
                <button class="specs-tab-btn active" data-tab="specs-hw-cabinet">Hardware</button>
                <button class="specs-tab-btn" data-tab="specs-sw-cabinet">Software</button>
              </div>
              <div class="specs-tab-content">
                <!-- Hardware Specs -->
                <div class="specs-tab-pane active" id="specs-hw-cabinet">
                  <div class="spec-table-block card-panel" style="padding: 30px; background: #ffffff; border-radius: 12px; border: 1px solid var(--border-light); max-width: 900px; margin: 0 auto; box-shadow: var(--shadow-normal);">
                    <h4 style="font-size: 1.2rem; color: var(--color-navy); margin-top: 0; margin-bottom: 20px; font-family: var(--font-secondary); border-bottom: 2px solid var(--border-light); padding-bottom: 12px; font-weight: 700;">Cabinet Hardware Specifications</h4>
                    <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; line-height: 1.8;">
                      <tbody>
                        <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Cabinet Material</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">Powder-coated mild steel (1 mm)</td></tr>
                        <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Door Type</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">Transparent polycarbonate with metal frame</td></tr>
                        <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Capacity & Expandability</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">16 / 32 base keys, expandable to 128 keys</td></tr>
                        <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Dimensions</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">745 × 614 × 175 mm</td></tr>
                        <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Weight</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">21 kg (base unit)</td></tr>
                        <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Power Supply Input</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">110V – 240V AC</td></tr>
                        <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Power Supply Output</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">15V DC</td></tr>
                        <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Power Consumption</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">Approx. 20W per 32 keys</td></tr>
                        <tr><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Compliance</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">BIS, CE</td></tr>
                      </tbody>
                    </table>
                  </div>
                </div>

                <!-- Software Specs -->
                <div class="specs-tab-pane" id="specs-sw-cabinet">
                  <div class="spec-table-block card-panel" style="padding: 30px; background: #ffffff; border-radius: 12px; border: 1px solid var(--border-light); max-width: 900px; margin: 0 auto; box-shadow: var(--shadow-normal);">
                    <h4 style="font-size: 1.2rem; color: var(--color-navy); margin-top: 0; margin-bottom: 20px; font-family: var(--font-secondary); border-bottom: 2px solid var(--border-light); padding-bottom: 12px; font-weight: 700;">Software & System Specifications</h4>
                    <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; line-height: 1.8;">
                      <tbody>
                        <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Locker Management Software</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">KeyKnox Shield</td></tr>
                        <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">User Capacity</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">Up to 500 users per system</td></tr>
                        <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Event Storage Capacity</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">50,000 events</td></tr>
                        <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Communication</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">TCP/IP</td></tr>
                        <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">RFID Support</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">125kHz / 13.56MHz</td></tr>
                        <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Multi-factor Authentication</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">RFID, PIN, optional biometric</td></tr>
                        <tr style="border-bottom: 1px solid var(--border-light);"><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Key Position Tracking</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">Hook positional sensors</td></tr>
                        <tr><td style="padding: 10px 0; font-weight: 600; color: #4c4d56;">Compliance Reports</td><td style="padding: 10px 0; text-align: right; color: #0e0e0e; font-weight: 500;">Excel and PDF export support</td></tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
"""

def generate_header(active_page, active_sub):
    return f"""  <header class="site-header" id="site-header">
    <div class="header-container">
      <a class="logo-link" href="index.html" style="display: inline-block; padding: 5px 0;">
        <img src="assets/images/new_logo.png" alt="Meclix Mechatronix" style="max-height: 48px; width: auto; display: block;">
      </a>
      
      <button class="menu-toggle" id="menu-toggle" aria-label="Toggle menu">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
      </button>

      <nav class="nav-menu" id="nav-menu">
        <a class="nav-link{" active" if active_page == "home" else ""}" href="index.html">Home</a>
        <a class="nav-link{" active" if active_page == "about" else ""}" href="about.html">About Us</a>
        <div class="nav-dropdown">
          <a class="nav-link dropdown-toggle{" active" if active_page == "lockers" else ""}" href="lockers.html">ArcaKnox System</a>
          <ul class="dropdown-menu">
            <li><a href="lockers.html"{" class=\"active\"" if active_sub == "employee" else ""}>Employee Assets</a></li>
            <li><a href="it-lockers.html"{" class=\"active\"" if active_sub == "it" else ""}>IT Assets</a></li>
            <li><a href="visitor-lockers.html"{" class=\"active\"" if active_sub == "visitor" else ""}>Visitor Assets</a></li>
            <li><a href="tool-lockers.html"{" class=\"active\"" if active_sub == "tool" else ""}>Tool Kits</a></li>
          </ul>
        </div>
        <div class="nav-dropdown">
          <a class="nav-link dropdown-toggle{" active" if active_page == "keyknox" else ""}" href="keyknox.html">KeyKnox System</a>
          <ul class="dropdown-menu">
            <li><a href="keyknox.html"{" class=\"active\"" if active_sub == "fleet" else ""}>Fleet & Vehicles</a></li>
            <li><a href="server-racks.html"{" class=\"active\"" if active_sub == "server" else ""}>Server Racks</a></li>
            <li><a href="premise-workplace.html"{" class=\"active\"" if active_sub == "premise" else ""}>Premise & Workplace</a></li>
            <li><a href="plant-maintenance.html"{" class=\"active\"" if active_sub == "plant" else ""}>Plant & Maintenance</a></li>
          </ul>
        </div>
        <div class="nav-cta">
          <button class="btn btn-primary btn-sm btn-consultation-trigger">Book Consultation</button>
        </div>
      </nav>
    </div>
  </header>"""

def generate_value_matrix_redesign(usecase_key):
    stakeholders = benefits_data[usecase_key]
    sidebar_items_html = ""
    panes_html = ""
    
    for i, (name, benefits) in enumerate(stakeholders):
        slug = get_slug(name)
        active_class = " active" if i == 0 else ""
        icon = get_icon(name)
        
        # Sidebar item
        sidebar_items_html += f"""            <li class="locker-sidebar-item{active_class}" data-tab="{slug}">
              <button>
                {icon}
                {name}
              </button>
            </li>\n"""
            
        # Stakeholder pane card
        panes_html += f"""          <!-- Pane: {name} -->
          <div class="locker-pane{active_class}" id="pane-{slug}">
            <div class="stakeholder-card card-panel" style="padding: 35px; background: #ffffff; border-radius: 12px; border: 1px solid var(--border-light); box-shadow: var(--shadow-normal);">
              <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 24px; border-bottom: 1px solid var(--border-light); padding-bottom: 15px;">
                <div style="width: 48px; height: 48px; background: rgba(8, 106, 216, 0.08); color: var(--color-primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                  {icon}
                </div>
                <h4 style="margin: 0; font-size: 1.35rem; color: var(--color-navy); font-weight: 700;">{name}</h4>
              </div>
              <p style="font-size: 1.05rem; line-height: 1.75; color: var(--color-body); font-weight: 500; margin: 0;">
                {benefits}
              </p>
            </div>
          </div>\n\n"""

    new_redesign_html = f"""
      <!-- Value Matrix Section (Interactive Stakeholder Classification) -->
      <div class="section-header" style="margin-top: 60px; margin-bottom: 30px; text-align: center;">
        <span class="eyebrow" style="font-size: 0.85rem; letter-spacing: 1px;">Value Matrix</span>
        <h2 style="font-size: 2rem; color: #021e40; margin: 5px 0 10px 0;">Who Benefits & How</h2>
        <p style="color: var(--color-body); font-size: 1rem; max-width: 600px; margin: 0 auto;">Select a stakeholder from the left menu to view detailed operational benefits.</p>
      </div>

      <div class="locker-redesign-container" style="margin-top: 30px;">
        <!-- Stakeholder Sidebar Menu -->
        <aside class="locker-sidebar">
          <div class="locker-sidebar-title">Stakeholders</div>
          <ul class="locker-sidebar-menu">
{sidebar_items_html.rstrip()}
          </ul>
        </aside>

        <!-- Stakeholder Content Area -->
        <div class="locker-content-area">
{panes_html.rstrip()}
        </div>
      </div>
    """
    return new_redesign_html

def process_locker_page(filename, usecase_key, title, description):
    print(f"Processing Locker page: {filename}")
    filepath = os.path.join(workspace_dir, filename)
    
    # Read the base lockers.html (from c76b62b to get clean un-split data)
    # Actually we can just read the current locks base file or recreate it since it is reverted clean.
    basepath = os.path.join(workspace_dir, "lockers.html")
    with open(basepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace Title & Description
    content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content)
    content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{description}">', content)
    
    # Replace CTA heading
    content = content.replace("Find the Right Locker Solution", "Find the Right Smart Locker Management")
    
    # Replace Header
    header_start = content.find('<header class="site-header" id="site-header">')
    header_end = content.find('</header>', header_start) + 9
    new_header = generate_header("lockers", usecase_key)
    content = content[:header_start] + new_header + content[header_end:]
    
    # Extract the isolated usecase block
    usecase_blocks_start = content.find('<div class="usecase-blocks">')
    matrix_section_start = content.find('<!-- Value Matrix Section')
    if matrix_section_start == -1:
        matrix_section_start = content.find('<div class="stakeholder-matrix-section">')
    if matrix_section_start == -1:
        matrix_section_start = content.find('<!-- Stakeholder Matrix Section -->')
        
    if usecase_blocks_start == -1 or matrix_section_start == -1:
        print(f"Error finding usecase-blocks or matrix section in lockers.html")
        return
        
    ca = content[usecase_blocks_start:matrix_section_start]
    
    idx_emp = ca.find('<!-- Use Case 1: Employee Assets -->')
    idx_it = ca.find('<!-- Use Case 2: IT Assets -->')
    idx_vis = ca.find('<!-- Use Case 3: Visitor Assets -->')
    idx_tool = ca.find('<!-- Use Case 4: Tool Kits -->')
    
    last_div_idx = ca.rfind('</div>')
    
    panes = {
        'employee': ca[idx_emp:idx_it],
        'it': ca[idx_it:idx_vis],
        'visitor': ca[idx_vis:idx_tool],
        'tool': ca[idx_tool:last_div_idx]
    }
    
    active_pane_html = panes[usecase_key].strip()
    
    # Place specs tabs OUTSIDE the usecase-block 2-column grid
    active_pane_html = active_pane_html + '\n' + locker_specs_html
    
    # Locate redesign area: from start of usecase-blocks to start of Page CTA
    redesign_start = usecase_blocks_start
    redesign_end = content.find('<!-- Page CTA -->')
    
    new_matrix_html = generate_value_matrix_redesign(usecase_key)
    
    reconstructed_body = f"""<div class="usecase-blocks">
        {active_pane_html}
      </div>
      
      {new_matrix_html}
      """
      
    final_content = content[:redesign_start] + reconstructed_body + content[redesign_end:]
    final_content = apply_footer(final_content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"Successfully generated {filename}")

def process_keyknox_page(filename, usecase_key, title, description):
    print(f"Processing KeyKnox page: {filename}")
    filepath = os.path.join(workspace_dir, filename)
    
    # Read the base keyknox.html
    basepath = os.path.join(workspace_dir, "keyknox.html")
    with open(basepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace Title & Description
    content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content)
    content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{description}">', content)
    
    # Replace CTA Access Control to Asset Control
    content = content.replace("Ready to Strengthen your Access Control?", "Ready to Strengthen your Asset Control?")
    
    # Replace Header
    header_start = content.find('<header class="site-header" id="site-header">')
    header_end = content.find('</header>', header_start) + 9
    new_header = generate_header("keyknox", usecase_key)
    content = content[:header_start] + new_header + content[header_end:]
    
    # Extract the isolated usecase pane
    usecases_start = content.find('<!-- Sector-Specific Key Governance Content -->')
    if usecases_start == -1:
        usecases_start = content.find('<div class="key-use-cases-tabs')
    usecases_end = content.find('<!-- Page CTA -->')
    
    if usecases_start == -1 or usecases_end == -1:
        print(f"Error finding key-use-cases-tabs in keyknox.html")
        return
        
    ca = content[usecases_start:usecases_end]
    
    idx_fleet = ca.find('<!-- Fleet & Vehicles -->')
    idx_server = ca.find('<!-- Server Racks -->')
    idx_premise = ca.find('<!-- Premise / Workplace -->')
    idx_plant = ca.find('<!-- Plant & Maintenance -->')
    
    last_div_idx = ca.rfind('</div>')
    second_last_div_idx = ca.rfind('</div>', 0, last_div_idx)
    
    panes = {
        'fleet': ca[idx_fleet:idx_server],
        'server': ca[idx_server:idx_premise],
        'premise': ca[idx_premise:idx_plant],
        'plant': ca[idx_plant:second_last_div_idx]
    }
    
    active_pane_html = panes[usecase_key].strip()
    
    # Place specs tabs OUTSIDE the use-case-pane grid
    active_pane_html = active_pane_html + '\n' + keyknox_specs_html
    
    # Make sure it's active
    if 'use-case-pane active' not in active_pane_html:
        active_pane_html = active_pane_html.replace('use-case-pane', 'use-case-pane active')
        
    new_matrix_html = generate_value_matrix_redesign(usecase_key)
    
    reconstructed_body = f"""<!-- Sector-Specific Key Governance Content -->
      <div class="key-use-cases-tabs" style="margin-top: 40px;">
        <div class="use-case-tab-content">
          {active_pane_html}
        </div>
      </div>
      
      {new_matrix_html}
      """
      
    final_content = content[:usecases_start] + reconstructed_body + content[usecases_end:]
    final_content = apply_footer(final_content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"Successfully generated {filename}")

def update_global_page(filename, active_page):
    print(f"Updating global page header: {filename}")
    filepath = os.path.join(workspace_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    header_start = content.find('<header class="site-header" id="site-header">')
    if header_start == -1:
        header_start = content.find('<header class="site-header" id="masthead">')
    if header_start == -1:
        print(f"Header not found in {filename}")
        return
        
    header_end = content.find('</header>', header_start) + 9
    new_header = generate_header(active_page, None)
    
    final_content = content[:header_start] + new_header + content[header_end:]
    final_content = apply_footer(final_content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"Successfully updated header and footer in {filename}")

# First reset lockers.html and keyknox.html to commit c76b62b (which has all use cases) to make sure we process the clean original base files!
os.system("git checkout c76b62b -- lockers.html keyknox.html")

# Run font migration on the base template files
os.system("python scratch/change_font_to_poppins.py")

# Execute
process_locker_page("it-lockers.html", "it", 
                   "Smart Locker for IT Asset Management | Meclix Mechatronix",
                   "Secure, electronically controlled storage for laptops, tablets, and peripherals. Automated checkout, integrated charging, and compliance-ready audit trails.")

process_locker_page("visitor-lockers.html", "visitor", 
                   "Smart Locker for Visitor Asset Management | Meclix Mechatronix",
                   "Secure visitor locker systems integrated with Visitor Management Systems (VMS). QR code access, self-service retrieval, and audit logging.")

process_locker_page("tool-lockers.html", "tool", 
                   "Smart Locker for Tool Management | Meclix Mechatronix",
                   "Secure electronic tool lockers for industrial, assembly, and maintenance teams. Track checkout, returns, and damaged items with full shift accountability.")

# lockers.html processed last
process_locker_page("lockers.html", "employee", 
                   "Smart Locker for Employee Asset Management | Meclix Mechatronix",
                   "Meclix Smart Locker: Secure storage for employee assets, RFID-based access, real-time tracking, and audit-ready reporting.")

process_keyknox_page("server-racks.html", "server",
                    "KeyKnox Key Management for Server Racks | Meclix Mechatronix",
                    "Advanced electronic key cabinets to secure server racks and network closets. Role-based permissions and compliance logging for datacenters.")

process_keyknox_page("premise-workplace.html", "premise",
                    "KeyKnox Key Management for Workplace | Meclix Mechatronix",
                    "Electronic key control cabinets for corporate offices, workspaces, and campuses. Time-bound permissions, exit integration, and full audit logs.")

process_keyknox_page("plant-maintenance.html", "plant",
                    "KeyKnox Key Management for Plant & Maintenance | Meclix Mechatronix",
                    "Secure industrial key cabinets for manufacturing, utilities, and pharma plants. Manage technician shifts, contractor access, and critical safety isolations.")

# keyknox.html processed last
process_keyknox_page("keyknox.html", "fleet",
                    "KeyKnox Electronic Key Management for Fleet Management | Meclix Mechatronix",
                    "Secure, track, and manage vehicle keys for logistics, showrooms, and corporate fleets. RFID tracking, driver authentication, and audit trails.")

# 2. Update global pages headers
update_global_page("index.html", "home")
update_global_page("about.html", "about")
update_global_page("software.html", "software")

print("All tasks completed successfully!")
