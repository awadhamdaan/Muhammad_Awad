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
        'title': 'Operations & Business Support Manager',
        'summary': 'Operations/Business Account Management, Business Development Professional with 20+ years of experience across Pakistan, the UAE, Saudi Arabia, and Portugal. Proven expertise in operations management, finance, customer experience, compliance, process improvement, and team leadership.',

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
            'Process Improvement Specialist', 'Project Coordinator', 'Data Analyst'
        ],

        'experience': [
            {
                'about_company': "Lifecent Unipessoal is a Portugal-based parent company overseeing multiple business divisions, including LTMT Travels & Money Transfers, which provides travel management, visa consultancy, foreign exchange, and international money transfer services, and Uma Iniciativa, which specializes in workforce recruitment, labor supply, international hiring, work permit processing, and staffing solutions.",
                'title': 'Operations Manager',
                'company': 'Lifecent Unipessoal',
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
            {
                'about_company': "Leading UAE-based travel and business services organization operating a nationwide branch network.",
                'title': 'Operations & Customer Experience Manager',
                'company': 'Sharjah National Travel & Tourism',
                'location': 'Kingdom of Saudi Arabia',
                'period': '2017 - 2019',
                'description': [
                    'Managed daily branch operations, ensuring service excellence and regulatory compliance',
                    'Led and developed a team of 13 employees, driving performance and accountability',
                    'Independently managed key corporate accounts and built strong client relationships',
                    'Monitored operational performance through KPI-driven decision-making'
                ]
            },
            {
                'about_company': "Leading UAE-based travel and business services organization operating a nationwide branch network.",
                'title': 'Assistant Manager - Finance, Operations',
                'company': 'Sharjah National Travel & Tourism',
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
                'location': 'Khorfakkan, UAE',
                'period': '2008 - 2011',
                'description': [
                    'Managed accounts receivable, reconciliations, and customer payment follow-up',
                    'Oversaw daily cash management and bank deposits',
                    'Prepared bank reconciliations and client account statements',
                    'Maintained accurate financial documentation and compliance'
                ]
            },
            {
                'about_company': "Marhaba Aviation Pvt. Ltd. (General Sales Agent for Gulf Air) representing Gulf Air in Pakistan, providing airline sales, financial administration, and commercial support services.",
                'title': 'Finance Supervisor',
                'company': 'Marhaba Aviation Pvt. Ltd.',
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

        'technologies': ['Python', 'Flask', 'JavaScript', 'SQL', 'Oracle ERP', 'Amadeus', 'Sabre', 'Galileo', 'Django',
                         'Git', 'HTML5', 'CSS3'],

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
            'contact_number': '+351 9XX XXX XXX'
        },

        'links': {
            'linkedin': 'https://www.linkedin.com/feed/',
            'github': 'https://github.com/your-profile',
            'email': 'mailto:eman.awad.hamdaan.pt@gmail.com'
        }
    }
    return render_template('index.html', **context)


# ===== CONTACT ROUTE (Using smtplib with better error handling) =====
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
                           title='Operations & Business Support Manager')


if __name__ == '__main__':
    app.run(debug=True)