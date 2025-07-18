import streamlit as st
import matplotlib.pyplot as plt
import joblib

st.set_page_config(page_title = 'Resume')
st.image('Me.jpeg', width=400)


st.title('My Resume')
st.markdown('#### DATA SCIENCE| DATABASE DEVELOPMENT| DATA ANALYTICS')
st.write('Data Professional & Air Force Veteran, leveraging over 5 years of proven experience specializing in database development, systems administration, and secure communications. Proven ability to design, implement, and optimize SQL databases and automate workflows using Power Automate & PowerShell scripts, ability to build custom tools to support operational readiness and data-driven decision-making. Experienced in managing satellite communications networks and leading cross-functional teams in high-pressure environments. Adept at using software, programming languages, and scripting languages to develop dashboards, streamline reporting, and automate data integration. Career supported by the completion of a Master’s in Data Science. Create efficient processes to extract only actionable data! ')
st.markdown('''## Education | Certifications:''')

with st.expander('Masters of Science'):
    st.markdown('Data Science | Eastern University | Expected 2025')
with st.expander('Bachelors of Science'):
    st.markdown('Management Information Systems | University of Marlyand | 2023')
with st.expander('Associate of Science'):
    st.markdown('Electronic Systems Technology | Community College of the Air Force | 2021')
with st.expander('ITIL'):
    st.markdown('ITIL v4 Foundation | PeopleCert | 2025')
with st.expander('IATAM'):
    st.markdown('Certified Software Asset Manager | IAITAM | 2025')
with st.expander('Specialized Military Training '):
    st.markdown('''
                - Basic Leadership & Development  
                - Airman Leadership School 
                - Modernization of Enterprise Terminals Sustainment Course
                ''')

st.markdown('''
## Professional Experience:
#### United States Air Force | Various Locations | 2020 – Present
''')
with st.expander('Database Developer'):
    st.markdown('''
- Designed and optimized complex SQL queries, stored procedures, and triggers to support critical data operations; automated repetitive workflows using Power Automate, improving processing speed and accuracy
- Integrated database solutions with automated reporting tools to streamline decision-making; built and maintained dashboards and data visualizations using Excel and Power BI for leadership briefings
- Analyzed business processes to identify automation opportunities and reduce manual input; collaborated with cross-functional teams to align data systems with organizational goals
- Conducted regular data audits to ensure consistency and compliance with Air Force data standards; improved data transfer processes, decreasing turnaround times by 40
- Provided technical support and training on new data tools to end-users; documented development protocols to ensure maintainability and knowledge transfer
                ''')


with st.expander('SATCOM Gateway Supervisor'):
    st.markdown('''
- Managed and maintained satellite communication systems, ensuring 99.9% system availability for global operations; supervised a team of 6 technicians in operating the most diverse satellite gateway in U.S. Air Forces Europe
- Troubleshot, repaired, and inspected equipment, reducing communication failures by 30%; coordinated a $2M facility upgrade project, completing a power migration with no operational delays
- Oversaw 99K maintenance actions, maintaining near-perfect uptime for a U.S. Navy missile defense mission; restored missile communication capabilities within 72 hours after a critical power outage affecting 31 allied nations
- Authored automated tools for metrics tracking and reporting, improving situational awareness; eliminated a 4-year hazardous materials issue, saving $500K and ensuring site safety for 6K personnel
- Delivered 130 configuration updates, cutting system recovery time by 1.5 hours; facilitated multilingual communications, enhancing coordination with allied forces during crisis response

                ''')
   
with st.expander('IT Asset Manager/Interim Spectrum Manager'):
    st.markdown('''
- Developed and maintained a frequency management database, increasing record accuracy by 25%; oversaw 500+ radio frequency devices, ensuring compliance with federal communication standards
- Conducted spectrum usage audits and regulatory reviews to maintain mission readiness; automated IT service request workflows halving the average response time
- Tracked and managed communications equipment inventory, reducing asset loss by 15%; led procurement efforts for new communications systems, aligning with mission requirements
- Provided technical guidance on radio frequency usage to units across the base; reduced radio frequency interference by 10% through proactive monitoring and coordination
- Developed compliance documentation for audits and inspections; served as acting Spectrum Manager during staffing gaps, maintaining uninterrupted operations
                ''')
    
with st.expander('Emergency Action Controller'):
    st.markdown(
        '''
- Executed over 50 emergency evacuations for medical and casualty events with zero delay; managed logistics support for emergency responses, cutting delivery time by 30%
- Developed and maintained the base crisis communication plan, improving inter-agency coordination; monitored base-wide alarm systems and executed emergency protocols during high-risk scenarios
- Served as a central point of contact for command post operations during 24/7 shifts; disseminated time-sensitive alerts and orders to leadership and first responders
- Coordinated responses to natural disasters and exercises with local and federal agencies; tracked real-time mission statuses across multiple units, providing immediate updates to leadership
- Conducted regular drills to ensure base personnel were trained in emergency response protocols; maintained communication systems to support uninterrupted command and control during crises
'''
    )

with st.expander('Radio Frequency Transmission Systems Technician'):
    st.markdown(
        '''
- Maintained and repaired over 1K land mobile radio systems, achieving a 24-hour average resolution time; conducted preventative maintenance on 50+ transmission systems, reducing downtime by 95%
- Supported emergency deployments by setting up mobile communications platforms, boosting effectiveness by 50%; upgraded 500+ radios with secure encryption to enhance operational security
- Managed the frequency allocation program for 25 tenant units and over 15K records; conducted an inventory of 600 tactical radios supporting a $2.2M security upgrade initiative
- Directed restoration of communications during IT outages affecting 14K personnel; created training materials for helicopter aircrews, improving readiness for over 700 missions
- Coordinated audio-visual support for ceremonies and official events at the Wing level; streamlined the service request process, reducing technician workload and improving service delivery by 60%

'''
    )


st.markdown('#### Allied Universal | New York, NY | 2018 – 2020')

with st.expander('Lead Airline Security Supervisor'):
    st.markdown('''
- Developed a comprehensive training program, reducing onboarding time by 50% and improving staff retention; managed scheduling and payroll for 50+ officers, eliminating errors and reducing labor disputes
- Reduced overtime costs by 20% through efficient scheduling and resource allocation; oversaw security screening procedures, ensuring compliance with TSA and FAA regulations
- Responded to incidents and escalated conflicts, ensuring a safe airport environment; led audits and inspections to assess and maintain security protocol effectiveness
- Provided on-the-job training and mentorship to new hires and team leads; facilitated communication between airport stakeholders to resolve operational issues
- Improved reporting accuracy by implementing a digital tracking system for incidents and patrol logs; assisted in the coordination of emergency response drills and real-world incidents

''')

st.markdown('### Technical Competencies')
with st.expander('Data Analysis & Programming'):
    st.markdown('Python | SQL | R | Tableau | Power BI | Excel')
with st.expander('IT & Networking'):
    st.markdown('Network configuration & troubleshooting | Systems Maintenance | Radio Frequency Communications')
with st.expander ('Project Management'):
    st.markdown('Agile methodologies | Database Management | Process Automation')
