import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# --- Title ---
st.title("✨ AI Story Generator")
st.write("Create your own story with the power of AI! (GPT-2 model)")


# --- Load model and tokenizer ---
@st.cache_resource  # để cache model, không tải lại mỗi lần
def load_model():
    model_name = "NlpHUST/gpt2-vietnamese"  # ✅ model tiếng Việt
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    return tokenizer, model, device


tokenizer, model, device = load_model()

# --- User input ---
prompt = st.text_area("Nhập phần mở đầu cho câu chuyện:",
                      "Ngày xửa ngày xưa, có một cậu bé sống trong một ngôi làng nhỏ.")

max_length = st.slider("Story length (tokens)", 50, 500, 200)
temperature = st.slider("Creativity level (temperature)", 0.3, 1.5, 0.8)

# --- Generate button ---
if st.button("Generate Story"):
    with st.spinner("✨ AI is writing your story..."):
        input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
        output = model.generate(
            input_ids,
            max_new_tokens=max_length,
            temperature=temperature,
            top_p=0.9,
            do_sample=True,
            repetition_penalty=1.2
        )
        story = tokenizer.decode(output[0], skip_special_tokens=True)

    st.subheader("Your AI-generated story:")
    st.write(story)
