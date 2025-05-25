# Streamlit app for SalesMate demo (MAKR 75 Q&A)
import streamlit as st
import openai

st.set_page_config(page_title="SalesMate - MAKR 75 Bot")
st.title("🤖 SalesMate: Ask About MAKR 75")

# Ask user to input OpenAI API Key
api_key = st.text_input("Enter your OpenAI API key:", type="password")

# MAKR 75 knowledge chunk (condensed)
knowledge = """
The Corsair MAKR 75 Barebones is a high-performance DIY mechanical keyboard featuring:
- Hot-swappable sockets supporting 5-pin mechanical switches.
- Fully aluminum case, gasket mount, and 8-layer sound dampening foam.
- Compatible with Cherry MX-style switches (linear, tactile, clicky).
- Supports up to 8000 Hz polling via Corsair AXON.
- No switches included – fully customizable.
"""

# Simple Q&A logic
question = st.text_input("Ask a product question:")

if api_key and question:
    openai.api_key = api_key
    prompt = f"""You are a helpful product expert. Answer the following question based only on the provided knowledge.
    
Knowledge:
{knowledge}

Question: {question}
Answer:"""

    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.3,
        )
        answer = response.choices[0].message.content.strip()
        st.success(answer)
