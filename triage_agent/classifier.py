
def classify(query):
    q = query.lower()
    if "login" in q or "password" in q:
        return "account_issue"
    elif "payment" in q or "refund" in q:
        return "billing_issue"
    elif "api" in q or "error" in q:
        return "technical_issue"
    return "product_issue"
