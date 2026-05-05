
import csv
from retriever import Retriever
from classifier import classify
from risk import detect_risk
from utils import generate_response, escalation_response
import random

def detect_product_area(query):
    q = query.lower()

    hackerank_keywords = ["coding test", "challenge", "submission", "hackerrank"]
    claude_keywords = ["claude", "prompt", "ai response", "anthropic"]
    visa_keywords = ["card", "visa", "payment", "transaction", "bank"]

    def match_score(keywords):
        return sum(1 for k in keywords if k in q)

    scores = {
        "hackerrank": match_score(hackerank_keywords),
        "claude": match_score(claude_keywords),
        "visa": match_score(visa_keywords)
    }

    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "general"

def should_escalate(query):
    q = query.lower()
    keywords = ["fraud", "unauthorized", "stolen", "hack", "scam"]
    return any(k in q for k in keywords)

def process(input_file, output_file):
    retriever = Retriever("corpus")
    rows = []

    with open(input_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            query = row["query"]

            product_area = detect_product_area(query)

            if should_escalate(query):
                status = "escalated"
                response = escalation_response()
                justification = "Escalated: sensitive or high-risk query detected"
                request_type = "sensitive_issue"

            else:
                result, score = retriever.search(query)

                if score > 0.25:
                    status = "replied"
                    response = result.strip().capitalize()
                    justification = "Answer retrieved from knowledge base"
                    request_type = classify(query)
                else:
                    issue = classify(query)
                    risk = detect_risk(query)
                    response = generate_response(issue, risk)
                    status = "replied"
                    justification = f"Generated response using classification ({issue}) and risk ({risk})"
                    request_type = issue

            rows.append({
                "status": status,
                "product_area": product_area,
                "response": response,
                "justification": justification,
                "request_type": request_type
            })

    with open(output_file, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            "status",
            "product_area",
            "response",
            "justification",
            "request_type"
        ])
        writer.writeheader()
        writer.writerows(rows)
