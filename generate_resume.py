import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def create_resume_pdf(filename="Farrukh_Mumtaz_Resume.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=30,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()

    # Custom styles
    name_style = ParagraphStyle(
        'NameStyle',
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        alignment=1,
        textColor=colors.HexColor('#0d0f14')
    )

    contact_style = ParagraphStyle(
        'ContactStyle',
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        alignment=1,
        textColor=colors.HexColor('#333333')
    )

    heading_style = ParagraphStyle(
        'HeadingStyle',
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13,
        textColor=colors.HexColor('#0d0f14'),
        spaceBefore=5,
        spaceAfter=3
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        fontName='Helvetica',
        fontSize=8.8,
        leading=12.5,
        textColor=colors.HexColor('#222222')
    )

    bullet_style = ParagraphStyle(
        'BulletStyle',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#333333'),
        leftIndent=10,
        spaceAfter=1.5
    )

    story = []

    # Name
    story.append(Paragraph("<b>FARRUKH MUMTAZ</b>", name_style))
    story.append(Spacer(1, 3))
    
    # Contact
    contact_text = "+92 328 8271853 &nbsp;&nbsp;&diamond;&nbsp;&nbsp; Rahim Yar Khan, Punjab, Pakistan<br/>" \
                   "<font color='#0066cc'>farrukhmumtaz.ai@gmail.com</font> &nbsp;&nbsp;&diamond;&nbsp;&nbsp; " \
                   "<font color='#0066cc'>linkedin.com/in/farrukh-ai-developer</font>"
    story.append(Paragraph(contact_text, contact_style))
    story.append(Spacer(1, 5))

    def add_section(title):
        story.append(Paragraph(f"<b>{title.upper()}</b>", heading_style))
        story.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor('#666666'), spaceAfter=4, spaceBefore=2))

    # Objective
    add_section("Objective")
    story.append(Paragraph("Graduate in BS Artificial Intelligence with a 3.5/4.0 CGPA and a passion for building intelligent systems that solve real-world problems. Hands-on experience in Machine Learning, Deep Learning, Natural Language Processing, and Computer Vision.", body_style))
    story.append(Spacer(1, 3))

    # Experience
    add_section("Experience")
    story.append(Paragraph("<b>AI Developer</b> &ndash; SMJSols <font color='#555555' size=8.5>Present</font>", body_style))
    story.append(Paragraph("&bull; Developing production-grade artificial intelligence models, computer vision systems, and ML pipelines.", bullet_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>AI Developer Intern</b> &ndash; Aixon (Onsite) <font color='#555555' size=8.5>2025</font>", body_style))
    story.append(Paragraph("&bull; Developed real-time object detection systems using YOLO and benchmarked Vision-Language Models (VLLMs).", bullet_style))
    story.append(Spacer(1, 3))

    # Education
    add_section("Education")
    story.append(Paragraph("<b>BS Artificial Intelligence</b> <font color='#555555' size=8.5>2022 &ndash; 2026</font><br/>"
                           "Khawaja Fareed University of Engineering & IT, Rahim Yar Khan | CGPA: 3.50 / 4.0", body_style))
    story.append(Spacer(1, 2))

    story.append(Paragraph("<b>FSc Pre-Medical</b> <font color='#555555' size=8.5>2019 &ndash; 2021</font><br/>"
                           "Punjab Group of College, Sadiqabad | Marks: 917 / 1100", body_style))
    story.append(Spacer(1, 2))

    story.append(Paragraph("<b>Matriculation</b> <font color='#555555' size=8.5>2017 &ndash; 2019</font><br/>"
                           "Govt Secondary School Kotla Hiyat | Marks: 998 / 1100", body_style))
    story.append(Spacer(1, 3))

    # Skills
    add_section("Skills")
    skills_text = "<b>Programming:</b> Python &nbsp;|&nbsp; <b>ML/DL:</b> Supervised/Unsupervised Learning, CNNs, Transformers<br/>" \
                  "<b>Computer Vision:</b> YOLO, Object Detection, Classification &nbsp;|&nbsp; <b>NLP/GenAI:</b> LLMs, RAG, Fine-tuning, Voice Cloning<br/>" \
                  "<b>Tools & Deployment:</b> PyTorch, TensorFlow, Hugging Face, OpenCV, FastAPI, REST APIs"
    story.append(Paragraph(skills_text, body_style))
    story.append(Spacer(1, 3))

    # Projects
    add_section("Key AI Projects")
    
    projects = [
        ("AI Employee Suite", "Autonomous multi-agent workforce suite for enterprise task delegation, document processing, and workflow automation."),
        ("AI Twin System (Final Year Project)", "Voice cloning & conversational mimicry using fine-tuned Transformers, RAG, and NLP speech pipeline."),
        ("WhatsApp Bot for Businesses", "Automated customer support & order management chatbot integrated with WhatsApp API and NLP intent parsing."),
        ("Android Security App", "Real-time mobile security scanner and malware behavior analyzer for Android devices."),
        ("AI Resume Analyzer", "Automated resume parsing and job description matching using NLP embeddings and LLMs."),
        ("AI Emotion Detector", "Real-time facial expression and micro-emotion recognition system using deep CNNs and OpenCV."),
        ("AI Inventory Management", "Demand forecasting and automated stock replenishment system using time-series ML models."),
        ("Stock Recommender System", "Predictive market analyzer leveraging historical financial data and LSTM neural networks."),
        ("Smart Parking Booking System", "Slot reservation platform integrated with real-time camera occupancy tracking."),
        ("Fire Detector & Alarm System", "Real-time computer vision system for early flame and smoke detection with automated alerts.")
    ]

    for title, desc in projects:
        story.append(Paragraph(f"<b>&bull; {title}:</b> {desc}", bullet_style))

    story.append(Spacer(1, 3))

    # Achievements
    add_section("Achievements")
    story.append(Paragraph("&bull; Dean's Honor Award for Academic Excellence in Artificial Intelligence.", bullet_style))
    story.append(Paragraph("&bull; AI Developer at SMJSols & completed Industry AI Internship at Aixon.", bullet_style))

    doc.build(story)
    print(f"Resume regenerated successfully as {filename}")

if __name__ == "__main__":
    create_resume_pdf()
