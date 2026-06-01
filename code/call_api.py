import os
from dotenv import load_dotenv
from openai import OpenAI

def call_model(prompt: str) -> str:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL")
    model_name = os.getenv("MODEL_NAME")

    if not api_key:
        raise ValueError("没有找到 API_KEY，请检查 .env 文件。")
    if not base_url:
        raise ValueError("没有找到 BASE_URL，请检查 .env 文件")
    if not model_name:
        raise ValueError("没有找到 MODEL_NAME，请检查 .env 文件")

    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        max_tokens=300,
    )

    
    answer = response.choices[0].message.content
    return answer

if __name__ == "__main__":
    prompt = "Explain what a LLM is."
    answer = call_model(prompt)

    print("User:",prompt)
    print()
    print("Assistant:",answer)

