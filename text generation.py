from transformers import pipeline

# Tạo mô hình sinh văn bản (GPT-2)
generator = pipeline("text-generation", model="gpt2")

# Nhập prompt
prompt = "Once upon a time in a quiet village, there was a young boy who"

# Sinh truyện
story = generator(
    prompt,
    max_length=150,
    num_return_sequences=1,
    temperature=0.8,
)

# In kết quả
print("\n✨ Your AI-generated story:\n")
print(story[0]["generated_text"])