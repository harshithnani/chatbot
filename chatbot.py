import streamlit as st
import torch
import transformers

# Install required packages
st.title('Chatbot')

# Initialize chatbot components
# (Add your chatbot initialization code here)

# Define function to interact with chatbot
def chatbot_response(user_input):
    # Call your chatbot model/pipeline to get response
    response = query_pipeline(user_input)
    return response

# Define Streamlit UI
user_input = st.text_input('You:', '')
if st.button('Send'):
    if user_input:
        bot_response = chatbot_response(user_input)
        st.text_area('Bot:', value=bot_response, height=200)

# Load chatbot model
model_id = 'meta-llama/Llama-2-7b-chat-hf'
hf_auth = "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"
model_config = transformers.AutoConfig.from_pretrained(
    model_id,
    use_auth_token=hf_auth
)
model = transformers.LlamaForCausalLM.from_pretrained(
    model_id,
    trust_remote_code=True,
    config=model_config,
    quantization_config=bnb_config,
    device_map='auto',
    use_auth_token=hf_auth,
)
tokenizer = transformers.AutoTokenizer.from_pretrained(
    model_id,
    use_auth_token=hf_auth
)
query_pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.float16,
    device_map="auto",
)

# Run Streamlit app
if __name__ == '__main__':
    st.run()

