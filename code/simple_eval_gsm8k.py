from datasets import load_dataset

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

def print_examples(examples):
    """
    打印题目和标准答案，方便观察数据格式。
    """
    for idx, item in enumerate(examples,start=1):
        print("=" * 80)
        print(item["question"])
        print()
        print("Answer:")
        print(item["answer"])
        print()

if __name__ == "__main__":
    examples = load_gsm8k_examples(num_examples=5)
    print_examples(examples)