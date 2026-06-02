#  AI-Powered Cold Email Generator (LangChain + Streamlit + Groq + ChromaDB)

This project is an **AI-powered Cold Email Generator** built using **Python, Streamlit, LangChain, Groq LLM, and ChromaDB**.  
It automatically generates personalized cold emails for job applications based on job descriptions provided by the user.

---

##  Project Objective

The purpose of this project is to automate the process of writing professional cold emails for job applications using AI.  
It extracts important job details from the description and generates a personalized email accordingly.

---

##  Features

-  Input job description via **Copy-Paste or URL**
-  Uses **LangChain + Groq LLM (Llama-3.3-70B)** for AI text generation
-  Extracts key job details:
  - Role
  - Experience
  - Skills
  - Description
-  Generates **professional cold emails (150–200 words)**
-  Fully personalized email content
-  Simple and interactive **Streamlit UI**
-  Fast AI response using Groq API
-  Text cleaning before processing

---

##  Tech Stack

- Python   
- Streamlit   
- LangChain  
- Groq LLM   
- ChromaDB   
- Regex (Text Cleaning)   
- Dotenv   

---

##  Project Structure
app.py → Streamlit UI
chain.py → LangChain logic (job extraction + email generation)
clean_data.py → Text cleaning functions
requirements.txt → Required dependencies

##  Installation (VS Code Setup)

###  Open Project in VS Code
- Open **VS Code**
- Click **File → Open Folder**
- Select your project folder

---

### Create Virtual Environment
```bash id="c9p2kt"
python -m venv venv
```

---

###  Activate Virtual Environment

**Windows:**
```bash id="v1n8dq"
venv\Scripts\activate
```

---

### Install Required Libraries
```bash id="m3x9la"
pip install -r requirements.txt
```

---

### Add API Key

Create a file named `.env` in project folder:

```env id="h2q8sd"
GROQ_API_KEY=your_api_key_here
```

---

### Run the Project
```bash id="t5w1km"
streamlit run app.py
```

---

##  How It Works

1. User enters job description (text or URL)
2. Data is cleaned and processed
3. LangChain extracts:
   - Job role
   - Skills
   - Experience
4. Groq LLM generates a cold email
5. Streamlit displays the final email

---

## Workflow

```
Job Description
      ↓
Text Cleaning
      ↓
LangChain Extraction
      ↓
Groq LLM Processing
      ↓
Email Generation
      ↓
Streamlit Output
```

---

## Important Notes

- Use **Copy-Paste job description** for best results
- Some URLs may not work due to website restrictions
- LinkedIn URLs are not supported
- Internet connection is required
- Valid Groq API key must be added

---

## 🔥 Future Improvements

-  ChromaDB-based portfolio matching (RAG system)
-  Resume upload feature
- Direct email sending feature
- Save email history
- UI improvements

---

## Author

AI Cold Email Generator Project  
Built using LangChain + Streamlit + Groq LLM

---

## Output

Generate professional cold emails in seconds using AI!

