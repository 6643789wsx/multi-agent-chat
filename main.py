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
    
    while count_log_entries(log_file_name) < 100:
        for model in models:
            if count_log_entries(log_file_name) >= 100:
                break
            previous_conversation = read_log(log_file_name)
            response = get_response(model, previous_conversation)
            write_log(log_file_name, f"{model} response: {response}")

if __name__ == "__main__":
    question = "您如何看待大语言模型的“推理”能力？它的“推理”能力与检索增强、外挂工具以及Agent技术等相结合将形成什么样的新的软件形态？"
    multi_agent_discussion(question)
