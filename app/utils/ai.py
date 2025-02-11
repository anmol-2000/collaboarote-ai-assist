import openai

def analyze_code(code: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Analyze this code: {code}"}]
    )
    return response['choices'][0]['message']['content']
