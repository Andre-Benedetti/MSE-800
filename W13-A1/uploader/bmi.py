def calculate_bmi_info(weight, height):
    try:
        weight = float(weight)
        height = float(height)
        if height <= 0: return None
        
        bmi = round(weight / (height ** 2), 2)
        
        # Determine category
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