
def detect_risk(query):
    q = query.lower()
    if "urgent" in q or "asap" in q:
        return "high"
    elif "error" in q or "failed" in q:
        return "medium"
    return "low"
