import json
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="EduTrack", page_icon="🎓", layout="wide", initial_sidebar_state="expanded")

NAVY  = "#0F1E36"
TEAL  = "#00C9A7"
AMBER = "#FFB347"
SLATE = "#1E3050"
PAPER = "#F0F4FA"
MUTED = "#7A8FA6"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500&display=swap');
html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; background-color: {PAPER}; color: {NAVY}; }}
[data-testid="stSidebar"] {{ background: linear-gradient(160deg, {NAVY} 0%, {SLATE} 100%); }}
[data-testid="stSidebar"] * {{ color: #E8EFF7 !important; }}
h1, h2, h3 {{ font-family: 'Space Grotesk', sans-serif; font-weight: 700; }}
.metric-card {{ background: white; border-radius: 14px; padding: 1.4rem 1.6rem; border-left: 4px solid {TEAL}; box-shadow: 0 2px 12px rgba(15,30,54,0.07); margin-bottom: 1rem; }}
.metric-card.amber {{ border-left-color: {AMBER}; }}
.metric-card.purple {{ border-left-color: #A78BFA; }}
.metric-label {{ font-size: 0.78rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: {MUTED}; }}
.metric-value {{ font-family: 'Space Grotesk', sans-serif; font-size: 2.2rem; font-weight: 700; color: {NAVY}; line-height: 1.1; }}
.person-card {{ background: white; border-radius: 12px; padding: 1rem 1.2rem; margin-bottom: 0.7rem; border: 1px solid #DDE5F0; box-shadow: 0 1px 6px rgba(15,30,54,0.05); display: flex; align-items: center; gap: 0.9rem; }}
.avatar {{ width: 48px; height: 48px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 1.15rem; flex-shrink: 0; }}
.avatar-s {{ background: {TEAL}33; color: #007A62; }}
.avatar-t {{ background: {AMBER}44; color: #A06000; }}
.badge {{ display: inline-block; background: {TEAL}22; color: #007A62; border-radius: 50px; padding: 0.18rem 0.75rem; font-size: 0.75rem; font-weight: 600; }}
.badge-amber {{ background: {AMBER}33; color: #A06000; }}
.grade-pill {{ display: inline-block; padding: 0.2rem 0.75rem; border-radius: 6px; font-size: 0.82rem; font-weight: 600; background: {NAVY}11; color: {NAVY}; margin: 0.2rem 0.15rem; }}
.profile-card {{ background: white; border-radius: 16px; padding: 2rem; margin-top: 1rem; box-shadow: 0 2px 16px rgba(15,30,54,0.08); border: 1px solid #DDE5F0; }}
.field-label {{ font-size: 0.73rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.07em; color: {MUTED}; margin-bottom: 0.15rem; }}
.field-value {{ font-weight: 600; font-size: 0.95rem; color: {NAVY}; margin-bottom: 0.8rem; }}
.section-head {{ font-family: 'Space Grotesk', sans-serif; font-size: 1.05rem; font-weight: 700; color: {NAVY}; padding-bottom: 0.4rem; border-bottom: 2px solid {PAPER}; margin: 1rem 0 0.8rem; }}
.stButton > button {{ background: {TEAL}; color: white; border: none; border-radius: 10px; font-family: 'Space Grotesk', sans-serif; font-weight: 600; font-size: 0.9rem; padding: 0.55rem 1.6rem; box-shadow: 0 2px 8px {TEAL}44; }}
.stButton > button:hover {{ background: #00A88C; }}
</style>
""", unsafe_allow_html=True)

DATABASE = "School_data.json"

def load_data():
    p = Path(DATABASE)
    if p.exists():
        c = p.read_text().strip()
        if c:
            return json.loads(c)
    return {"Students": [], "Teachers": []}

def save_data(d):
    with open(DATABASE, "w") as f:
        json.dump(d, f, indent=4)

def validate_email(e):
    return "@" in e and "." in e

def get_initials(name):
    parts = name.split()
    return (parts[0][0] + (parts[1][0] if len(parts) > 1 else "")).upper()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    data = load_data()
    st.markdown(f"""
    <div style="text-align:center;padding:1.4rem 1rem 1rem;border-bottom:1px solid rgba(255,255,255,0.1);margin-bottom:1.5rem;">
        <div style="font-size:2.4rem;">🎓</div>
        <div style="font-family:'Space Grotesk',sans-serif;font-size:1.5rem;font-weight:700;color:white;">EduTrack</div>
        <div style="font-size:0.72rem;color:{TEAL};font-weight:600;letter-spacing:0.1em;text-transform:uppercase;">School Management</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio("nav", [
        "📊  Dashboard", "🎒  Register Student", "👩‍🏫  Register Teacher",
        "📝  Add Grades", "🔍  Student Details", "🔍  Teacher Details",
    ], label_visibility="collapsed")

    st.markdown(f"""
    <div style="margin-top:1.5rem;padding:1rem;background:rgba(255,255,255,0.07);border-radius:12px;">
        <div style="font-size:0.72rem;color:#7AB8D4;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:0.6rem;">Quick Stats</div>
        <div style="display:flex;justify-content:space-between;margin-bottom:0.3rem;">
            <span style="font-size:0.85rem;">Students</span>
            <span style="font-family:'Space Grotesk',sans-serif;font-weight:700;color:{TEAL};">{len(data["Students"])}</span>
        </div>
        <div style="display:flex;justify-content:space-between;">
            <span style="font-size:0.85rem;">Teachers</span>
            <span style="font-family:'Space Grotesk',sans-serif;font-weight:700;color:{AMBER};">{len(data["Teachers"])}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Dashboard ─────────────────────────────────────────────────────────────────
if page == "📊  Dashboard":
    data = load_data()
    st.markdown(f'<h1 style="font-size:2rem;margin-bottom:0.1rem;">Welcome back 👋</h1><p style="color:{MUTED};margin-bottom:1.8rem;">Overview of your school.</p>', unsafe_allow_html=True)

    total_grades = sum(len(s.get("grades", [])) for s in data["Students"])
    c1, c2, c3 = st.columns(3)
    c1.markdown(f'<div class="metric-card"><div class="metric-label">Students</div><div class="metric-value">{len(data["Students"])}</div></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="metric-card amber"><div class="metric-label">Teachers</div><div class="metric-value">{len(data["Teachers"])}</div></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="metric-card purple"><div class="metric-label">Grade Entries</div><div class="metric-value">{total_grades}</div></div>', unsafe_allow_html=True)

    col_s, col_t = st.columns(2)
    with col_s:
        st.markdown('<div class="section-head">Recent Students</div>', unsafe_allow_html=True)
        if data["Students"]:
            for s in reversed(data["Students"][-5:]):
                ini = get_initials(s["name"])
                gc = len(s.get("grades", []))
                st.markdown(f'<div class="person-card"><div class="avatar avatar-s">{ini}</div><div style="flex:1;"><div style="font-weight:600;font-size:0.95rem;">{s["name"]}</div><div style="font-size:0.8rem;color:{MUTED};">Roll #{s["roll_number"]} &nbsp;·&nbsp; Age {s["age"]}</div></div><span class="badge">{gc} grade{"s" if gc!=1 else ""}</span></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p style="color:{MUTED};font-size:0.9rem;">No students yet.</p>', unsafe_allow_html=True)

    with col_t:
        st.markdown('<div class="section-head">Recent Teachers</div>', unsafe_allow_html=True)
        if data["Teachers"]:
            for t in reversed(data["Teachers"][-5:]):
                ini = get_initials(t["name"])
                st.markdown(f'<div class="person-card"><div class="avatar avatar-t">{ini}</div><div style="flex:1;"><div style="font-weight:600;font-size:0.95rem;">{t["name"]}</div><div style="font-size:0.8rem;color:{MUTED};">ID {t["emp_id"]} &nbsp;·&nbsp; {t["subject"]}</div></div><span class="badge badge-amber">{t["subject"]}</span></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p style="color:{MUTED};font-size:0.9rem;">No teachers yet.</p>', unsafe_allow_html=True)

# ── Register Student ──────────────────────────────────────────────────────────
elif page == "🎒  Register Student":
    st.markdown(f'<h1 style="font-size:1.8rem;margin-bottom:0.1rem;">Register Student</h1><p style="color:{MUTED};margin-bottom:1.4rem;">Add a new student to the system.</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        name  = st.text_input("Full Name",     placeholder="e.g. Arjun Sharma")
        email = st.text_input("Email Address", placeholder="student@school.edu")
    with c2:
        age  = st.number_input("Age", min_value=5, max_value=25, value=16)
        roll = st.text_input("Roll Number",   placeholder="e.g. S2024001")
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Register Student"):
        data = load_data()
        if not name.strip() or not email.strip() or not roll.strip():
            st.error("Please fill in all fields.")
        elif not validate_email(email):
            st.error("Please enter a valid email address.")
        elif any(s["roll_number"] == roll.strip() for s in data["Students"]):
            st.error(f"Roll number **{roll}** already exists.")
        else:
            data["Students"].append({"name": name.strip(), "age": int(age), "email": email.strip(), "roll_number": roll.strip(), "grades": []})
            save_data(data)
            st.success(f"Student **{name}** registered successfully!")

# ── Register Teacher ──────────────────────────────────────────────────────────
elif page == "👩‍🏫  Register Teacher":
    st.markdown(f'<h1 style="font-size:1.8rem;margin-bottom:0.1rem;">Register Teacher</h1><p style="color:{MUTED};margin-bottom:1.4rem;">Add a new teacher to the system.</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        name    = st.text_input("Full Name",     placeholder="e.g. Priya Mehta")
        email   = st.text_input("Email Address", placeholder="teacher@school.edu")
        subject = st.text_input("Subject",       placeholder="e.g. Mathematics")
    with c2:
        age    = st.number_input("Age", min_value=22, max_value=75, value=35)
        emp_id = st.text_input("Employee ID",   placeholder="e.g. T2024001")
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Register Teacher"):
        data = load_data()
        if not name.strip() or not email.strip() or not subject.strip() or not emp_id.strip():
            st.error("Please fill in all fields.")
        elif not validate_email(email):
            st.error("Please enter a valid email address.")
        elif any(t["emp_id"] == emp_id.strip() for t in data["Teachers"]):
            st.error(f"Employee ID **{emp_id}** already exists.")
        else:
            data["Teachers"].append({"name": name.strip(), "age": int(age), "email": email.strip(), "subject": subject.strip(), "emp_id": emp_id.strip()})
            save_data(data)
            st.success(f"Teacher **{name}** registered successfully!")

# ── Add Grades ────────────────────────────────────────────────────────────────
elif page == "📝  Add Grades":
    st.markdown(f'<h1 style="font-size:1.8rem;margin-bottom:0.1rem;">Add Grades</h1><p style="color:{MUTED};margin-bottom:1.4rem;">Record a grade entry for a student.</p>', unsafe_allow_html=True)
    data = load_data()
    if not data["Students"]:
        st.info("No students registered yet. Register a student first.")
    else:
        opts = {f"{s['name']}  (Roll: {s['roll_number']})": s["roll_number"] for s in data["Students"]}
        selected = st.selectbox("Select Student", list(opts.keys()))
        roll = opts[selected]
        c1, c2 = st.columns(2)
        with c1:
            subject = st.text_input("Subject", placeholder="e.g. Physics")
        with c2:
            grade = st.text_input("Grade", placeholder="e.g. A+ or 92")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Save Grade"):
            if not subject.strip() or not grade.strip():
                st.error("Please enter both subject and grade.")
            else:
                data = load_data()
                for s in data["Students"]:
                    if s["roll_number"] == roll:
                        s["grades"].append({"subject": subject.strip(), "grade": grade.strip()})
                        save_data(data)
                        st.success(f"Grade **{grade}** in **{subject}** saved for {s['name']}.")
                        break
        data = load_data()
        for s in data["Students"]:
            if s["roll_number"] == roll and s.get("grades"):
                st.markdown(f'<div class="section-head">Current Grades ({len(s["grades"])})</div>', unsafe_allow_html=True)
                pills = "".join(f'<span class="grade-pill">{g["subject"]}: <b>{g["grade"]}</b></span>' for g in s["grades"])
                st.markdown(f'<div style="margin-top:0.4rem;">{pills}</div>', unsafe_allow_html=True)
                break

# ── Student Details ───────────────────────────────────────────────────────────
elif page == "🔍  Student Details":
    st.markdown(f'<h1 style="font-size:1.8rem;margin-bottom:0.1rem;">Student Details</h1><p style="color:{MUTED};margin-bottom:1.4rem;">Look up a student profile.</p>', unsafe_allow_html=True)
    data = load_data()
    if not data["Students"]:
        st.info("No students registered yet.")
    else:
        opts = {f"{s['name']}  —  Roll #{s['roll_number']}": s["roll_number"] for s in data["Students"]}
        selected = st.selectbox("Choose a student", list(opts.keys()))
        roll = opts[selected]
        student = next((s for s in data["Students"] if s["roll_number"] == roll), None)
        if student:
            ini = get_initials(student["name"])
            grades = student.get("grades", [])
            st.markdown(f'<div class="profile-card"><div style="display:flex;align-items:center;gap:1rem;margin-bottom:1.5rem;"><div class="avatar avatar-s" style="width:60px;height:60px;font-size:1.4rem;">{ini}</div><div><div style="font-family:\'Space Grotesk\',sans-serif;font-size:1.4rem;font-weight:700;">{student["name"]}</div><span class="badge">Student</span></div></div></div>', unsafe_allow_html=True)
            fc1, fc2 = st.columns(2)
            fc1.markdown(f'<div class="field-label">Roll Number</div><div class="field-value">{student["roll_number"]}</div>', unsafe_allow_html=True)
            fc2.markdown(f'<div class="field-label">Age</div><div class="field-value">{student["age"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="field-label">Email</div><div class="field-value">{student["email"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="section-head">Grades ({len(grades)})</div>', unsafe_allow_html=True)
            if grades:
                pills = "".join(f'<span class="grade-pill">{g["subject"]}: <b>{g["grade"]}</b></span>' for g in grades)
                st.markdown(f'<div>{pills}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<p style="color:{MUTED};font-size:0.9rem;">No grades recorded yet.</p>', unsafe_allow_html=True)

# ── Teacher Details ───────────────────────────────────────────────────────────
elif page == "🔍  Teacher Details":
    st.markdown(f'<h1 style="font-size:1.8rem;margin-bottom:0.1rem;">Teacher Details</h1><p style="color:{MUTED};margin-bottom:1.4rem;">Look up a teacher profile.</p>', unsafe_allow_html=True)
    data = load_data()
    if not data["Teachers"]:
        st.info("No teachers registered yet.")
    else:
        opts = {f"{t['name']}  —  ID {t['emp_id']}": t["emp_id"] for t in data["Teachers"]}
        selected = st.selectbox("Choose a teacher", list(opts.keys()))
        emp_id = opts[selected]
        teacher = next((t for t in data["Teachers"] if t["emp_id"] == emp_id), None)
        if teacher:
            ini = get_initials(teacher["name"])
            st.markdown(f'<div class="profile-card"><div style="display:flex;align-items:center;gap:1rem;margin-bottom:1.5rem;"><div class="avatar avatar-t" style="width:60px;height:60px;font-size:1.4rem;">{ini}</div><div><div style="font-family:\'Space Grotesk\',sans-serif;font-size:1.4rem;font-weight:700;">{teacher["name"]}</div><span class="badge badge-amber">Teacher &nbsp;&middot;&nbsp; {teacher["subject"]}</span></div></div></div>', unsafe_allow_html=True)
            fc1, fc2 = st.columns(2)
            fc1.markdown(f'<div class="field-label">Employee ID</div><div class="field-value">{teacher["emp_id"]}</div>', unsafe_allow_html=True)
            fc2.markdown(f'<div class="field-label">Age</div><div class="field-value">{teacher["age"]}</div>', unsafe_allow_html=True)
            fc3, fc4 = st.columns(2)
            fc3.markdown(f'<div class="field-label">Subject</div><div class="field-value">{teacher["subject"]}</div>', unsafe_allow_html=True)
            fc4.markdown(f'<div class="field-label">Email</div><div class="field-value">{teacher["email"]}</div>', unsafe_allow_html=True)
