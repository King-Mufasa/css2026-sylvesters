import streamlit as st

st.set_page_config(page_title="Researcher Profile", page_icon="🧠", layout="wide")

# --- HEADER ---
st.title("Your Name Here")
st.subheader("Researcher / Student | Your Field (e.g., Data Science, Nursing, CS)")
st.write(
    "Short bio: 2–4 lines about what you study, what you are interested in, and what kind of work you do."
)

# Optional: contact links
st.markdown("""
**Email:** yourname@email.com  
**LinkedIn:** https://linkedin.com/in/yourprofile  
**GitHub:** https://github.com/yourusername  
**Google Scholar (optional):** https://scholar.google.com/citations?user=xxxx
""")

st.divider()

# --- ABOUT ---
col1, col2 = st.columns([2, 1])
with col1:
    st.header("About Me")
    st.write("""
- Your program/school and focus area
- Key interests (3–5 bullet points)
- Tools/skills (Python, R, Excel, SQL, etc.)
""")

with col2:
    st.header("Quick Facts")
    st.write("""
- Location: City, Country  
- Interests: X, Y, Z  
- Current Role: Student / Research Assistant / etc.
""")

st.divider()

# --- PROJECTS ---
st.header("Projects / Research")
projects = [
    {
        "title": "Project 1 Title",
        "desc": "1–2 sentence description of what you did, the goal, and result.",
        "tools": "Tools: Python, Pandas, Streamlit",
        "link": "https://github.com/yourusername/project1"
    },
    {
        "title": "Project 2 Title",
        "desc": "1–2 sentence description.",
        "tools": "Tools: SQL, Excel",
        "link": "https://github.com/yourusername/project2"
    },
]

for p in projects:
    st.subheader(p["title"])
    st.write(p["desc"])
    st.caption(p["tools"])
    st.write(f"Link: {p['link']}")
    st.divider()

# --- PUBLICATIONS / PRESENTATIONS ---
st.header("Publications / Presentations (optional)")
st.write("""
- Author, A. (Year). Title. Venue. Link  
- Poster/Presentation: Title, event, year  
""")

# --- FOOTER ---
st.caption("Made with Streamlit ☁️")
