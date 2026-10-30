from transformers import T5ForConditionalGeneration, T5Tokenizer
def qgen():
  model_name = "valhalla/t5-base-qg-hl"
  model = T5ForConditionalGeneration.from_pretrained(model_name)
  tokenizer = T5Tokenizer.from_pretrained(model_name)

  # Example with highlighted text
  context = "The Great Wall of China is one of the most remarkable architectural feats in history. It was originally built to protect the Chinese states and empires from nomadic invasions and raids. Construction began as early as the <hl>7th century BC<hl> and continued through several dynasties, including the Qin, Han, and Ming. The wall stretches over <hl>13,000 miles<hl>, making it the longest man-made structure in the world. One of the most iconic sections of the wall near <hl>Beijing<hl> is visited by millions of tourists every year. Despite its historical military purpose, the Great Wall has become a symbol of <hl>China's strength and perseverance<hl>. In 1987, it was designated as a <hl>UNESCO World Heritage Site<hl>, recognizing its cultural and historical importance."
    # The model expects <hl> to highlight the answer inside the text for each question.
    # We'll highlight manually for now. Later we can automate it.
  input_text = f"generate questions: {context}"
  input_ids = tokenizer.encode(input_text, return_tensors="pt")

  output = model.generate(
        input_ids=input_ids,
        max_length=128,
        num_beams=4,
        early_stopping=True
    )

  decoded = tokenizer.decode(output[0], skip_special_tokens=True)
  questions = list(set(q.strip() for q in decoded.split("<sep>") if q.strip()))
  return questions



questions=qgen()
print("Generated Questions:")
for q in questions:
    print("-", q)
