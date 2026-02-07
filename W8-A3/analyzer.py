import os
from docx import Document  # Required for .docx files

class GeminiClient:
    """Handles communication with the AI API."""
    def __init__(self, api_key):
        self.api_key = api_key
        
    def get_suggestions(self, cv_text):
        """Mock method for AI analysis."""
        return "Suggestion: Highlight your Master in Software Engineering at Yoobee more prominently."

class CVAnalyzer:
    """Handles CV file parsing and analysis orchestration."""
    def __init__(self, client):
        self.client = client

    def process_cv(self, file_path):
        """Extracts text from .txt or .docx and sends to client."""
        if not os.path.exists(file_path):
            return f"Error: File not found at {file_path}"
        
        try:
            # Logic to handle Word Documents (.docx)
            if file_path.endswith('.docx'):
                doc = Document(file_path)
                content = "\n".join([para.text for para in doc.paragraphs])
            # Logic to handle Text files (.txt)
            else:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            
            return self.client.get_suggestions(content)
        except Exception as e:
            return f"Processing error: {str(e)}"