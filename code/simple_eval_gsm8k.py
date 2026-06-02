import os
import re
import json
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from datasets import load_dataset

def get_project_root() -> Path:
    return Path(__file__).resolve().parent.parent

def get_client() -> tuple[OpenAI, str]:
    project_root = get_project_root()
    env_path = project_root/".env"
    load_dotenv(env_path)
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL")
    model_name = os.getenv("MODEL_NAME")

    if not api_key:
        raise ValueError("没有找到 API_KEY，请检查项目根目录下的 .env 文件。")

    if not base_url:
        raise ValueError("没有找到 BASE_URL，请检查项目根目录下的 .env 文件。")

    if not model_name:
        raise ValueError("没有找到 MODEL_NAME，请检查项目根目录下的 .env 文件。")
    
    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )

    return client, model_name

def call_model(prompt : str):
    client, model_name = get_client()
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Follow the user's instruction carefully.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0,
        max_tokens=256,
    )
    return response.choices[0].message.content

def load_gsm8k_examples(num_examples: int=5):
    """
    读取 GSM8K 测试集中的前 num_examples 道题
    """
    dataset = load_dataset("gsm8k", "main", split="test")
    examples = []
    for i in range(num_examples):
        item = dataset[i]
        question = item["question"]
        answer = item["answer"]

        examples.append({
            "question": question,
            "answer": answer,
        })
    return examples

def build_direct_prompt(question: str):
    prompt = f"""Please solve the following math problem. Give only the final answer as a number.
    
    Question:
    {question}
    """
    return prompt

def extract_gold_answer(answer: str):
    if "####" not in answer:
        return extract_number(answer)
    final_answer = answer.split("####")[-1].strip()
    return normalize_number(final_answer)
    
def extract_number(answer):
    numbers = re.findall(r"-?\d+(?:,\d{3})*(?:\.\d+)?|-?\d+(?:\.\d+)?", answer)
    if not numbers:
        return ""
    return normalize_number(numbers[-1])

def normalize_number(final_answer: str):
    final_answer = final_answer.strip()
    final_answer = final_answer.replace(",", "")
    match = re.search(r"-?\d+(?:\.\d+)?", final_answer)
    if not match:
        return ""
    number = match.group(0)
    if "." in number:
        try:
            value = float(number)
            if value.is_integer():
                number = str(int(value))
        except ValueError:
            pass
    
    return number

def evaluate_gsm8k(num_examples: int = 10):
    examples = load_gsm8k_examples(num_examples = num_examples)
    results = []
    correct_count = 0
    for idx, item in enumerate(examples, start=1):
        question = item["question"]
        gold_answer_full = item["answer"]
        prompt = build_direct_prompt(question)
        try:
            model_output = call_model(prompt)
        except Exception as e:
            model_output = ""
            error_message = str(e)
            print("API 调用失败：", error_message)
        else:
            error_message = ""
        gold_answer = extract_gold_answer(gold_answer_full)
        model_answer = extract_number(model_output)
        is_correct = gold_answer == model_answer
        if is_correct:
            correct_count += 1
        print("Gold Answer:", gold_answer)
        print("Model Output:", model_output)
        print("Extracted Model Answer:", model_answer)
        print("Correct:", is_correct)
        results.append({
            "index": idx,
            "question": question,
            "gold_answer_full": gold_answer_full,
            "gold_answer": gold_answer,
            "prompt": prompt,
            "model_output": model_output,
            "model_answer": model_answer,
            "correct": is_correct,
            "error_message": error_message,
        })

    accuracy  =correct_count/num_examples
    print("=" * 80)
    print("Evaluation Finished")
    print(f"Correct: {correct_count}/{num_examples}")
    print(f"Accuracy: {accuracy:.2%}")

    save_results(results, accuracy, num_examples)

    return accuracy, results

def save_results(results, accuracy: float, num_examples: int):
    """
    保存评测结果到 outputs/gsm8k_eval_results.json。
    """
    project_root = get_project_root()
    output_dir = project_root / "outputs"
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / "gsm8k_eval_results.json"

    data = {
        "num_examples": num_examples,
        "accuracy": accuracy,
        "results": results,
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Results saved to: {output_path}")

if __name__ == "__main__":
    evaluate_gsm8k(num_examples=10)