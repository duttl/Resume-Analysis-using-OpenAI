# ATS Resume Matcher (Streamlit + OpenAI)

An industry-grade Applicant Tracking System (ATS) that uses OpenAI's `gpt-3.5-turbo` model to analyze resumes against job descriptions and generate match scores, relevant skill mapping, and improvement suggestions. Built with modular architecture, full test coverage, and production-ready practices.

---

## 🚀 Demo

<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit" width="25"/> Launch locally with:

```bash
streamlit run ats/app.py
```

---

## 🧠 Features

- 📄 PDF Resume Parsing using PyMuPDF
- ✍️ Smart JD/Resume Matching with OpenAI
- 🎯 Match Scoring + Skill Feedback
- 🧪 Unit-Tested and Modular Code
- 📦 Packaged for CLI Launch (`ats-app`)
- 🔒 Secure API Key Handling via `.env`
- 📊 Future-ready for deployment or scaling

---

## 🏗️ Project Structure

```
ats_app/
│
├── ats/                  # App code
│   ├── app.py            # Streamlit interface
│   ├── extractor.py      # Resume text parser
│   ├── llm_chatgpt.py    # ChatGPT integration
│   └── utils.py          # Logging setup
│
├── tests/                # Unit tests
│   └── test_*.py
│
├── .env                  # (API key, ignored)
├── requirements.txt
├── setup.py              # Installable as CLI
└── README.md
```

---

## ⚙️ Setup Instructions

```bash
# Step 1: Clone and setup environment
git clone https://github.com/your-username/ats_app.git
cd ats_app
conda create -n ats_env python=3.10 -y
conda activate ats_env

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Add your OpenAI key
echo OPENAI_API_KEY=sk-... >> .env

# Step 4: Run the app
streamlit run ats/app.py
```

---

## ✅ Tests

```bash
pytest tests/
```

100% passing coverage with mocks for OpenAI API.

---

## 📦 Packaging & CLI

Install app as CLI:

```bash
pip install -e .
ats-app  # Launches the Streamlit UI
```

---

## 🏁 Production-Readiness

- 🔐 `.env` for API secrets
- 🔎 Logging for debugging and tracing
- 📁 Modular design with separation of concerns
- 🧪 Unit tests with `pytest` and mocks
- 🧰 `setup.py` for packaging and CLI entry points
- 📤 Easily deployable to Streamlit Cloud or Docker

---

## 📚 Learning & Takeaways

- How to build modular Streamlit apps
- How to integrate OpenAI GPT models with context-rich prompts
- How to design testable, maintainable, production-level Python code
- Using `pytest`, `unittest.mock`, and `.env` practices for secure and testable design

---

## 🧠 Credits

Developed by [Dutt Lodagala](https://github.com/duttl)

---


