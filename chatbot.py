import streamlit as st
from chatbot import chatbot_response  # Importing your chatbot code

# Streamlit app title
st.title('Chatbot')

# Main function to run the Streamlit app
def main():
    # Text input for user to type their message
    user_input = st.text_input('You:', '')

    # Check if the user has entered a message
    if user_input:
        # Call the chatbot_response function from your chatbot code
        bot_response = chatbot_response(user_input)
        # Display the bot's response
        st.text_area('Bot:', value=bot_response, height=200)

# Run the main function to start the Streamlit app
if __name__ == '__main__':
    main()
