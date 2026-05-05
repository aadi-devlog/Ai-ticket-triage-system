
import random

def generate_response(issue, risk):
    templates = [
        f"We are handling your {issue}. Priority: {risk}.",
        f"Your {issue} has been identified. Priority level: {risk}.",
        f"Our team is reviewing your {issue} with {risk} priority."
    ]
    return random.choice(templates)

def escalation_response():
    return "This issue is sensitive and has been escalated to human support."
