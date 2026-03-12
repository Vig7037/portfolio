import base64
import streamlit as st
from streamlit_timeline import timeline
from PIL import Image

# Set page config
st.set_page_config(page_title="Vighnesh Singhal | Portfolio", layout="wide", page_icon="👨‍💻")

# Load images
image = Image.open(r"content/profile.png")
nss = Image.open(r"content/nss.jpg")
tbi = Image.open(r"content/tbi.png")
aci = Image.open(r"content/aci.jpg")
research = Image.open(r"content/research.png")
iit = Image.open(r"content/iit.png")

# Load GIF demo (base64 for inline HTML rendering)
with open(r"content/Demo.gif", "rb") as _f:
    gif_b64 = base64.b64encode(_f.read()).decode()

# Custom CSS
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

        header[data-testid="stHeader"] { display: none; }
        .block-container { padding-top: 0rem !important; }

        .navbar {
            position: sticky;
            top: 0;
            z-index: 9999;
            background: rgba(10, 10, 20, 0.92);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(99,179,237,0.15);
            padding: 0.75rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 2rem;
        }
        .nav-brand {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            font-size: 1.25rem;
            color: #63B3ED;
            letter-spacing: -0.02em;
        }
        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
            margin: 0;
            padding: 0;
        }
        .nav-links a {
            font-family: 'Inter', sans-serif;
            font-size: 0.875rem;
            font-weight: 500;
            color: #CBD5E0;
            text-decoration: none;
            transition: color 0.2s;
            letter-spacing: 0.02em;
        }
        .nav-links a:hover { color: #63B3ED; }

        body, .stApp {
            background: #0D0D1A;
            font-family: 'Inter', sans-serif;
            color: #E2E8F0;
        }

        .hero-greeting {
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            font-weight: 500;
            color: #63B3ED;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 0.5rem;
        }
        .hero-name {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 3.5rem;
            font-weight: 700;
            color: #F7FAFC;
            line-height: 1.1;
            margin-bottom: 0.75rem;
            letter-spacing: -0.03em;
        }
        .hero-name span { color: #63B3ED; }
        .hero-tagline {
            font-size: 1.1rem;
            color: #A0AEC0;
            line-height: 1.7;
            max-width: 520px;
            margin-bottom: 1.5rem;
        }

        .section-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.75rem;
            font-weight: 700;
            color: #F7FAFC;
            margin-top: 3rem;
            margin-bottom: 1.25rem;
            padding-bottom: 0.6rem;
            border-bottom: 2px solid #63B3ED;
            letter-spacing: -0.02em;
        }
        .section-title::before {
            content: '';
            display: inline-block;
            width: 10px;
            height: 10px;
            background: #63B3ED;
            border-radius: 50%;
            margin-right: 0.6rem;
            vertical-align: middle;
        }

        .skills-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin-bottom: 1rem;
        }
        .skill-pill {
            background: rgba(99,179,237,0.1);
            border: 1px solid rgba(99,179,237,0.3);
            color: #63B3ED;
            padding: 0.35rem 0.9rem;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 500;
        }
        .skill-group-label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: #718096;
            margin-bottom: 0.4rem;
            margin-top: 1rem;
        }

        .exp-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.07);
            border-left: 3px solid #63B3ED;
            border-radius: 10px;
            padding: 1.25rem 1.5rem;
            margin-bottom: 1.25rem;
        }
        .exp-card h3 {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.05rem;
            font-weight: 600;
            color: #F7FAFC;
            margin: 0 0 0.3rem;
        }
        .exp-date {
            font-size: 0.8rem;
            color: #63B3ED;
            font-weight: 500;
            margin-bottom: 0.6rem;
        }
        .exp-card p {
            font-size: 0.9rem;
            color: #A0AEC0;
            line-height: 1.65;
            margin: 0;
        }
        .exp-badge {
            display: inline-block;
            background: rgba(99,179,237,0.12);
            color: #63B3ED;
            font-size: 0.75rem;
            font-weight: 600;
            padding: 0.2rem 0.65rem;
            border-radius: 4px;
            margin-bottom: 0.5rem;
        }
        .achievement-badge {
            display: inline-block;
            background: rgba(246,173,85,0.15);
            color: #F6AD55;
            font-size: 0.75rem;
            font-weight: 600;
            padding: 0.2rem 0.65rem;
            border-radius: 4px;
            margin-bottom: 0.5rem;
        }
        .achievement-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.07);
            border-left: 3px solid #F6AD55;
            border-radius: 10px;
            padding: 1.25rem 1.5rem;
            margin-bottom: 1.25rem;
        }
        .achievement-card h3 {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.05rem;
            font-weight: 600;
            color: #F7FAFC;
            margin: 0 0 0.3rem;
        }
        .achievement-card .exp-date { color: #F6AD55; }
        .achievement-card p {
            font-size: 0.9rem;
            color: #A0AEC0;
            line-height: 1.65;
            margin: 0;
        }
        .trophy-stat {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            background: rgba(246,173,85,0.1);
            border: 1px solid rgba(246,173,85,0.3);
            color: #F6AD55;
            padding: 0.3rem 0.8rem;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 600;
            margin-top: 0.6rem;
        }

        .pub-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.07);
            border-radius: 10px;
            padding: 1.25rem 1.5rem;
            margin-bottom: 1rem;
        }
        .pub-card p {
            font-size: 0.875rem;
            color: #CBD5E0;
            line-height: 1.7;
            margin: 0;
        }
        .pub-card a {
            color: #63B3ED;
            text-decoration: none;
        }

        .cert-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.07);
            border-left: 3px solid #48BB78;
            border-radius: 8px;
            padding: 0.85rem 1.2rem;
            margin-bottom: 0.75rem;
            font-size: 0.9rem;
            color: #CBD5E0;
        }
        .cert-card::before {
            content: '✓ ';
            color: #48BB78;
            font-weight: 700;
        }

        /* ── CONTACT ── */
        .contact-wrapper {
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.07);
            border-radius: 14px;
            padding: 2rem 2rem 1.5rem;
            max-width: 500px;
        }
        .contact-label {
            font-size: 0.78rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: #718096;
            margin-bottom: 0.35rem;
            margin-top: 1rem;
        }
        .contact-input {
            width: 100%;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 8px;
            padding: 0.75rem 1rem;
            color: #E2E8F0;
            font-size: 0.9rem;
            margin-bottom: 0.2rem;
            outline: none;
            transition: border-color 0.2s;
            box-sizing: border-box;
        }
        .contact-input:focus { border-color: #63B3ED; }
        .btn-send {
            background: linear-gradient(135deg, #3B82F6, #1D4ED8);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.8rem 2rem;
            font-size: 0.95rem;
            font-weight: 600;
            cursor: pointer;
            width: 100%;
            margin-top: 1.2rem;
            letter-spacing: 0.02em;
            transition: opacity 0.2s;
        }
        .btn-send:hover { opacity: 0.88; }

        .contact-info-block {
            display: flex;
            flex-direction: column;
            gap: 1rem;
            padding: 1.5rem 0;
        }
        .contact-info-item {
            display: flex;
            align-items: center;
            gap: 0.85rem;
            color: #CBD5E0;
            font-size: 0.9rem;
        }
        .contact-info-icon {
            width: 38px;
            height: 38px;
            background: rgba(99,179,237,0.1);
            border: 1px solid rgba(99,179,237,0.25);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
            flex-shrink: 0;
        }
        .contact-info-item a {
            color: #63B3ED;
            text-decoration: none;
        }
        .contact-info-item a:hover { text-decoration: underline; }

        .footer {
            margin-top: 4rem;
            text-align: center;
            color: #4A5568;
            font-size: 0.85rem;
            padding-bottom: 2rem;
        }

        .anchor-target { scroll-margin-top: 70px; }
    </style>
""", unsafe_allow_html=True)

# ─── NAVIGATION BAR ───────────────────────────────────────────────────────────
st.markdown("""
<nav class="navbar">
    <div class="nav-brand">VS</div>
    <ul class="nav-links">
        <li><a href="#about">About</a></li>
        <li><a href="#experience">Experience</a></li>
        <li><a href="#projects">Projects</a></li>
        <li><a href="#achievements">Achievements</a></li>
        <li><a href="#research">Research</a></li>
        <li><a href="#contact">Contact</a></li>
    </ul>
</nav>
""", unsafe_allow_html=True)

# ─── HERO / ABOUT ─────────────────────────────────────────────────────────────
st.markdown('<div class="anchor-target" id="about"></div>', unsafe_allow_html=True)

c1, c2 = st.columns([1.3, 1])

with c1:
    st.markdown('<p class="hero-greeting">👋 Hello, I\'m</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-name">Vighnesh<br><span>Singhal</span></h1>', unsafe_allow_html=True)
    st.markdown('''<p class="hero-tagline">
        Computer Science Engineer specializing in <strong style="color:#63B3ED;">Computer Vision</strong>
        and <strong style="color:#63B3ED;">Multimodal AI</strong>.
        I build intelligent systems — from gesture recognition to automated OMR scanners —
        that bridge the gap between research and real-world impact.
    </p>''', unsafe_allow_html=True)

    lc1, lc2, lc3 = st.columns(3)
    with lc1:
        st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/vighnesh-singhal-33b792244/", type="primary")
    with lc2:
        st.link_button("🐙 GitHub", "https://github.com/Vig7037", type="primary")
    with lc3:
        st.link_button("🌐 Portfolio", "https://vighneshportfolio.streamlit.app/")

with c2:
    st.image(image, width=340)

# ─── SKILLS ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)

sc1, sc2 = st.columns(2)

with sc1:
    st.markdown('<p class="skill-group-label">Programming Languages</p>', unsafe_allow_html=True)
    st.markdown('''<div class="skills-grid">
        <span class="skill-pill">Python</span>
        <span class="skill-pill">SQL</span>
        <span class="skill-pill">Bash</span>
        <span class="skill-pill">C++</span>
    </div>''', unsafe_allow_html=True)

    st.markdown('<p class="skill-group-label">CV & Deep Learning Frameworks</p>', unsafe_allow_html=True)
    st.markdown('''<div class="skills-grid">
        <span class="skill-pill">OpenCV</span>
        <span class="skill-pill">PyTorch</span>
        <span class="skill-pill">TorchVision</span>
        <span class="skill-pill">Mediapipe</span>
        <span class="skill-pill">OpenVINO</span>
        <span class="skill-pill">Unsloth</span>
    </div>''', unsafe_allow_html=True)

    st.markdown('<p class="skill-group-label">Vision Models</p>', unsafe_allow_html=True)
    st.markdown('''<div class="skills-grid">
        <span class="skill-pill">YOLOv8</span>
        <span class="skill-pill">R-CNN</span>
        <span class="skill-pill">ResNet</span>
        <span class="skill-pill">ViT</span>
        <span class="skill-pill">SAM3</span>
    </div>''', unsafe_allow_html=True)

with sc2:
    st.markdown('<p class="skill-group-label">Annotation & CV Tools</p>', unsafe_allow_html=True)
    st.markdown('''<div class="skills-grid">
        <span class="skill-pill">CVAT</span>
        <span class="skill-pill">Roboflow</span>
        <span class="skill-pill">Label Studio</span>
    </div>''', unsafe_allow_html=True)

    st.markdown('<p class="skill-group-label">DevOps & Tools</p>', unsafe_allow_html=True)
    st.markdown('''<div class="skills-grid">
        <span class="skill-pill">Docker</span>
        <span class="skill-pill">Git</span>
        <span class="skill-pill">GitHub</span>
        <span class="skill-pill">VS Code</span>
        <span class="skill-pill">SQLite</span>
        <span class="skill-pill">Google Colab</span>
    </div>''', unsafe_allow_html=True)

    st.markdown('<p class="skill-group-label">AI / LLM</p>', unsafe_allow_html=True)
    st.markdown('''<div class="skills-grid">
        <span class="skill-pill">Langchain</span>
        <span class="skill-pill">Agno</span>
        <span class="skill-pill">RAG</span>
        <span class="skill-pill">Ollama</span>
        <span class="skill-pill">FastMCP</span>
        <span class="skill-pill">NVIDIA NIM</span>
    </div>''', unsafe_allow_html=True)

# ─── EXPERIENCE ───────────────────────────────────────────────────────────────
st.markdown('<div class="anchor-target" id="experience"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Experience</div>', unsafe_allow_html=True)

ec1, ec2 = st.columns([1, 1.6])
with ec1:
    st.image(iit, use_container_width=True)
with ec2:
    st.markdown('''<div class="exp-card">
    <span class="exp-badge">Internship</span>
    <h3>Intern – Multimodal AI & Data Automation</h3>
    <p class="exp-date">📍 IIT Mandi iHub and HCI Foundation &nbsp;|&nbsp; Sep 2025 – Jan 2026 &nbsp;|&nbsp; Mandi, Himachal Pradesh</p>
    <p>
        Researched robust Multimodal AI models to automate fusion of RGB and Depth data.
        Conducted extensive research on dynamic hand gesture recognition, developing a dataset to identify key user patterns.
        Collaborated with a cross-functional team of researchers and engineers to integrate multimodal fusion modules.
    </p>
    </div>''', unsafe_allow_html=True)

st.markdown('''<div class="exp-card">
    <span class="exp-badge">Internship</span>
    <h3>Software Development Intern – Automation & Computer Vision</h3>
    <p class="exp-date">📍 Examination Cell, Graphic Era Hill University &nbsp;|&nbsp; May 2025 – Sep 2025 &nbsp;|&nbsp; Dehradun, India</p>
    <p>
        Engineered an automated Technical Data Extraction tool (OMR), replacing manual entry with 99%+ accuracy.
        Implemented robust image recognition algorithms to ensure reliability in digitizing physical records.
        Architected and deployed an automated data pipeline under direct faculty supervision.
    </p>
</div>''', unsafe_allow_html=True)

ec1, ec2 = st.columns([1, 1.6])
with ec1:
    st.image(tbi, use_container_width=True)
with ec2:
    st.markdown('''<div class="exp-card" style="margin-top:0">
    <span class="exp-badge">Research Intern</span>
    <h3>Research Intern – Technology Business Incubator</h3>
    <p class="exp-date">📍 TBI-GEU, Graphic Era Deemed to be University &nbsp;|&nbsp; Jul 2024 – Oct 2024</p>
    <p>
        Selected as a Research Intern at TBI-GEU. Worked in hybrid mode on research-aligned tasks and expectations
        outlined during the internship process. Demonstrated enthusiasm that impressed the evaluation panel.
    </p>
</div>''', unsafe_allow_html=True)

ec1, ec2 = st.columns([1, 1.6])
with ec1:
    st.image(nss, use_container_width=True)
with ec2:
    st.markdown('''<div class="exp-card" style="margin-top:0">
    <span class="exp-badge">Volunteer</span>
    <h3>NSS Volunteer</h3>
    <p class="exp-date">📍 Graphic Era Deemed to be University &nbsp;|&nbsp; Oct 2022 – Feb 2024</p>
    <p>
        Coordinated numerous campus events, achieving a 30% rise in event attendance.
        Earned accolades for exceptional organizational skills and community engagement.
        Awarded the NSS B Certificate (National Service Scheme).
    </p>
</div>''', unsafe_allow_html=True)

# ─── PROJECTS ─────────────────────────────────────────────────────────────────
st.markdown('<div class="anchor-target" id="projects"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)

with st.spinner("Building project timeline..."):
    with open(r'content/timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=520)

st.markdown("#### Latest Projects", unsafe_allow_html=False)

# ── Featured: Dynamic Gesture Recognition (with live demo GIF) ──
fg1, fg2 = st.columns([1, 1.4])
with fg1:
    st.markdown(f'''
    <div style="border-radius:12px; overflow:hidden; border:1px solid rgba(99,179,237,0.2); position:relative;">
        <img src="data:image/gif;base64,{gif_b64}" style="width:100%; display:block;" alt="Gesture Recognition Demo">
        <div style="position:absolute; top:10px; left:10px; background:rgba(10,10,20,0.75);
                    backdrop-filter:blur(6px); padding:0.25rem 0.65rem; border-radius:999px;
                    font-size:0.75rem; font-weight:600; color:#63B3ED; border:1px solid rgba(99,179,237,0.4);">
            ▶ Live Demo
        </div>
    </div>
    ''', unsafe_allow_html=True)

with fg2:
    st.markdown('''
    <div class="exp-card" style="margin-top:0; border-left-color:#63B3ED;">
        <span class="exp-badge">⭐ Featured · IIT Mandi Internship</span>
        <h3>Dynamic Hand Gesture Recognition</h3>
        <p class="exp-date">Sep 2025 – Jan 2026 &nbsp;|&nbsp; IIT Mandi iHub & HCI Foundation</p>
        <p>
            Built a real-time gesture recognition system using a CNN pipeline with mid-level RGB-D sensor fusion.
            The model runs at <strong style="color:#F7FAFC;">21+ FPS</strong> with
            <strong style="color:#F7FAFC;">97.3% confidence</strong> on live webcam input —
            detecting gestures like WAVE across 70-frame sliding windows.
            Achieved <strong style="color:#F7FAFC;">95.7% learning performance</strong> using
            optimized augmentation and segmentation techniques on a custom-built dataset.
        </p>
        <div class="skills-grid" style="margin-top:0.85rem;">
            <span class="skill-pill" style="font-size:0.75rem;">Python</span>
            <span class="skill-pill" style="font-size:0.75rem;">PyTorch</span>
            <span class="skill-pill" style="font-size:0.75rem;">OpenCV</span>
            <span class="skill-pill" style="font-size:0.75rem;">ResNet</span>
            <span class="skill-pill" style="font-size:0.75rem;">LSTM</span>
            <span class="skill-pill" style="font-size:0.75rem;">OpenVINO</span>
            <span class="skill-pill" style="font-size:0.75rem;">RTX-5090</span>
        </div>
    </div>
    ''', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Other Projects ──
proj_cols = st.columns(2)

projects = [
    {
        "title": "OMR Scanner",
        "period": "May 2025 – Aug 2025",
        "desc": "Automated OMR Data Extraction System processing 1000+ sheets/hour. Advanced camera alignment correction algorithms achieving 99%+ accuracy.",
        "tech": ["Python", "OpenCV", "PyQt5", "Pandas", "NumPy"]
    },
    {
        "title": "Go Kart Count",
        "period": "Dec 2024 – Apr 2025",
        "desc": "Kalman filter pipeline to track vehicle count on a go-kart track. Image subtraction algorithm for position analysis.",
        "tech": ["Python", "OpenCV", "Kalman Filter", "Image Subtraction"]
    },
]

for col, proj in zip(proj_cols, projects):
    with col:
        pills = "".join([f'<span class="skill-pill" style="font-size:0.75rem;">{t}</span>' for t in proj["tech"]])
        st.markdown(f'''
        <div class="exp-card" style="height:100%">
            <h3 style="font-size:0.95rem;">{proj["title"]}</h3>
            <p class="exp-date">{proj["period"]}</p>
            <p style="margin-bottom:0.75rem;">{proj["desc"]}</p>
            <div class="skills-grid">{pills}</div>
        </div>
        ''', unsafe_allow_html=True)

# ─── ACHIEVEMENTS ─────────────────────────────────────────────────────────────
st.markdown('<div class="anchor-target" id="achievements"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Achievements</div>', unsafe_allow_html=True)

# Hackathon — Project Showcase
ah1, ah2 = st.columns([1, 1.6])
with ah1:
    st.image(aci, use_container_width=True)
with ah2:
    st.markdown('''<div class="achievement-card" style="margin-top:0">
    <span class="achievement-badge">🏆 Top 5 Finish</span>
    <h3>🚀 Project Showcase Hackathon</h3>
    <p class="exp-date">⏱️ 8-Hour Hackathon &nbsp;|&nbsp; Graphic Era Deemed to be University</p>
    <p>
        Participated in the <strong style="color:#F7FAFC;">Project Showcase</strong> — an intensive 8-hour hackathon
        that challenged participants to ideate, build, and present a fully functional product under time pressure.
        Developed an AI-powered <strong style="color:#F7FAFC;">Trip Planning Assistant for Uttarakhand</strong>
        leveraging NVIDIA's NIM platform and the Llama3-70b-instruct model, featuring real-time AI-generated
        itineraries and context-aware travel recommendations built on a Streamlit interface.
    </p>
    <div style="margin-top:0.85rem; display:flex; gap:0.65rem; flex-wrap:wrap;">
        <span class="trophy-stat">🥇 Top 5 out of all participants</span>
        <span class="trophy-stat">⏱️ 8 Hours</span>
        <span class="trophy-stat">🤖 AI / LLM Track</span>
    </div>
</div>''', unsafe_allow_html=True)

# ─── RESEARCH ─────────────────────────────────────────────────────────────────
st.markdown('<div class="anchor-target" id="research"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Research</div>', unsafe_allow_html=True)

rc1, rc2 = st.columns([1, 1.6])
with rc1:
    st.image(research, use_container_width=True)
with rc2:
    st.markdown('''<div class="pub-card" style="margin-top:0">
    <span class="exp-badge">IEEE Publication · 2024</span>
    <h3 style="font-family:'Space Grotesk',sans-serif; font-size:1rem; font-weight:600; color:#F7FAFC; margin:0.5rem 0 0.5rem;">
        Chat Encryption and Decryption Using Divide and Merge Text Encryption Algorithm
    </h3>
    <p>
        V. Singhal, M. Nainwal and S. S. Dasawat<br>
        <em>2024 4th International Conference on Innovative Sustainable Computational Technologies (CISCT)</em>,
        Dehradun, India, 2024, pp. 1-4.<br><br>
        <a href="https://doi.org/10.1109/CISCT62494.2024.11134202" target="_blank">
            🔗 doi: 10.1109/CISCT62494.2024.11134202
        </a>
    </p>
</div>''', unsafe_allow_html=True)


# ─── CONTACT ──────────────────────────────────────────────────────────────────
st.markdown('<div class="anchor-target" id="contact"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Contact</div>', unsafe_allow_html=True)

con1, con2 = st.columns([1.2, 1])

with con1:
    contact_form = '''
    <div class="contact-wrapper">
        <p style="font-family:'Space Grotesk',sans-serif; font-size:1.1rem; font-weight:600; color:#F7FAFC; margin:0 0 0.25rem;">
            Send a Message
        </p>
        <p style="font-size:0.85rem; color:#718096; margin:0 0 1rem;">
            Have a project in mind or just want to say hi? I'd love to hear from you.
        </p>
        <form action="https://formsubmit.co/vighneshsinghal@gmail.com" method="POST"
              style="display:flex; flex-direction:column; gap:0.1rem;">
            <p class="contact-label">Your Name</p>
            <input class="contact-input" type="text" name="name" placeholder="e.g. John Doe" required>
            <p class="contact-label">Email Address</p>
            <input class="contact-input" type="email" name="email" placeholder="john@example.com" required>
            <p class="contact-label">Message</p>
            <textarea class="contact-input" name="message" placeholder="What's on your mind?" rows="4" style="resize:vertical;"></textarea>
            <button class="btn-send" type="submit">🚀 Send Message</button>
        </form>
    </div>
    '''
    st.markdown(contact_form, unsafe_allow_html=True)

with con2:
    st.markdown('''
    <div style="padding:1rem 0;">
        <p style="font-family:'Space Grotesk',sans-serif; font-size:1.1rem; font-weight:600; color:#F7FAFC; margin:0 0 0.5rem;">
            Get In Touch
        </p>
        <p style="font-size:0.875rem; color:#718096; margin:0 0 1.5rem; line-height:1.6;">
            I'm open to collaborations, internships, research opportunities, and interesting conversations about AI and Computer Vision.
        </p>
        <div class="contact-info-block">
            <div class="contact-info-item">
                <div class="contact-info-icon">📧</div>
                <div>
                    <div style="font-size:0.75rem; color:#718096; margin-bottom:0.1rem;">Email</div>
                    <a href="mailto:vighneshsinghal@gmail.com">vighneshsinghal@gmail.com</a>
                </div>
            </div>
            <div class="contact-info-item">
                <div class="contact-info-icon">📍</div>
                <div>
                    <div style="font-size:0.75rem; color:#718096; margin-bottom:0.1rem;">Location</div>
                    <span>Dehradun, Uttarakhand, India</span>
                </div>
            </div>
            <div class="contact-info-item">
                <div class="contact-info-icon">💼</div>
                <div>
                    <div style="font-size:0.75rem; color:#718096; margin-bottom:0.1rem;">LinkedIn</div>
                    <a href="https://www.linkedin.com/in/vighnesh-singhal-33b792244/" target="_blank">vighnesh-singhal-33b792244</a>
                </div>
            </div>
            <div class="contact-info-item">
                <div class="contact-info-icon">🐙</div>
                <div>
                    <div style="font-size:0.75rem; color:#718096; margin-bottom:0.1rem;">GitHub</div>
                    <a href="https://github.com/Vig7037" target="_blank">github.com/Vig7037</a>
                </div>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)


# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("<hr style='border-color:rgba(255,255,255,0.08); margin-top:3rem;'>", unsafe_allow_html=True)
st.markdown(
    '<div class="footer">Built with ❤️ by Vighnesh Singhal · Let\'s connect and build something amazing! 🚀</div>',
    unsafe_allow_html=True
)
