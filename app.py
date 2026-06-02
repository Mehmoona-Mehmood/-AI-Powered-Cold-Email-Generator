import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from clean_data import clean_text
from chains import Chain

# 1. Page Configuration
st.set_page_config(
    page_title="AI Cold Mail Generator",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Injecting Custom Modern CSS Elements
st.markdown("""
    <style>
    /* Main Background & Font Tweaks */
    .stApp {
        background-color: #f8fafc;
    }
    h1, h2, h3 {
        color: #1e293b !important;
        font-family: 'Inter', sans-serif;
    }
    
    /* Input Container Styling */
    .stTextArea textarea, .stTextInput input {
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
        color: #334155 !important;
    }
    
    /* Main Generate Button Style */
    .stButton>button {
        background-color: #2563eb !important;
        color: white !important;
        border-radius: 6px !important;
        padding: 0.6rem 2rem !important;
        font-weight: 600 !important;
        border: none !important;
        box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2);
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #1d4ed8 !important;
        transform: translateY(-1px);
    }
    
    /* Output Containers */
    .email-subject-box {
        background-color: #ffffff;
        padding: 1.25rem;
        border-radius: 8px;
        border-left: 5px solid #2563eb;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
        color: #1e293b;
    }
    .email-body-box {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.7;
        white-space: pre-wrap;
        color: #334155;
    }
    .cta-box {
        background-color: #eff6ff;
        padding: 1rem;
        border-radius: 8px;
        border: 1px dashed #3b82f6;
        text-align: center;
        font-weight: 500;
        font-size: 15px;
        color: #1d4ed8;
        margin-top: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

def display_email(email_content):
    """Display the email in an elegant, executive format"""
    try:
        parts = email_content.split("\n\n")
        if "Subject:" in parts[0]:
            subject = parts[0].replace("Subject:", "").strip()
            body = "\n\n".join(parts[1:])
        else:
            subject = "Personalized Application Outreach"
            body = email_content
    except Exception:
        subject = "Personalized Application Outreach"
        body = email_content

    st.markdown("### 📄 Generated Pitch")
    
    # Display Subject Box
    st.markdown(f"""
        <div class="email-subject-box">
            <span style="color: #64748b; font-size: 0.85rem; text-transform: uppercase; font-weight: bold; display: block; margin-bottom: 2px;">Subject Line</span>
            <strong>{subject}</strong>
        </div>
    """, unsafe_allow_html=True)

    # Display Email Body Box
    st.markdown(f"""
        <div class="email-body-box">{body}</div>
    """, unsafe_allow_html=True)

    # Action Banner
    st.markdown("""
        <div class="cta-box">
            🚀 Review the generated details, adapt details if necessary, and dispatch it to the hiring team!
        </div>
    """, unsafe_allow_html=True)

def create_streamlit_app(llm, clean_text):
    # Sidebar Info Panel
    with st.sidebar:
        st.markdown("### 🛠️ System Status")
        st.success("Connected to Groq LLM Engine")
        st.markdown("---")
        st.markdown("""
        **Tips for accurate generations:**
        * Copy-pasting full text provides stable context processing.
        * Standard web URLs extract live job metadata instantly.
        * Make sure your underlying configurations are validated.
        """)
    
    # Header Layout
    st.title("📧 AI Cold Mail Generator")
    st.markdown("<p style='color: #64748b; font-size: 1.1rem; margin-top: -15px;'>Transform standard job requirements into structured, high-conversion outreach emails automatically.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Main Application Layout Tabs
    tab1, tab2 = st.tabs(["📋 Direct Copy-Paste", "🌐 Live Job URL"])
    
    job_description = ""
    url_input = ""
    input_method = "Copy-Paste"

    with tab1:
        job_description = st.text_area(
            "Paste the complete target job description details:", 
            height=280, 
            placeholder="Paste technical requirements, company overview, role definitions here...",
            key="paste_area"
        )

    with tab2:
        url_input = st.text_input(
            "Target Portal Job Link (Excluding LinkedIn):", 
            placeholder="https://careers.company.com/pages/job-id-102",
            key="url_field"
        )
        if url_input:
            input_method = "Provide URL (Excluding LinkedIn)"

    # Operational Logic Check Execution
    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
    submit_button = st.button("Generate Cold Email")

    if submit_button:
        # Resolving inputs explicitly based on which tab contains active data
        active_tab_paste = job_description.strip() if tab1 else ""
        
        with st.spinner("Analyzing operational structures and generating draft..."):
            if url_input.strip() and not active_tab_paste:
                input_method = "Provide URL (Excluding LinkedIn)"
            elif active_tab_paste:
                input_method = "Copy-Paste"

            if input_method == "Copy-Paste":
                if not job_description.strip():
                    st.error("Execution halted: Please provide a valid job description text structure.")
                    return
                data = clean_text(job_description)
            else:
                if not url_input.strip():
                    st.error("Execution halted: Please configure a valid target job URL path.")
                    return
                loader = WebBaseLoader([url_input])
                data = clean_text(loader.load().pop().page_content)
            
            try:
                jobs = llm.extract_jobs(data)
                job = jobs[0]  

                email = llm.write_mail(
                    job["role"], 
                    job["experience"], 
                    ", ".join(job["skills"]), 
                    job["description"]
                )
                
                st.toast("Email Draft Compiled!", icon="✨")
                display_email(email)
            except Exception as e:
                st.error(f"Processing Error occurred during LLM compilation pipeline: {str(e)}")

if __name__ == "__main__":
    chain = Chain()
    create_streamlit_app(chain, clean_text)