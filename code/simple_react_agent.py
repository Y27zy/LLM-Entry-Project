import os
import re
import json
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

def get_project_root() -> Path:
    return Path(__file__).resolve().parent.parent

def get_client() -> tuple[OpenAI, str]:
    project_root = get_project_root()
    env_path = project_root / ".env"

    load_dotenv(env_path)

    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL")
    model_name = os.getenv("MODEL_NAME")

    if not api_key:
        raise ValueError("没有找到 API_KEY，请检查 .env 文件。")
    if not base_url:
        raise ValueError("没有找到 BASE_URL，请检查 .env 文件。")
    if not model_name:
        raise ValueError("没有找到 MODEL_NAME，请检查 .env 文件。")

    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )

    return client, model_name

def call_model(messages: list[dict]) -> str:
    client, model_name = get_client()
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0,
        max_tokens=512,
    )
    content = response.choices[0].message.content
    if content is None or content.strip() == "":
        raise ValueError("模型返回空内容。")
    
    return content.strip()

def calculator(expression: str) -> str:
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Calculator error : {e}"
    
def build_system_prompt() -> str:
    return """You are a ReAct agent. You can solve problems by reasoning and you have access to the following tool:
    
    calculator(expression):
    - use this tool to calculator a mathematical expression.
    - Example: calculator("79*3+12")

    You must following this format:

    Thought: your reasoning about what to do next
    Action: calculator("expression")

    After you receive an Observation, continue with :

    Thought: your reasoning about what to do next
    Final Answer: the final answer to the user

    Rules:
    - If calculation is needed, use the calculator tool.
    - Do not invent the Observation yourself.
    - Use exactly one Action at a time.
    - When you know the answer, output Final Answer.
"""

def parse_action(model_output: str):
    pattern = r'Action:\s*calculator\("(.+?)"\)'
    match = re.search(pattern, model_output, flags=re.DOTALL)

    if not match:
        return None
    
    expression = match.group(1)

    return {
        "tool_name": "calculator",
        "tool_input": expression,
    }

def run_tool(tool_name: str, tool_input: str) -> str:
    if tool_name == "calculator":
        return calculator(tool_input)
    
    return f"Unknow tool: {tool_name}"

def run_react_agent(question: str, max_steps: int = 5) -> dict:
    messages = [
        {
            "role": "system",
            "content": build_system_prompt(),
        },
        {
            "role": "user",
            "content": f"Question: {question}",
        },
    ]

    trace = {
        "question": question,
        "steps": [],
        "final_answer": "",
    }

    for step in range(1, max_steps + 1):
        model_output = call_model(messages)

        step_record = {
            "step": step,
            "model_output": model_output,
        }

        print("=" * 80)
        print(f"Step {step}")
        print("-" * 80)
        print(model_output)
        print()

        if "Final Answer:" in model_output:
            final_answer = model_output.split("Final Answer:", 1)[-1].strip()
            trace["final_answer"] = final_answer
            step_record["type"] = "final_answer"
            trace["steps"].append(step_record)
            break

        action = parse_action(model_output)

        if action is None:
            step_record["type"] = "parse_error"
            step_record["error"] = "No valid Action found."
            trace["steps"].append(step_record)
            break

        tool_name = action["tool_name"]
        tool_input = action["tool_input"]
        observation = run_tool(tool_name, tool_input)

        step_record["type"] = "tool_call"
        step_record["tool_name"] = tool_name
        step_record["tool_input"] = tool_input
        step_record["observation"] = observation

        trace["steps"].append(step_record)

        messages.append({
            "role": "assistant",
            "content": model_output,
        })

        messages.append({
            "role": "user",
            "content": f"Observation: {observation}",
        })

    save_trace(trace)
    return trace

def save_trace(trace: dict):
    project_root = get_project_root()
    output_dir = project_root / "outputs"
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / "react_agent_traces.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(trace, f, ensure_ascii=False, indent=2)

    print(f"Trace saved to: {output_path}")

if __name__ == "__main__":
    question = "A book costs 69 yuan. I buy 4 books and pay 15 yuan for shipping. How much do I pay in total?"
    trace = run_react_agent(question)

    print("=" * 80)
    print("Final Answer:")
    print(trace["final_answer"])