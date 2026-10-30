from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
def qgen(context):
  model_name = "valhalla/t5-small-e2e-qg"
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
  # Example
  input_text = f"generate questions: {context}"
  input_ids = tokenizer.encode(input_text, return_tensors="pt")
    
  output = model.generate(
        input_ids,
        max_length=64,
        num_beams=8,
        num_return_sequences=8,
        do_sample=True,
        early_stopping=True
    )
  questions=tokenizer.decode(output[0], skip_special_tokens=True)
  questions=questions.split("<sep>")
  return questions
context="The Taj Mahal was built by Mughal emperor Shah Jahan in memory of his wife Mumtaz Mahal. It is located in Agra, India, and is one of the most famous monuments in the world."
questions=qgen(context)
for i in questions:
    print(i)
