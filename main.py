import os
import ollama

# Define the models
models = [
    "codellama:34b",
    "llama3.2:3b",
    "mistral:latest",
    "llama3:8b",
    "qwen:latest",
    "codeqwen:latest"
]

def initialize_log(question):
    if not os.path.exists("log"):
        os.makedirs("log")
    log_file_name = f"log/{question}.txt"
    with open(log_file_name, 'w') as log_file:
        log_file.write("")
    return log_file_name

def read_log(log_file_name):
    with open(log_file_name, 'r') as log_file:
        return log_file.read()

def write_log(log_file_name, content):
    with open(log_file_name, 'a') as log_file:
        log_file.write("\n" + content + "\n\n")

def count_log_entries(log_file_name):
    with open(log_file_name, 'r') as log_file:
        return len(log_file.readlines())

def get_response(model, prompt):
    res = ollama.chat(model=model, stream=False, messages=[{"role": "user", "content": prompt}], options={"temperature": 0})
    return res['message']['content']

def multi_agent_discussion(question):
    log_file_name = initialize_log(question)
    write_log(log_file_name, f"Question: {question}")
    
    for i in range(10):
        for model in models:
            previous_conversation = read_log(log_file_name)
            response = get_response(model, previous_conversation)
            write_log(log_file_name, f"{model} :\n  {response}")


if __name__ == "__main__":
    question = [
        "1.什么是神经符号融合软件", 
        "2.您如何看待大语言模型的“推理”能力？它的“推理”能力与检索增强、外挂工具以及Agent技术等相结合将形成什么样的新的软件形态？",
        "3.神经符号融合软件的开发、测试和维护面临什么样的特殊问题？围绕相关方面有哪些值得注意的研究进展？同时还面临着什么样的长期挑战？",
        "4.您如何看待特斯拉提出的“软件2.0”的概念？未来符号化程序是否会消失并由神经网络取而代之？",
        "5.神经符号融合软件未来将向什么样的方向发展？您对软件工程、形式化方法、人工智能等相关领域的研究者有什么样的建议？",
    ]
    for q in question:
        multi_agent_discussion(q)
