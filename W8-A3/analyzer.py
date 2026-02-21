"""
CV Analyzer Module for Yoobee MSE-800.
Uses Groq (Llama 3.3) for lightning-fast NZ-focused career advice.
"""

import os
from groq import Groq
from docx import Document

# pylint: disable=too-few-public-methods
class GroqCVClient:
    """Handles communication with Groq API."""
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key) if api_key else None

    def get_suggestions(self, cv_text):
        """Sends CV text to Groq and returns professional NZ-focused advice."""
        if not self.client:
            return "Error: Groq API Key not configured."

        prompt = f"""
        You are a career expert in the New Zealand tech industry.
        Analyze the following CV and provide 3 actionable recommendations to improve its quality
        for a Software Engineering role. Focus on:
        1. The transition from administrative roles to tech.
        2. Mentioning the Master in Software Engineering at Yoobee.
        3. NZ-specific CV standards.

        CV Content:
        {cv_text}
        """

        try:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a professional NZ Career Coach."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=1024
            )
            return completion.choices[0].message.content
        except Exception as e: # pylint: disable=broad-exception-caught
            return f"Groq API Error: {str(e)}"

class CVAnalyzer:
    """Handles CV file parsing and analysis orchestration."""
    def __init__(self, client):
        self.client = client

    def process_cv(self, file_path):
        """Extracts text from .txt or .docx and sends it to the Groq client."""
        if not os.path.exists(file_path):
            return f"Error: File not found at {file_path}"
        try:
            if file_path.endswith('.docx'):
                doc = Document(file_path)
                content = "\n".join([para.text for para in doc.paragraphs])
            else:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            return self.client.get_suggestions(content)
        except Exception as e: # pylint: disable=broad-exception-caught
            return f"Processing error: {str(e)}"

if __name__ == "__main__":
    
    API_KEY = "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"

    groq_client = GroqCVClient(API_KEY)
    analyzer = CVAnalyzer(groq_client)

    print("\n--- Yoobee CV Analyzer (Powered by Groq) ---")
    path_to_cv = input("Path to .docx: ").strip().replace('"', '').replace("'", "")

    if path_to_cv:
        print("\nAnalyzing with Llama 3.3... hang tight!")
        result = analyzer.process_cv(path_to_cv)
        print("\n" + "="*50 + "\n" + result + "\n" + "="*50)
