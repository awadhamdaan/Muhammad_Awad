from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'


@app.route('/')
def home():
    context = {
        'name': 'Muhammad Awad Yasin',
        'title': 'Operations & Business Support Manager | Full-Stack Developer',
        'summary': 'Operations/Business Account Management, Business Development Professional with 20+ years of experience across Pakistan, the UAE, Saudi Arabia, and Portugal. Proven expertise in operations management, finance, customer experience, compliance, process improvement, and team leadership. '
                   'Now successfully transitioning into Full-Stack Python Development, having built and deployed real-world web applications using Django, PostgreSQL, HTML, CSS, JavaScript, and Git/GitHub. '
                   'Designed and developed Marhaba Super Market & Services — a multi-module business platform integrating e-commerce, travel booking, remittance services, and CV building — as well as a desktop ERP application for fleet management. '
                   'Seeking to bring my international experience and technical skills to a progressive organization in the Netherlands.',

        'stats': {
            'experience': '20+',
            'countries': '4',
            'clients': '60+',
            'teams': '40+'
        },

        'target_positions': [
            'Operations Manager', 'Business Manager', 'Customer Experience Manager',
            'Office Manager', 'Finance & Operations', 'Business Support Manager',
            'Quality Control Manager', 'Operations Coordinator', 'Operations Analyst',
            'Process Improvement Specialist', 'Project Coordinator', 'Data Analyst',
            'Full-Stack Python Developer', 'Django Developer'
        ],

        'experience': [
            # ===== CURRENT ROLE =====
            {
                'about_company': "Lifecent Unipessoal is a Portugal-based parent company overseeing multiple business divisions, including LTMT Travels & Money Transfers, which provides travel management, visa consultancy, foreign exchange, and international money transfer services, and Uma Iniciativa, which specializes in workforce recruitment, labor supply, international hiring, work permit processing, and staffing solutions.",
                'title': 'Operations Manager',
                'company': 'Lifecent Unipessoal',
                'logo': 'lifecent.png',
                'location': 'Portugal',
                'period': '2020 - Present',
                'description': [
                    'Directed end-to-end operations across travel, financial services, and workforce solutions',
                    'Led and developed a team of 40+ employees, driving performance and productivity',
                    'Managed financial operations including budgeting, cash flow, and regulatory compliance',
                    'Oversaw travel management, visa processing, and international money transfers',
                    'Built relationships with 60+ retail and corporate clients'
                ]
            },

            # ===== MARHABA SUPER MARKET & SERVICES =====
            {
                'about_company': "Marhaba Super Market & Services is a subsidiary of Lifecent Unipessoal, operating a multi-module business platform integrating e-commerce, service management, travel booking, and custom software development.",
                'title': 'Full-Stack Python/Django Developer',
                'company': 'Marhaba Super Market & Services',
                'logo': 'marhaba.png',
                'location': 'Portugal',
                'period': '2026 - Present',
                'project_urls': [
                    {'name': '🛒 Super Market', 'url': 'https://marhaba-market-services.com/'},
                    {'name': '🛠️ Marhaba Services', 'url': 'https://marhaba-market-services.com/marhaba-services/'}
                ],
                'description': [
                    'Designed and developed a multi-module web-based business platform using Python, Django, PostgreSQL, HTML, CSS, JavaScript, Git/GitHub and Render, integrating e-commerce and service-management functionality within a single application.',
                    'Developed a modular Django architecture covering customer accounts, product catalog, inventory, shopping cart, wishlist, orders, payments, coupons and customer reviews.',
                    'Designed and implemented a PostgreSQL relational database with Django ORM models and administrative management through Django Admin.',
                    'Developed Marhaba Services, providing a central platform for travel, remittance and other customer services.',
                    'Built a CV Builder allowing structured user information to be converted into professionally formatted CV output.',
                    'Developed customer-facing forms, validation, business rules, responsive interfaces and administrative workflows.',
                    'Implemented environment-based configuration for local development and production deployment.',
                    'Used Git and GitHub for source control and deployed the production application using Render and PostgreSQL.',
                    'Structured the project using reusable Django applications to support future expansion and third-party API integrations.'
                ]
            },

            # ===== MARHABA TRAVEL BOOKING SYSTEM =====
            {
                'about_company': "Marhaba Travel Booking & Airline Ticketing System is part of the Marhaba Services platform, providing end-to-end airline reservation, ticketing and post-booking management.",
                'title': 'Full-Stack Developer - Travel Booking System',
                'company': 'Marhaba Travel Services',
                'logo': 'marhaba.png',
                'location': 'Portugal',
                'period': '2026 - Present',
                'description': [
                    'Developed one-way and round-trip flight search and booking workflows with passenger management for adults, children and infants.',
                    'Implemented mandatory passenger information including passport details, nationality, and emergency contact information.',
                    'Built structured flight itinerary management covering outbound and return flights, departure/arrival times, baggage, cabin class, duration and stops.',
                    'Developed booking lifecycle management covering booking, held status, payment, ticket processing, ticketing, cancellation, reissue and refund states.',
                    'Implemented unique Marhaba booking references, PNR/provider references and individual passenger e-ticket numbers.',
                    'Built a complete ticket reissue/exchange workflow, including new flight selection, fare difference, airline change penalties and new ticket generation.',
                    'Implemented partial passenger reissue, enabling selected passengers to move to a new itinerary while remaining passengers retain their original itinerary.',
                    'Developed split-PNR-ready workflows for selected-passenger reissues and refunds.',
                    'Built dynamically generated professional PDF e-tickets using ReportLab, including itinerary, individual passenger ticket details, payment/exchange history, baggage information and fare policies.',
                    'Created provider abstraction supporting a mock flight provider for development/testing and a structure prepared for integration with external supplier APIs.'
                ]
            },

            # ===== TRUCK DISPATCHER PRO =====
            {
                'about_company': "Truck Dispatcher Pro is a standalone desktop ERP application for trucking, fleet and dispatch operations.",
                'title': 'Python Desktop Application Developer',
                'company': 'Truck Dispatcher Pro',
                'logo': 'truck.png',
                'location': 'Portugal',
                'period': '2026 - Present',
                'description': [
                    'Developed a modular desktop ERP application for trucking, fleet and dispatch operations using Python, PyQt6, SQLAlchemy and SQLite.',
                    'Built driver management functionality with database-backed CRUD operations.',
                    'Developed modules for trucks, trailers, loads and dispatch operations.',
                    'Designed relational database models using SQLAlchemy ORM and SQLite.',
                    'Developed dispatch workflows connecting drivers, trucks, trailers and loads.',
                    'Built an analytical management dashboard displaying operational and financial KPIs.',
                    'Developed monthly financial visualization and invoice/dispatch status charts.',
                    'Added dashboard views for recent dispatches, recent invoices and year-based reporting.',
                    'Designed a modular Finance & Accounting architecture for integration with fleet operations.',
                    'Structured the application for future Windows EXE and installer distribution.'
                ]
            },

            # ===== MARHABA REMITTANCE MODULE =====
            {
                'about_company': "Marhaba Remittance / Money Transfer Module is part of the Marhaba Services platform, providing web-based remittance quotation and enquiry.",
                'title': 'Python/Django Developer - Remittance Module',
                'company': 'Marhaba Services',
                'logo': 'marhaba.png',
                'location': 'Portugal',
                'period': '2026 - Present',
                'description': [
                    'Developed a web-based remittance quotation and enquiry module integrated into the Marhaba Services platform.',
                    'Created customer-facing international money-transfer quotation workflows.',
                    'Implemented country-based demo exchange-rate calculations.',
                    'Created structured remittance enquiry and customer information forms.',
                    'Designed the module for future integration with a live remittance provider API.',
                    'Integrated the module into the broader Django services architecture.'
                ]
            },

            # ===== SHARJAH NATIONAL TRAVEL - SAUDI ARABIA =====
            {
                'about_company': "Leading UAE-based travel and business services organization operating a nationwide branch network.",
                'title': 'Operations & Customer Experience Manager',
                'company': 'Sharjah National Travel & Tourism',
                'logo': 'sntt.png',
                'location': 'Kingdom of Saudi Arabia',
                'period': '2017 - 2019',
                'description': [
                    'Managed daily branch operations, ensuring service excellence and regulatory compliance',
                    'Led and developed a team of 13 employees, driving performance and accountability',
                    'Independently managed key corporate accounts and built strong client relationships',
                    'Monitored operational performance through KPI-driven decision-making'
                ]
            },

            # ===== SHARJAH NATIONAL TRAVEL - UAE =====
            {
                'about_company': "Leading UAE-based travel and business services organization operating a nationwide branch network.",
                'title': 'Assistant Manager - Finance, Operations',
                'company': 'Sharjah National Travel & Tourism',
                'logo': 'sntt.png',
                'location': 'Khorfakkan, UAE',
                'period': '2011 - 2016',
                'description': [
                    'Oversaw finance and operational support across 6 regional branches',
                    'Managed accounts payable, receivable, reconciliations, and financial reporting',
                    'Coordinated payroll and inter-branch transactions using Oracle ERP',
                    'Handled high-volume settlement processes through Sabre, Galileo, and BSP Link'
                ]
            },
            {
                'about_company': "Leading UAE-based travel and business services organization operating a nationwide branch network.",
                'title': 'Branch Accountant',
                'company': 'Sharjah National Travel & Tourism',
                'logo': 'sntt.png',
                'location': 'Khorfakkan, UAE',
                'period': '2008 - 2011',
                'description': [
                    'Managed accounts receivable, reconciliations, and customer payment follow-up',
                    'Oversaw daily cash management and bank deposits',
                    'Prepared bank reconciliations and client account statements',
                    'Maintained accurate financial documentation and compliance'
                ]
            },

            # ===== MARHABA AVIATION =====
            {
                'about_company': "Marhaba Aviation Pvt. Ltd. (General Sales Agent for Gulf Air) representing Gulf Air in Pakistan, providing airline sales, financial administration, and commercial support services.",
                'title': 'Finance Supervisor',
                'company': 'Marhaba Aviation Pvt. Ltd.',
                'logo': 'marhaba.png',
                'location': 'Peshawar, Pakistan',
                'period': '2003 - 2008',
                'description': [
                    'Supervised daily financial operations, cash management, and bank reconciliations',
                    'Managed sales reporting for 140+ travel agency partners',
                    'Controlled daily cash transactions exceeding PKR 4 million',
                    'Prepared financial reports and supported airline operational reporting'
                ]
            }
        ],

        'software_projects': [
            {
                'title': 'Marhaba Super Market - Full-Stack Django Platform',
                'technologies': ['Python', 'Django', 'PostgreSQL', 'HTML5', 'CSS3', 'JavaScript', 'Git', 'Render'],
                'project_url': 'https://marhaba-market-services.com/',
                'description': [
                    'Designed and developed a multi-module business platform integrating e-commerce and service management',
                    'Built customer accounts, product catalog, inventory, shopping cart, wishlist, orders, payments, coupons and reviews',
                    'Developed Marhaba Services platform for travel, remittance and other customer services',
                    'Created a CV Builder for professional CV output from structured user data',
                    'Deployed on Render with PostgreSQL and Git/GitHub version control'
                ]
            },
            {
                'title': 'Marhaba Travel Booking & Ticketing System',
                'technologies': ['Python', 'Django', 'PostgreSQL', 'ReportLab', 'Git'],
                'description': [
                    'End-to-end airline reservation, ticketing and post-booking management system',
                    'One-way and round-trip flight search, booking, and passenger management',
                    'Complete booking lifecycle: hold, payment, ticketing, cancellation, reissue and refund',
                    'PDF e-ticket generation with ReportLab including itinerary and passenger details',
                    'Split-PNR-ready workflows for partial reissues and refunds'
                ]
            },
            {
                'title': 'Truck Dispatcher Pro - Desktop Fleet ERP',
                'technologies': ['Python', 'PyQt6', 'SQLAlchemy', 'SQLite'],
                'description': [
                    'Modular desktop ERP for trucking, fleet and dispatch operations',
                    'Driver, truck, trailer, load and dispatch management modules',
                    'Analytical dashboard with operational and financial KPIs',
                    'Monthly financial visualization and invoice/dispatch status charts',
                    'Structured for Windows EXE and installer distribution'
                ]
            }
        ],

        'education': [
            {'degree': 'Bachelor of Business Administration (BBA)', 'institution': 'University of East',
             'location': 'Karachi, Pakistan'},
            {'degree': 'Full Stack Python Development Diploma', 'institution': 'Udemy/Self Studies',
             'location': 'Ongoing'},
            {'degree': 'Diploma in Accounting', 'institution': 'Govt. College of Commerce',
             'location': 'Peshawar, Pakistan'}
        ],

        'skills': {
            'Technical': [
                {'name': 'Python', 'level': 85},
                {'name': 'SQL', 'level': 80},
                {'name': 'JavaScript', 'level': 70},
                {'name': 'HTML & CSS', 'level': 75},
                {'name': 'Django & Flask', 'level': 75},
                {'name': 'Git & GitHub', 'level': 70},
                {'name': 'Oracle ERP', 'level': 90},
                {'name': 'Data Analysis', 'level': 85}
            ],
            'Travel Systems': [
                {'name': 'Amadeus', 'level': 85},
                {'name': 'Sabre', 'level': 80},
                {'name': 'Galileo', 'level': 75},
                {'name': 'BSP Link', 'level': 80}
            ],
            'Office': [
                {'name': 'Microsoft Office Suite', 'level': 90},
                {'name': 'Google Workspace', 'level': 85},
                {'name': 'E-Travel 2000', 'level': 80}
            ]
        },

        'technologies': ['Python', 'Django', 'Flask', 'JavaScript', 'SQL', 'PostgreSQL',
                         'Oracle ERP', 'Amadeus', 'Sabre', 'Galileo', 'Git', 'HTML5', 'CSS3'],

        'languages': [
            {'name': 'English', 'level': 'Fluent'},
            {'name': 'Arabic', 'level': 'Professional'},
            {'name': 'Urdu', 'level': 'Native'},
            {'name': 'Portuguese', 'level': 'Intermediate'}
        ],

        'personal': {
            'nationality': 'Pakistan',
            'dob': '04 Jul 1982',
            'visa_status': 'Residence Card Holder',
            'country_of_residence': 'Portugal',
            'marital_status': 'Married',
            'driving_license': 'Light Vehicle, Motor Bike',
            'contact_number': '+351-920008127'
        },

        'links': {
            'linkedin': 'https://www.linkedin.com/feed/',
            'github': 'https://github.com/your-profile',
            'email': 'mailto:eman.awad.hamdaan.pt@gmail.com',
            'whatsapp': 'https://wa.me/351920008127'
        }
    }
    return render_template('index.html', **context)


# ===== CONTACT ROUTE =====
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('contact'))

        try:
            # Email configuration
            sender_email = 'eman.awad.hamdaan.pt@gmail.com'
            sender_password = 'cfazcoibkeaiwthm'  # Your App Password
            recipient_email = 'eman.awad.hamdaan.pt@gmail.com'

            # Create message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = f"New Message from {name} - Portfolio Contact"

            body = f"""
            Name: {name}
            Email: {email}
            Message:
            {message}
            """
            msg.attach(MIMEText(body, 'plain'))

            # Send email with timeout
            server = smtplib.SMTP('smtp.gmail.com', 587, timeout=30)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            server.quit()

            flash('Thank you! Your message has been sent successfully.', 'success')
            return redirect(url_for('contact'))
        except smtplib.SMTPAuthenticationError:
            flash('Email authentication failed. Please check your email settings.', 'error')
            return redirect(url_for('contact'))
        except smtplib.SMTPException as e:
            flash(f'Email server error: {str(e)}', 'error')
            return redirect(url_for('contact'))
        except Exception as e:
            print(f"Error: {str(e)}")
            flash('Error sending message. Please try again later or contact me directly via email.', 'error')
            return redirect(url_for('contact'))

    return render_template('contact.html',
                           name='Muhammad Awad Yasin',
                           title='Operations & Business Support Manager | Full-Stack Developer')


if __name__ == '__main__':
    app.run(debug=True)