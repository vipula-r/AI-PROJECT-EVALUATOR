import ollama
def evaluate_idea(idea):
    prompt = f"""
    Evaluate the following project idea:
    {idea}
    Give:
    1. Feasibility Score (0-100)
    2. Innovation Score (0-100) 
    3. Complexity Level 
    4. Technologies Required
    5. Advantages
    6. Risks
    7. Suggestions
    """
    response = ollama.chat(
        model="llama3.2:latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response["message"]["content"]
    