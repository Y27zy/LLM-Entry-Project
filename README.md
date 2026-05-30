# 大模型推理与 Agent 方向进组面试 11 天准备计划

## 1. 项目定位

这个项目不是为了做一个漂亮的展示作品，而是为了在 11 天内通过代码练习和笔记整理，补齐进组面试需要的三类能力：

1. 了解大模型推理与后训练方法：SFT、DPO、PPO、GRPO、CoT 等；
2. 能调用闭源 API 或加载开源模型，并在评测数据集上做基础评估；
3. 理解 Agent / ReAct / Tool Calling，并能写出一个简单工具调用 Agent。

代码的目的不是展示，而是帮助自己真的理解：如果老师问到“怎么评测模型”“ReAct 怎么实现”“SFT 和 GRPO 有什么区别”，我能结合自己写过的代码说清楚。

---

## 2. 项目结构

```text
llm-interview-prep/
├── README.md
├── requirements.txt
├── .env.example
│
├── code/
│   ├── call_api.py
│   ├── simple_eval_gsm8k.py
│   ├── compare_prompts_gsm8k.py
│   ├── run_local_model.py
│   └── simple_react_agent.py
│
├── notes/
│   ├── 01_llm_and_prompt.md
│   ├── 02_evaluation_and_gsm8k.md
│   ├── 03_post_training.md
│   ├── 04_agent_and_react.md
│   ├── 05_open_source_models.md
│   └── interview_questions.md
│
├── outputs/
│   ├── gsm8k_eval_results.json
│   ├── prompt_comparison_results.json
│   ├── wrong_cases.json
│   └── react_agent_traces.json
│
└── summaries/
    ├── daily_log.md
    ├── final_review.md
    └── email_draft.md
```

---

## 3. 各文件作用说明

### 3.1 代码文件

| 文件 | 作用 |
|---|---|
| `code/call_api.py` | 练习大模型 API 调用，理解 `messages`、`temperature`、`max_tokens`、response 解析。 |
| `code/simple_eval_gsm8k.py` | 完成最小 GSM8K 评测流程：读数据、构造 prompt、调用模型、提取答案、计算 accuracy。 |
| `code/compare_prompts_gsm8k.py` | 比较 Direct Prompt 和 CoT Prompt 的效果，观察 prompt 对结果的影响。 |
| `code/run_local_model.py` | 尝试加载 HuggingFace 开源小模型，理解 tokenizer、generate、本地模型和 API 模型的区别。 |
| `code/simple_react_agent.py` | 实现简单 ReAct Agent，理解 Thought / Action / Observation / Tool Calling。 |

### 3.2 笔记文件

| 文件 | 作用 |
|---|---|
| `notes/01_llm_and_prompt.md` | 记录 LLM、Prompt、CoT、Self-Consistency 等基础内容。 |
| `notes/02_evaluation_and_gsm8k.md` | 记录 benchmark、GSM8K、accuracy、答案提取、错误分析。 |
| `notes/03_post_training.md` | 记录 SFT、RLHF、PPO、DPO、GRPO、DeepSeek-R1。 |
| `notes/04_agent_and_react.md` | 记录 Agent、ReAct、Tool Calling、Memory、Planning、Multi-Agent。 |
| `notes/05_open_source_models.md` | 记录 HuggingFace、本地模型加载、tokenizer、generate。 |
| `notes/interview_questions.md` | 整理面试可能被问到的问题和自己的回答。 |

### 3.3 输出文件

| 文件 | 作用 |
|---|---|
| `outputs/gsm8k_eval_results.json` | 保存基础 GSM8K 评测结果。 |
| `outputs/prompt_comparison_results.json` | 保存 Direct Prompt 和 CoT Prompt 的对比结果。 |
| `outputs/wrong_cases.json` | 保存错误样例，用于分析模型错误类型。 |
| `outputs/react_agent_traces.json` | 保存 ReAct Agent 运行轨迹。 |

### 3.4 总结文件

| 文件 | 作用 |
|---|---|
| `summaries/daily_log.md` | 每天记录完成内容、问题、明天要补的东西。 |
| `summaries/final_review.md` | 面试前最终复盘。 |
| `summaries/email_draft.md` | 给老师发邮件前的草稿。 |

---

## 4. 十一天学习计划

每一天都按这个顺序来：

1. 先学当天必须理解的概念；
2. 再写对应代码；
3. 最后整理笔记和面试回答。

不要求把代码写得很工程化，但要求能运行、能看懂、能解释。

---

### Day 1：5.31 周日  
**主题：LLM、Prompt 与 API 调用入门**

#### 今日目标

跑通 `call_api.py`，知道如何用 Python 调用一个大模型 API。

#### 学习顺序

1. 先弄懂几个基本概念：
   - LLM 是什么；
   - Prompt 是什么；
   - API 调用是什么；
   - `messages` 是什么；
   - `temperature` 和 `max_tokens` 控制什么。

2. 配置 API 环境：
   - 准备 API key、base_url、model name；
   - 建立 `.env.example`；
   - 安装必要依赖。

3. 编写 `code/call_api.py`：
   - 写一个 `call_model(prompt)` 函数；
   - 固定输入几个问题测试；
   - 打印模型返回内容。

4. 测试三类问题：
   - 简单计算：`What is 2 + 3?`
   - 数学表达式：`Please solve: 79 * 3 + 12.`
   - 概念解释：`Explain Chain-of-Thought in one paragraph.`

5. 在 `notes/01_llm_and_prompt.md` 记录：
   - API 调用流程；
   - `messages` 格式；
   - `temperature` 的作用；
   - 今天遇到的问题。

#### 今日产物

- `code/call_api.py`
- `.env.example`
- `notes/01_llm_and_prompt.md`

#### 最低完成线

`call_api.py` 能成功调用模型，并返回一句回答。

#### 可选加深

- 支持命令行输入问题；
- 测试不同 `temperature` 的输出差异；
- 把 `call_model(prompt)` 写成后续脚本可以复用的函数。

---

### Day 2：6.1 周一  
**主题：Prompt 基础与 GSM8K 数据集读取**

#### 今日目标

理解 Zero-shot、Few-shot、CoT，并能读取 GSM8K 前几条数据。

#### 学习顺序

1. 学 Prompt 基础：
   - Zero-shot；
   - Few-shot；
   - Chain-of-Thought；
   - Direct Prompt；
   - 固定输出格式，例如 `Final Answer: <number>`。

2. 学 Benchmark 和 GSM8K：
   - benchmark 是标准评测数据集；
   - GSM8K 是数学应用题推理数据集；
   - 看清楚 `question` 和 `answer` 的格式。

3. 在 `code/simple_eval_gsm8k.py` 中先写数据读取部分：
   - 读取 GSM8K 前 5 道题；
   - 打印 `question`；
   - 打印 `answer`。

4. 观察标准答案：
   - 标准答案里是否有推理过程；
   - 最终答案在哪里；
   - 能不能用简单规则提取最终数字。

5. 在 `notes/02_evaluation_and_gsm8k.md` 记录：
   - GSM8K 是什么；
   - 一条数据长什么样；
   - 为什么答案提取很重要。

#### 今日产物

- `code/simple_eval_gsm8k.py` 初版
- `notes/02_evaluation_and_gsm8k.md`

#### 最低完成线

能读取并打印 GSM8K 前 5 道题。

#### 可选加深

- 查看 train/test split；
- 写出 Direct Prompt 和 CoT Prompt 模板；
- 尝试从标准答案中提取最终数字。

---

### Day 3：6.2 周二  
**主题：完成最小 GSM8K 模型评测闭环**

#### 今日目标

把 API 调用和 GSM8K 数据连接起来，跑通前 10 题评测。

#### 学习顺序

1. 先写清楚评测流程：

```text
读取数据集
构造 prompt
调用模型
提取模型答案
提取标准答案
比较答案
计算 accuracy
保存结果
```

2. 在 `simple_eval_gsm8k.py` 中实现答案提取函数：

```python
def extract_number(text):
    """
    从文本中提取最后一个数字。
    第一版先能用，不追求完美。
    """
```

3. 使用 Direct Prompt：

```text
Please solve the following math problem. Give only the final answer as a number.

Question:
{question}
```

4. 跑 GSM8K 前 10 道题：
   - 逐题调用模型；
   - 提取模型答案；
   - 提取标准答案；
   - 判断对错；
   - 输出 accuracy。

5. 保存结果到 `outputs/gsm8k_eval_results.json`，每条记录包括：
   - question；
   - gold_answer；
   - model_output；
   - extracted_gold；
   - extracted_model；
   - correct。

6. 在 `notes/02_evaluation_and_gsm8k.md` 记录：
   - accuracy 怎么算；
   - 答案提取遇到的问题；
   - 模型输出格式是否稳定。

#### 今日产物

- `code/simple_eval_gsm8k.py`
- `outputs/gsm8k_eval_results.json`

#### 最低完成线

能跑 GSM8K 前 10 道题，并输出 accuracy。

#### 可选加深

- 保存错误样例到 `wrong_cases.json`；
- 改进 `extract_number`；
- 支持修改评测题目数量；
- 加 API 异常处理。

---

### Day 4：6.3 周三  
**主题：Direct Prompt vs CoT Prompt 对比实验**

#### 今日目标

通过代码观察 prompt 对评测结果的影响。

#### 学习顺序

1. 学 CoT 和 Self-Consistency：
   - CoT 为什么可能提升推理；
   - CoT 为什么可能出错；
   - Self-Consistency 是什么。

2. 准备两个 prompt。

Direct Prompt：

```text
Please solve the following math problem. Give only the final answer as a number.

Question:
{question}
```

CoT Prompt：

```text
Please solve the following math problem step by step.
At the end, write your answer in the format:
Final Answer: <number>

Question:
{question}
```

3. 编写 `code/compare_prompts_gsm8k.py`：
   - 读取 GSM8K 前 20 道题；
   - 分别用 Direct Prompt 和 CoT Prompt 调用模型；
   - 分别提取答案；
   - 分别计算 accuracy；
   - 保存对比结果。

4. 保存错误样例到 `outputs/wrong_cases.json`，字段包括：
   - question；
   - gold_answer；
   - direct_output；
   - cot_output；
   - direct_extracted；
   - cot_extracted；
   - error_type。

5. 错误类型先粗略分为：
   - 答案提取错误；
   - 模型计算错误；
   - 模型推理错误；
   - 输出格式错误；
   - 不确定。

6. 在 `notes/02_evaluation_and_gsm8k.md` 写下：
   - Direct 和 CoT 的区别；
   - 两种 prompt 的 accuracy；
   - 典型错误样例；
   - 自己的观察。

#### 今日产物

- `code/compare_prompts_gsm8k.py`
- `outputs/prompt_comparison_results.json`
- `outputs/wrong_cases.json`

#### 最低完成线

能跑 GSM8K 前 20 道题，并得到 Direct Prompt 和 CoT Prompt 的 accuracy。

#### 可选加深

- 题目数量扩展到 50；
- 改进 `Final Answer` 提取；
- 分析 Direct 对但 CoT 错的样例；
- 分析 CoT 对但 Direct 错的样例；
- 比较 `temperature=0` 和 `temperature=0.7`。

---

### Day 5：6.4 周四  
**主题：后训练算法：SFT、PPO、DPO、GRPO**

#### 今日目标

建立后训练知识框架，能解释 SFT、PPO、DPO、GRPO 的基本区别。

#### 学习顺序

1. 先写训练阶段总图：

```text
Pretraining
↓
SFT
↓
RLHF / PPO / DPO / GRPO
↓
Reasoning / Agent
```

2. 学 SFT，重点回答：
   - SFT 是什么；
   - SFT 的数据长什么样；
   - SFT 和预训练有什么区别；
   - SFT 和 RL 后训练有什么区别；
   - SFT 的优点和局限是什么。

3. 学 RLHF、Reward Model、PPO，重点回答：
   - RLHF 是什么；
   - Reward Model 是什么；
   - PPO 在 RLHF 里起什么作用；
   - 为什么 PPO 比 SFT 复杂。

4. 学 DPO，重点回答：
   - DPO 是什么；
   - DPO 和 PPO 有什么区别；
   - 为什么 DPO 更简单；
   - DPO 需要什么样的数据。

5. 学 GRPO，重点回答：
   - GRPO 是什么；
   - GRPO 和 PPO 有什么区别；
   - 为什么 GRPO 和 DeepSeek-R1 相关；
   - 为什么 GRPO 适合推理任务。

6. 在 `notes/03_post_training.md` 写一张对比表：

| 方法 | 数据形式 | 核心思想 | 优点 | 局限 |
|---|---|---|---|---|
| SFT | 问题-标准答案 | 模仿人工答案 | 稳定简单 | 可能泛化有限 |
| PPO | 奖励模型打分 | 强化学习优化 | 能按奖励优化 | 训练复杂 |
| DPO | 偏好对 | 直接优化好坏回答偏好 | 比 PPO 简洁 | 依赖偏好数据 |
| GRPO | 同题多回答及奖励 | 组内相对比较 | 适合推理 RL | 仍依赖奖励设计 |

7. 在 `notes/interview_questions.md` 写 5 个后训练问题和回答。

#### 今日产物

- `notes/03_post_training.md`
- `notes/interview_questions.md` 更新

#### 最低完成线

能用自己的话解释 SFT、PPO、DPO、GRPO 的基本区别。

#### 可选加深

- 阅读 DeepSeek-R1 摘要或导读；
- 写一段“SFT vs RL：为什么 RL 可能更能提升推理泛化？”；
- 思考后训练和 Prompt Engineering 的关系。

---

### Day 6：6.5 周五  
**主题：ReAct Agent 第一版实现**

#### 今日目标

理解 Agent 和普通 LLM 的区别，并写出最小 ReAct 工具调用循环。

#### 学习顺序

1. 学 Agent 基础：
   - Agent 是什么；
   - Agent 和普通 LLM 有什么区别；
   - Tool Calling 是什么；
   - ReAct 是什么；
   - Thought / Action / Observation 分别是什么。

2. 写下 ReAct 标准格式：

```text
Question: 用户问题
Thought: 我需要做什么
Action: 工具名(参数)
Observation: 工具返回结果
Thought: 根据结果继续思考
Final Answer: 最终回答
```

3. 在 `code/simple_react_agent.py` 中写 calculator 工具：

```python
def calculator(expression):
    """
    执行简单数学表达式计算。
    这里只用于本地学习。
    """
```

4. 设计 Agent Prompt，要求模型：
   - 知道有哪些工具；
   - 按指定格式输出 Action；
   - 得到 Observation 后继续推理；
   - 最后输出 Final Answer。

5. 实现最小循环：
   - 输入用户问题；
   - 调用模型生成 Thought / Action；
   - 解析 Action；
   - 调用 calculator；
   - 把 Observation 放回上下文；
   - 再次调用模型；
   - 直到出现 Final Answer。

6. 保存运行轨迹到 `outputs/react_agent_traces.json`。

#### 今日产物

- `code/simple_react_agent.py`
- `outputs/react_agent_traces.json`
- `notes/04_agent_and_react.md`

#### 最低完成线

ReAct Agent 能调用 calculator 完成一个简单数学问题。

#### 可选加深

- 支持多轮工具调用；
- 加最大循环次数，防止死循环；
- 对 Action 解析失败做错误提示；
- 记录 Agent 失败样例。

---

### Day 7：6.6 周六  
**主题：Agent 工具扩展、Memory、Planning 与失败分析**

#### 今日目标

扩展 Agent 工具，并总结 Agent 常见失败原因。

#### 学习顺序

1. 复习 ReAct：
   - ReAct 和普通 CoT 有什么区别；
   - 为什么 Observation 要重新喂给模型；
   - 为什么 Agent 需要工具。

2. 学 Agent 扩展概念：
   - Memory：记录过去信息；
   - Planning：把复杂任务拆成步骤；
   - Multi-Agent：多个 Agent 分工或互相检查。

3. 在 `simple_react_agent.py` 增加工具：

```python
def mock_search(query):
    return "This is a mock search result for: " + query
```

4. 让 Agent 支持两个工具：
   - `calculator(expression)`；
   - `mock_search(query)`。

5. 测试三类问题：
   - 纯计算问题；
   - 需要查询的问题；
   - 查询和计算结合的问题。

6. 在 `notes/04_agent_and_react.md` 总结失败原因：
   - 工具选择错误；
   - 工具参数格式错误；
   - Action 解析失败；
   - 工具结果理解错误；
   - 模型编造工具结果；
   - 陷入重复循环；
   - 过早给出 Final Answer。

#### 今日产物

- `code/simple_react_agent.py` 更新
- `outputs/react_agent_traces.json` 更新
- `notes/04_agent_and_react.md` 更新

#### 最低完成线

Agent 支持 calculator 和 mock_search 两个工具，并能解释常见失败原因。

#### 可选加深

- 使用统一 JSON 格式表示工具调用；
- 增加工具调用错误处理；
- 写一段“Agent 和普通 LLM 的区别”面试回答。

---

### Day 8：6.7 周日  
**主题：HuggingFace 开源小模型加载**

#### 今日目标

理解开源模型加载流程，知道本地模型和 API 模型的区别。

#### 学习顺序

1. 学 HuggingFace 基础：
   - HuggingFace 是什么；
   - transformers 是什么；
   - tokenizer 是什么；
   - AutoTokenizer 是什么；
   - AutoModelForCausalLM 是什么；
   - generate 是什么。

2. 选一个小模型，不要一上来跑 7B：
   - Qwen2.5-0.5B-Instruct；
   - Qwen2.5-1.5B-Instruct；
   - TinyLlama。

3. 编写 `code/run_local_model.py`：
   - 加载 tokenizer；
   - 加载 model；
   - 构造 prompt；
   - tokenize；
   - `model.generate`；
   - decode；
   - 打印回答。

4. 测试三个问题：
   - `What is 2 + 3?`
   - `Explain what an LLM is.`
   - `Solve: 79 * 3 + 12.`

5. 在 `notes/05_open_source_models.md` 对比：
   - API 模型：强、方便、省本地资源，但依赖网络和服务商；
   - 本地模型：可控、可研究、可复现，但需要硬件资源和环境配置。

#### 今日产物

- `code/run_local_model.py`
- `notes/05_open_source_models.md`

#### 最低完成线

写出 `run_local_model.py` 的基本流程，并能解释 tokenizer、generate、本地模型和 API 模型的区别。

#### 可选加深

- 成功跑通一个小模型；
- 比较本地小模型和 API 模型对同一问题的回答；
- 记录模型加载失败原因；
- 理解 `device_map`、`torch_dtype`、`max_new_tokens`。

---

### Day 9：6.8 周一  
**主题：知识关系整理与面试问题第一轮**

#### 今日目标

把前 8 天内容整理成面试问题体系。

#### 学习顺序

1. 在 `summaries/final_review.md` 整理知识地图：

```text
LLM 基础
├── Token / Tokenizer
├── Transformer
├── Prompt
└── CoT

模型评测
├── Benchmark
├── GSM8K
├── Prompt 构造
├── 答案提取
└── Accuracy

后训练
├── SFT
├── RLHF
├── PPO
├── DPO
└── GRPO

Agent
├── ReAct
├── Tool Calling
├── Memory
├── Planning
└── Multi-Agent
```

2. 在 `notes/interview_questions.md` 按模块整理问题：
   - 大模型基础；
   - Prompt 与推理；
   - 模型评测；
   - 后训练；
   - Agent；
   - 代码实现。

3. 每个问题先写 3 到 6 句话回答，要求是自己的话，不要抄定义。

4. 检查核心代码是否能运行：
   - `call_api.py`；
   - `simple_eval_gsm8k.py`；
   - `compare_prompts_gsm8k.py`；
   - `simple_react_agent.py`。

5. 在 `summaries/daily_log.md` 写下当前最不熟的 3 个问题。

#### 今日产物

- `notes/interview_questions.md` 第一版
- `summaries/final_review.md` 第一版
- `summaries/daily_log.md` 更新

#### 最低完成线

整理出至少 25 个面试问题，并为大部分问题写出自己的回答。

#### 可选加深

- 扩展到 40 个问题；
- 给问题标注熟悉程度；
- 按“必会 / 了解 / 不熟”分类；
- 录音练习口头回答。

---

### Day 10：6.9 周二  
**主题：综合复盘与薄弱点补强**

#### 今日目标

补最弱的地方，把代码练习和面试回答连起来。

#### 学习顺序

1. 从 Day 9 标出的薄弱点里选 2 到 3 个重点补：
   - SFT / DPO / PPO / GRPO；
   - GSM8K 评测流程；
   - 答案提取；
   - CoT 和 ReAct 区别；
   - Agent 工具调用流程；
   - HuggingFace 模型加载。

2. 在 `notes/interview_questions.md` 增加“代码支撑回答”。

例如：

```text
Q: 怎么评测一个模型在 GSM8K 上的表现？

A: 我写过一个简单脚本，流程是：
1. 用 datasets 读取 GSM8K；
2. 为每道题构造 prompt；
3. 调用 API 得到模型输出；
4. 用 extract_number 提取最终答案；
5. 和标准答案比较；
6. 计算 accuracy；
7. 保存 wrong cases 分析错误。
```

3. 给核心代码加注释：
   - `code/call_api.py`；
   - `code/compare_prompts_gsm8k.py`；
   - `code/simple_react_agent.py`。

4. 挑 10 个问题口头回答：
   - SFT 是什么；
   - GRPO 是什么；
   - SFT 和 RL 有什么区别；
   - CoT 是什么；
   - 怎么评测 GSM8K；
   - 为什么答案提取重要；
   - Agent 和普通 LLM 区别；
   - ReAct 是什么；
   - Tool Calling 是什么；
   - 代码练习中最有收获的地方是什么。

5. 在 `summaries/email_draft.md` 写邮件草稿。

#### 今日产物

- `notes/interview_questions.md` 更新
- 核心代码注释更新
- `summaries/email_draft.md`

#### 最低完成线

能比较顺畅地回答 10 个核心问题，邮件草稿写好。

#### 可选加深

- 为每个核心问题准备“短回答”和“展开回答”；
- 把不会的问题列成补习清单；
- 让 ChatGPT 模拟老师追问。

---

### Day 11：6.10 周三  
**主题：发邮件前最终整理与模拟面试**

#### 今日目标

完成最终复盘，确保自己能回答、能解释代码、能说明准备过程。

#### 学习顺序

1. 检查核心文件是否完成：
   - `README.md`；
   - `code/call_api.py`；
   - `code/simple_eval_gsm8k.py`；
   - `code/compare_prompts_gsm8k.py`；
   - `code/simple_react_agent.py`；
   - `notes/03_post_training.md`；
   - `notes/04_agent_and_react.md`；
   - `notes/interview_questions.md`；
   - `summaries/final_review.md`；
   - `summaries/email_draft.md`。

2. 跑核心代码：

```bash
python code/call_api.py
python code/compare_prompts_gsm8k.py
python code/simple_react_agent.py
```

如果因为 API、网络、环境问题跑不通，就在笔记里写清楚原因，不要临时大改。

3. 完成 `summaries/final_review.md`：
   - 这 11 天学了什么；
   - 写了哪些代码练习；
   - 现在能回答哪些问题；
   - 还不熟什么；
   - 如果老师问到不熟内容，怎么诚实回答。

4. 模拟回答 10 个问题：
   - 你最近做了哪些准备；
   - SFT 和 GRPO 有什么区别；
   - 你怎么理解大模型推理能力；
   - 如果让你评测一个模型，你怎么做；
   - GSM8K 是什么；
   - CoT 为什么可能提升表现；
   - Agent 和普通 LLM 有什么区别；
   - ReAct 是什么；
   - 怎么实现简单工具调用 Agent；
   - 你现在还有哪些地方不熟。

5. 修改 `summaries/email_draft.md` 最终版。

#### 今日产物

- `summaries/final_review.md` 完成
- `summaries/email_draft.md` 完成
- `notes/interview_questions.md` 完成第一版

#### 最低完成线

能用自己的话回答核心面试问题，并能解释自己写过的 API、评测和 Agent 代码练习。

#### 可选加深

- 录音模拟面试；
- 让 ChatGPT 追问；
- 把最容易卡住的问题单独补充到笔记；
- 准备“我目前还不熟，但下一步想学什么”的回答。

---

## 5. 6.11 发邮件当天安排

6.11 不作为主要学习日，只做发邮件和轻量复习。

当天任务：

1. 检查邮件内容；
2. 发邮件给老师；
3. 复习 `notes/interview_questions.md`；
4. 看 `summaries/final_review.md`；
5. 跑一遍 `simple_react_agent.py`；
6. 不再临时大改项目结构。

邮件表达可以参考：

```text
老师您好，我最近按照进组前的自测标准做了一些初步准备：学习了 SFT、DPO、PPO、GRPO 等后训练方法的基本思想；通过代码练习调用大模型 API，并在 GSM8K 子集上做了简单评测；此外也实现了一个 ReAct 风格的简单工具调用 Agent。想请问老师 6.12～6.14 期间是否方便交流。
```

---

## 6. 6.12～6.14 面试窗口期安排

这几天不再以学新知识为主，主要做复习和稳定表达。

每天做三件事：

1. 复习 `notes/interview_questions.md`；
2. 复习 `summaries/final_review.md`；
3. 跑一遍或看一遍核心代码。

面试前最后半小时只看：

```text
notes/interview_questions.md
summaries/final_review.md
notes/03_post_training.md
notes/04_agent_and_react.md
```

不要临时打开大量新论文或新教程。

---

## 7. 最终检查清单

### 7.1 理论方面

至少能解释：

```text
LLM
Prompt
CoT
SFT
DPO
PPO
GRPO
Benchmark
GSM8K
Agent
ReAct
Tool Calling
```

### 7.2 代码方面

至少能解释：

```text
call_api.py 的 API 调用流程
simple_eval_gsm8k.py / compare_prompts_gsm8k.py 的评测流程
simple_react_agent.py 的 ReAct 工具调用流程
```

### 7.3 面试表达方面

至少能说清楚：

```text
我为什么想进组
我最近做了哪些准备
我现在掌握到什么程度
我还不熟什么
我后续想继续学什么
```
