
import os
import random

class Retriever:
    def __init__(self, folder):
        self.docs = []
        for file in os.listdir(folder):
            with open(os.path.join(folder, file)) as f:
                self.docs.append(f.read())

    def search(self, query):
        matches = []
        for doc in self.docs:
            if any(word in doc.lower() for word in query.lower().split()):
                matches.append(doc.strip())

        if matches:
            return random.choice(matches), 0.5

        return "", 0.0
