from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Use Zephyr 7B (instruction-tuned, open access)
model_name = "HuggingFaceH4/zephyr-7b-alpha"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    torch_dtype=torch.float16, 
    device_map="auto"
)

# Input paragraph
paragraph = """
Albert Einstein was a German-born theoretical physicist who developed the theory of relativity, 
one of the two pillars of modern physics. His work is also known for its influence on the philosophy 
of science. He received the 1921 Nobel Prize in Physics for his explanation of the photoelectric effect, 
a pivotal step in the development of quantum theory.
"""

# Prompt
prompt = f"""<|system|>
You are a helpful assistant that generates multiple choice questions from educational content.
<|user|>
Generate 5 multiple choice questions based on the following text:

{paragraph}

Return only the questions and options, numbered from 1 to 5.
<|assistant|>
"""

# Tokenize and prepare for generation
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

# Generate
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=500,
        temperature=0.7,
        top_p=0.95,
        do_sample=True,
        repetition_penalty=1.2
    )

# Decode and print
output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(output_text)
