import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib import colors

def build_pdf(filename="resume.pdf"):
    # Target page width = 612pt, height = 792pt (letter)
    # Margins: 36pt (0.5 inch) top/bottom, 40pt left/right
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=32,
        bottomMargin=32
    )

    styles = getSampleStyleSheet()

    # Custom typography styles
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#000000')
    )

    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#222222')
    )

    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#333333')
    )

    section_heading_style = ParagraphStyle(
        'SectionHeadingStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#000000')
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.8,
        leading=11.8,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#222222')
    )

    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.6,
        leading=11.5,
        alignment=TA_LEFT,
        leftIndent=12,
        firstLineIndent=-8,
        textColor=colors.HexColor('#222222')
    )

    left_heading_style = ParagraphStyle(
        'LeftHeadingStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#000000')
    )

    right_heading_style = ParagraphStyle(
        'RightHeadingStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.8,
        leading=12,
        alignment=TA_RIGHT,
        textColor=colors.HexColor('#333333')
    )

    role_sub_style = ParagraphStyle(
        'RoleSubStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#444444')
    )

    story = []

    # 1. Header
    story.append(Paragraph("ERICK JAMES SIBAYAN", name_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("Data Analyst &nbsp;|&nbsp; Python &nbsp;|&nbsp; SQL &nbsp;|&nbsp; ML &nbsp;|&nbsp; Data Pipeline", subtitle_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("Dagupan, Pangasinan &nbsp;|&nbsp; +63 968 207 3973 &nbsp;|&nbsp; erickjamessibayan2004@gmail.com &nbsp;|&nbsp; https://www.linkedin.com/in/erickjames-sibayan/", contact_style))
    story.append(Spacer(1, 6))

    # Helper function for section titles with line
    def add_section_header(title):
        story.append(Paragraph(title, section_heading_style))
        story.append(Spacer(1, 2))
        story.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor('#111111'), spaceBefore=1, spaceAfter=5))

    # 2. Professional Summary
    add_section_header("PROFESSIONAL SUMMARY")
    story.append(Paragraph("Computer Science student and part-time Junior Data Analyst with hands-on experience driving Amazon marketplace performance through data-driven decision-making. Skilled in Python, SQL, and Excel automation for sales.", body_style))
    story.append(Spacer(1, 6))

    # 3. Technical Skills
    add_section_header("TECHNICAL SKILLS")
    skills_data = [
        [Paragraph("<b>Data & Analytics</b> :", body_style), Paragraph("SQL &middot; Python &middot; Excel (Power Query, Pivot Tables, VLOOKUP) &middot; Statistical Analysis &middot; Data Cleaning", body_style)],
        [Paragraph("<b>Visualization & BI</b>:", body_style), Paragraph("Power BI (basic) &middot; Tableau (basic) &middot; Lucidchart &middot; Figma", body_style)],
        [Paragraph("<b>Programming</b> :", body_style), Paragraph("Python &middot; SQL &middot; JavaScript &middot; Java &middot; HTML/CSS &middot; Golang &middot; C++", body_style)],
        [Paragraph("<b>Developer Tools</b> :", body_style), Paragraph("Git &middot; GitLab &middot; GitHub &middot; VS Code &middot; Cursor &middot; IntelliJ IDEA &middot; Antigravity IDE", body_style)],
    ]
    skills_table = Table(skills_data, colWidths=[110, 422])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 6))

    # 4. Experience
    add_section_header("EXPERIENCE")

    # Exp 1
    t1 = Table([
        [Paragraph("<b>Product and Engineering</b> &nbsp;&nbsp;&nbsp; CloudSwyft Global Systems, Inc. <i>(Internship)</i>", left_heading_style),
         Paragraph("June&ndash; July 2026", right_heading_style)]
    ], colWidths=[380, 152])
    t1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t1)
    story.append(Paragraph("&bull; &nbsp; Improved product positioning clarity by researching and documenting end-to-end platform workflows (news posting, SSON installation).Translating technical operations into stakeholder ready data narratives for internal use.", bullet_style))
    story.append(Spacer(1, 5))

    # Exp 2
    t2 = Table([
        [Paragraph("<b>Junior Data Analyst</b> &nbsp;&nbsp;&nbsp; Angry Orange <i>(Part-time)</i>", left_heading_style),
         Paragraph("Feb &ndash; May 2026", right_heading_style)]
    ], colWidths=[380, 152])
    t2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t2)
    story.append(Paragraph("&bull; &nbsp; Increased ASIN-level campaign profitability by 80% by writing SQL queries to extract Amazon sales data, applying statistical analysis to identify underperforming listings, and launching precision-targeted ad campaigns.", bullet_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("&bull; &nbsp; Reduced daily and monthly reporting cycle time by consolidating raw Amazon exports into an automated Excel dashboard, delivering real-time sales performance insights to stakeholders.", bullet_style))
    story.append(Spacer(1, 5))

    # Exp 3
    t3 = Table([
        [Paragraph("<b>Freelance Web Developer</b> &nbsp;&nbsp;&nbsp; 100 Degree Caf&eacute;", left_heading_style),
         Paragraph("Sept 2024 &ndash; Oct 2024", right_heading_style)]
    ], colWidths=[380, 152])
    t3.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t3)
    story.append(Paragraph("&bull; &nbsp; Grew estimated online customer engagement by 40% by designing and deploying a responsive website that improved digital visibility and gave customers direct access to menu and store information.", bullet_style))
    story.append(Spacer(1, 6))

    # 5. Academic Projects
    add_section_header("ACADEMIC PROJECTS")

    # Proj 1
    tp1 = Table([
        [Paragraph("<b>Philippine Food Price Forecasting System</b> &nbsp;&nbsp;&nbsp; Saint Louis University", left_heading_style),
         Paragraph("May 2026", right_heading_style)]
    ], colWidths=[380, 152])
    tp1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(tp1)
    story.append(Paragraph("<i>Project Manager</i>", role_sub_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("&bull; &nbsp; Built an ML pipeline forecasting Philippine food prices across 4 commodity groups using XGBoost, Optuna, and MAPIE conformal prediction &mdash; 90.9% coverage, RMSE &#8369;7.43, with an dashboard for 2050 climate scenarios.", bullet_style))
    story.append(Spacer(1, 5))

    # Proj 2
    tp2 = Table([
        [Paragraph("<b>Job Networking App (TrabaguioHanap)</b> &nbsp;&nbsp;&nbsp; Saint Louis University", left_heading_style),
         Paragraph("March 2025", right_heading_style)]
    ], colWidths=[380, 152])
    tp2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(tp2)
    story.append(Paragraph("<i>Frontend &amp; Backend Developer</i>", role_sub_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("&bull; &nbsp; Reduced job search friction for Baguio-based students by building a full-stack job platform with user flows for job searching, profile management, and application tracking &mdash; handling both frontend design and backend logic.", bullet_style))
    story.append(Spacer(1, 6))

    # 6. Certifications
    add_section_header("CERTIFICATIONS")
    story.append(Paragraph("&bull; &nbsp; Product and Engineering (Cloudswfyt) - July 2026", bullet_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("&bull; &nbsp; Foundation of Digital Marketing and E-Commerce (Coursera) - March 2026", bullet_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("&bull; &nbsp; DICT Digital Careers Expo Baguio &mdash; August 2024", bullet_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("&bull; &nbsp; Trend Micro Cyber Defense Society Conference &mdash; March 2024", bullet_style))
    story.append(Spacer(1, 6))

    # 7. Education
    add_section_header("EDUCATION")
    te = Table([
        [Paragraph("<b>BS Computer Science</b> &middot; Saint Louis University", left_heading_style),
         Paragraph("2023 &ndash; Present", right_heading_style)]
    ], colWidths=[380, 152])
    te.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(te)
    story.append(Paragraph("&bull; &nbsp; Dean&rsquo;s Lister &mdash; 2023 to Present", bullet_style))

    doc.build(story)

if __name__ == "__main__":
    build_pdf("resume.pdf")
    print("resume.pdf successfully generated.")
