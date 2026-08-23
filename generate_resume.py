from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

content = '''ERICK JAMES SIBAYAN
Data Analyst | Python | SQL | ML | Data Pipeline
Dagupan, Pangasinan | +63 968 207 3973 | erickjamessibayan2004@gmail.com | https://www.linkedin.com/in/erickjames-sibayan/

PROFESSIONAL SUMMARY
Computer Science student and part-time Junior Data Analyst with hands-on experience driving Amazon marketplace
performance through data-driven decision-making. Skilled in Python, SQL, and Excel automation for sales.

TECHNICAL SKILLS
Data & Analytics : SQL · Python · Excel (Power Query, Pivot Tables, VLOOKUP) · Statistical Analysis · Data Cleaning
Visualization & BI: Power BI (basic) · Tableau (basic) · Lucidchart · Figma
Programming : Python · SQL · JavaScript · Java · HTML/CSS · Golang · C++
Developer Tools : Git · GitLab · GitHub · VS Code · Cursor · IntelliJ IDEA · Antigravity IDE

EXPERIENCE
Product and Engineering — CloudSwyft Global Systems, Inc. (Internship)  June–July 2026
- Improved product positioning clarity by researching and documenting end-to-end platform workflows (news posting, SSON installation). Translating technical operations into stakeholder-ready data narratives for internal use.

Junior Data Analyst — Angry Orange (Part-time) Feb–May 2026
- Increased ASIN-level campaign profitability by 80% by writing SQL queries to extract Amazon sales data, applying statistical analysis to identify underperforming listings, and launching precision-targeted ad campaigns.
- Reduced daily and monthly reporting cycle time by consolidating raw Amazon exports into an automated Excel dashboard, delivering real-time sales performance insights to stakeholders.

Freelance Web Developer — 100 Degree Café Sept 2024–Oct 2024
- Grew estimated online customer engagement by 40% by designing and deploying a responsive website that improved digital visibility and gave customers direct access to menu and store information.

ACADEMIC PROJECTS
Philippine Food Price Forecasting System — Saint Louis University (May 2026)
Project Manager
- Built an ML pipeline forecasting Philippine food prices across 4 commodity groups using XGBoost, Optuna, and MAPIE conformal prediction — 90.9% coverage, RMSE ₱7.43, with a dashboard for 2050 climate scenarios.

Job Networking App (TrabaguioHanap) — Saint Louis University (March 2025)
Frontend & Backend Developer
- Reduced job search friction for Baguio-based students by building a full-stack job platform with user flows for job searching, profile management, and application tracking — handling both frontend design and backend logic.

CERTIFICATIONS
- Product and Engineering (Cloudswfyt) - July 2026
- Foundation of Digital Marketing and E-Commerce (Coursera) - March 2026
- DICT Digital Careers Expo Baguio — August 2024
- Trend Micro Cyber Defense Society Conference — March 2024

EDUCATION
BS Computer Science · Saint Louis University 2023 – Present
- Dean’s Lister — 2023 to Present
'''

c = canvas.Canvas('resume.pdf', pagesize=letter)
width, height = letter
text = c.beginText(72, height - 72)
text.setFont('Helvetica-Bold', 14)

for line in content.split('\n'):
    if line.strip() == '':
        text.textLine('')
    else:
        # Use bold for section headers
        if line.isupper() and len(line.split()) < 6:
            text.setFont('Helvetica-Bold', 12)
            text.textLine(line)
            text.setFont('Helvetica', 10)
        else:
            text.textLine(line)

c.drawText(text)
c.save()
print('Generated resume.pdf')
