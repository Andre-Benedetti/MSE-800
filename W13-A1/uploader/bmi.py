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
        f"INSTRUCTION: Act as a professional nutritionist and provide a personalized diet suggestion "
        f"including macronutrient focus and food examples for the profile below.\n"
        f"USER PROFILE: Age {age}, Sex {gender}, BMI {bmi_info['value']} ({bmi_info['category']}).\n\n"
        f"TASK:\n"
        f"1. Rephrase the INSTRUCTION above to show you understand your professional role and requirements.\n"
        f"2. Respond to that rephrased instruction with the actual diet plan.\n\n"
        f"FORMAT:\n"
        f"REPHRASED INSTRUCTION: [Your rephrasing]\n"
        f"NUTRITIONAL PLAN: [Your suggestion]\n"
        f"DONE"
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
           temperature=0.4,      # Focused and professional
            top_p=0.24,           # Narrowed probability mass
            stop=["DONE"],        # Stop sequence
            max_tokens=1024         #Limit response length to ensure conciseness
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error connecting to GroqCloud: {str(e)}"