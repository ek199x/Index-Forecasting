import streamlit as st
import matplotlib.pyplot as plt
import joblib

st.set_page_config(initial_sidebar_state="expanded")
st.set_page_config(page_title = 'Resume')
st.image('Me.jpeg', width=400)


st.title('My Resume')
st.markdown('#### DATA SCIENCE | DATABASE DEVELOPMENT | DATA ANALYTICS')
st.write('Data Professional & Air Force Veteran, leveraging over 5 years of proven experience specializing in database development, systems administration, and secure communications. Proven ability to design, implement, and optimize SQL databases and automate workflows using Power Automate & PowerShell scripts, ability to build custom tools to support operational readiness and data-driven decision-making. Experienced in managing satellite communications networks and leading cross-functional teams in high-pressure environments. Adept at using software, programming languages, and scripting languages to develop dashboards, streamline reporting, and automate data integration. Career supported by the completion of a Master’s in Data Science. Create efficient processes to extract only actionable data! ')

col1, col2, col3 = st.columns(3)
col1.markdown(''' 
- Python/SQL/R
- Machine Learning
- Data Visualization
''')
col2.markdown(''' 
- English | Russian 
- Secure Communications
- Quality Assurance
''')
col3.markdown('''
- Data Analysis
- Policy Implementation
- Process Improvement 

''')

st.markdown('''
## Professional Experience:
#### United States Air Force | Various Locations | 2020 – Present
''')
with st.expander('Data Integration & Intelligence Manager - Human Resources Section'):
    st.markdown('''
- Integrated database solutions such as MS Access with automated tools in the MS Power suite as a pipeline for data used in executive level decision-making involving a team of 500+ reflected in 5 unique dashboards and over 20 dynamic data visualizations reporting on HR, financial, & operational data
- Created a streamlined employee onboarding process by designing and optimizing over 15 complex SQL queries, storing procedures and triggers to support critical data operations; automated over 20 repetitive workflows using Power Automate, improving processing speed by 80% 
- Innovated company policy by seeking process engineering opportunities resulting in reducing over 400 hours of manual input by collaborating with cross-functional teams to align data systems and automation products with organizational goals of HR
- Conducted internal data audits spanning over 4,000 records to ensure consistency and compliance with Air Force data standards resulting in a 100% pass rate on official Air Force audits 
- Taught critical database principles and fundamentals to HR team for use of new data tools for continuity operations resulting in documented development protocols to ensure maintainability and knowledge transfer

                ''')


with st.expander('Realtime Data Operations Manager - Satellite Communications Section'):
    st.markdown('''
- Spearheaded real-time data tracking for a 25-member team supporting 24/7 operations by designing and maintaining a custom database linked to an operational dashboard to enhance supervisory awareness and decision-making for maintenance and operations of satellite equipment
- Engineered automated data tools for metrics tracking and performance reporting, elevating awareness of equipment lifecycle stages within the work center increasing equipment turnover efficiency by 50% for over 1,000 distinct pieces of equipment
- Coordinated a $2M facility upgrade involving a complex power migration from main power to secondary and tertiary power sources in order to replace vital components providing electricity to overall communications systems using previously documented power-flow diagrams within the operational database
- Supervised personnel performing over 99K maintenance actions ensuring all activities accurately captured in maintenance database, resulting in communications support linked to missile defense operations for 31 allied nations
- Maintained a 24/7 schedule for crew operations providing non-stop mission critical communication operations for over 100 global teams focusing on diverse sets of tasks such as special warfare operations, counter-terrorism, and missile defense, ensuring all shifts were above critical staffing threshold


                ''')
   
with st.expander('IT Asset Manager & LMR Technician'):
    st.markdown('''
- Tracked and managed communications equipment inventory, reducing asset loss by 15% and led procurement efforts for new communications systems, aligning with the unique mission requirements of each agency present on base; conducted an inventory of 600 tactical radios supporting a $2.2M security upgrade initiative
- Developed and maintained a frequency management database, increasing record accuracy by 25% for 500+ radio frequency devices in use by first responders and operational agencies, ensuring compliance with federal communication standards 
- Provided technical guidance and trainings on radio frequency usage to base agencies, reducing radio frequency interference by 10% through education and proactive monitoring with spectrum analysis devices
- Maintained and repaired over 1K land mobile radio systems, achieving a 24-hour average resolution time; conducted preventative maintenance on 50+ transmission systems, reducing downtime by 95%
- Supported emergency deployments by setting up mobile communications platforms, boosting effectiveness by 50%; upgraded 500+ radios with secure encryption to enhance operational security
- Directed restoration of communications during IT outages affecting 14K personnel; created training materials for helicopter aircrews, improving readiness for over 700 missions

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



st.markdown('#### Allied Universal | New York, NY | 2018 – 2020')

with st.expander('Lead Airline Security Supervisor'):
    st.markdown('''
- Developed a comprehensive training program, reducing onboarding time by 50% and improving staff retention; managed scheduling and payroll for 50+ officers, eliminating errors and reducing labor disputes
- Reduced overtime costs by 20% through efficient scheduling and resource allocation; oversaw security screening procedures, ensuring compliance with TSA and FAA regulations
- Responded to incidents and escalated conflicts, ensuring a safe airport environment; led audits and inspections to assess and maintain security protocol effectiveness
- Provided on-the-job training and mentorship to new hires and team leads; facilitated communication between airport stakeholders to resolve operational issues
''')

st.markdown('''## Education | Certifications:''')

with st.expander('Masters of Science'):
    st.markdown('Data Science | Eastern University | Expected 2025')
with st.expander('Bachelors of Science'):
    st.markdown('Management Information Systems | University of Marlyand | 2023')
with st.expander('Associate of Science'):
    st.markdown('Electronic Systems Technology | Community College of the Air Force | 2021')
with st.expander('ITIL'):
    st.markdown('ITIL v4 Foundation | PeopleCert | 2025')
with st.expander('IAITAM'):
    st.markdown('Certified Software Asset Manager | IAITAM | 2025')
with st.expander('Service Now'):
    st.markdown('Certified System Administrator | Service Now | 2025')
with st.expander('Specialized Military Training '):
    st.markdown('''
                - Basic Leadership & Development  
                - Airman Leadership School 
                - Modernization of Enterprise Terminals Sustainment Course
                ''')
st.link_button('Download My Resume', 'https://docs.google.com/document/d/1PKOTTOiJ_xMRQA1-oR_vK4tjLFKfNUjZVR9es7WgU3w&export=download')
    
