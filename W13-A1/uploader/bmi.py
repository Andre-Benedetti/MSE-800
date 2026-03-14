from groq import Groq

# Initialize the Groq client with your key
client = Groq(
    api_key="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",
)

def calculate_bmi_info(weight, height):
    try:
        weight = float(weight)
        height = float(height)
        if height <= 0: return None
        
        bmi = round(weight / (height ** 2), 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"
            
        return {"value": bmi, "category": category}
    except (ValueError, TypeError):
        return None

def get_llm_diet_suggestion(bmi_info, age, gender):
    """
    Calls GroqCloud to get a diet suggestion based on BMI, Age, and Sex.
    """
    if not bmi_info:
        return "Invalid data provided."

    # Construct the prompt
    prompt = (
        f"Act as a professional nutritionist. Provide a personalized diet suggestion for a patient with the following profile:\n"
        f"- Age: {age} years old\n"
        f"- Sex: {gender}\n"
        f"- BMI: {bmi_info['value']} ({bmi_info['category']})\n\n"
        f"Please include specific macronutrient focus and examples of recommended foods. Keep it concise."
    )

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile", 
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error connecting to GroqCloud: {str(e)}"