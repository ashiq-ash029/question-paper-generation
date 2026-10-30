from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# 1. Define tokenizer FIRST
tokenizer = AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta")

# 2. Then define model
model = AutoModelForCausalLM.from_pretrained(
    "HuggingFaceH4/zephyr-7b-beta",
    torch_dtype=torch.float16,
    device_map="auto"
)

# 3. Now use them together
inputs = tokenizer("Hello, world!", return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=20)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))