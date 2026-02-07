import os
from google.genai import Client
from docx import Document

class GeminiClient:
    """Handles communication with the Google Gemini API using the modern SDK."""
    def __init__(self, api_key):
        self.api_key = api_key
        if self.api_key:
            # In the new SDK, we initialize the Client directly with the API key
            self.client = Client(api_key=self.api_key)
        else:
            self.client = None
        
    def get_suggestions(self, cv_text):
        """Sends CV text to Gemini and returns professional NZ-focused advice."""
        if not self.client:
            return "Error: Gemini API Key not configured correctly."

        # Structured prompt for the AI
        prompt = f"""
        You are a career expert in the New Zealand tech industry. 
        Analyze the following CV and provide 3 actionable recommendations to improve its quality 
        for a Software Engineering role, specifically highlighting the transition from 
        administrative/operations roles to tech. Mention that the candidate is currently 
        studying a Master in Software Engineering at Yoobee.
        
        CV Content:
        {cv_text}
        """

        try:
            response = self.client.models.generate_content(
                model='gemini-2.0-flash',
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"API Error: {str(e)}"

class CVAnalyzer:
    """Handles CV file parsing and analysis orchestration."""
    def __init__(self, client):
        self.client = client

    def process_cv(self, file_path):
        """Extracts text from .txt or .docx and sends it to the Gemini client."""
        if not os.path.exists(file_path):
            return f"Error: File not found at {file_path}"
        
        try:
            # Handle Word Documents
            if file_path.endswith('.docx'):
                doc = Document(file_path)
                content = "\n".join([para.text for para in doc.paragraphs])
            # Handle Plain Text files
            else:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            
            # Send extracted content to the AI client
            return self.client.get_suggestions(content)
        except Exception as e:
            return f"Processing error: {str(e)}"