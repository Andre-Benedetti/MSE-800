import os
from analyzer import CVAnalyzer, GeminiClient

def main():
    # Retrieve the API Key from environment variables
    api_key = os.getenv("GEMINI_API_KEY", "your_default_key")
    
    # Initialize the OOP components
    client = GeminiClient(api_key)
    analyzer = CVAnalyzer(client)

    # DEFINE FILE PATH HERE:   
    print("\n--- CV Analyzer System ---")
    cv_filename = input("Please enter the CV filename (e.g., my_cv.docx): ").strip()
    root_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(root_path, cv_filename)

    # Execute the analysis
    report = analyzer.process_cv(file_path)
    
    print("\n--- CV IMPROVEMENT REPORT ---")
    print(report)

if __name__ == "__main__":
    main()