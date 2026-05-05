# 🤖 AI Support Triage System

This project is a hybrid AI-based support ticket triage system that classifies, prioritizes and responds to user queries using retrieval-based logic and rule-based decision making.

It was developed as part of a HackerRank Hackathon project.

---

## 🔍 Features

* Classifies support tickets into categories like billing, account, technical, etc
* Detects high priority issues (fraud, hacked account, urgent cases)
* Retrieves responses from a knowledge base (corpus) using keyword-based matching
* Avoids hallucination by not generating random answers
* Simple pipeline and easy to understand

---

## 🧠 Approach

This system follows a deterministic pipeline:

**User Query → Classification → Risk Detection → Retrieval → Response**

Technologies / logic used:

* Keyword-based retrieval
* Rule-based classification
* Keyword based risk detection

The main idea was to keep the system reliable and explainable rather than fully generative.

---

## 📁 Project Structure

```bash id="2x0hyk"
ai-support-triage-system/
│
├── main.py
├── agent.py
├── retriever.py
├── classifier.py
├── risk.py
├── utils.py
├── corpus/
│   └── faq.txt
├── support_tickets.csv
```

---

## ⚙️ How to Run

Install dependencies (if needed):

```bash id="y27z4s"
pip install scikit-learn
```

Run the main file:

```bash id="9q8u1r"
python main.py
```

Output will be generated in:

```bash id="t8m2kq"
output.csv
```

---

## ⚠️ Limitations

* Corpus is very small (only few entries right now)
* Retrieval is basic and not semantic
* No real ML model is trained
* Responses are simple and can be improved

---

## 🚀 Future Improvements

* Add larger dataset for better retrieval
* Use embeddings for semantic search
* Improve classification using ML models
* Build a simple UI for better interaction

---

## ⚠️ Mistakes Occurred During Development

* Initially used random selection in retriever which made responses inconsistent
* Product area detection was not accurate (e.g., payment queries going to wrong category)
* Forgot to include `ticket_id` in output which made tracking difficult
* Corpus was too small at beginning (only one line)
* Used template-based response generation which was not fully grounded
* File naming issues (like `agent(3).py`) caused import errors while running

These issues were later identified and improved step by step.

---

## 💡 Learning Outcome

This project helped me understand how support systems work internally and why deterministic and explainable systems are important.

---

## 👤 Author

Aditya Singh
