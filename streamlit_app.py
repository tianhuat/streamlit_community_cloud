import streamlit as st
import openai
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Configure OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Page configuration
st.set_page_config(
    page_title="GPT-4o-mini Chat",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .stTextInput > div > div > input {
        background-color: #f0f2f6;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .chat-message.user {
        background-color: #e3f2fd;
        align-items: flex-end;
    }
    .chat-message.bot {
        background-color: #f5f5f5;
        align-items: flex-start;
    }
    .chat-message .avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin-bottom: 0.5rem;
    }
    .chat-message .message {
        background-color: white;
        padding: 0.75rem 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        max-width: 80%;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "api_key_valid" not in st.session_state:
        st.session_state.api_key_valid = False

def validate_api_key():
    """Validate OpenAI API key"""
    api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY", "")
    
    if not api_key:
        return False
    
    try:
        # Test API key with a simple request
        client = openai.OpenAI(api_key=api_key)
        client.models.list()
        return True
    except Exception as e:
        st.error(f"Invalid API key: {str(e)}")
        return False

def get_gpt_response(messages):
    """Get response from GPT-4o-mini"""
    try:
        api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY", "")
        client = openai.OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7,
            max_tokens=1000,
            stream=True
        )
        
        return response
    except Exception as e:
        st.error(f"Error getting response: {str(e)}")
        return None

def display_chat_message(role, content):
    """Display a chat message with styling"""
    if role == "user":
        st.markdown(f"""
        <div class="chat-message user">
            <div class="message">
                <strong>You:</strong><br>{content}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message bot">
            <div class="message">
                <strong>GPT-4o-mini:</strong><br>{content}
            </div>
        </div>
        """, unsafe_allow_html=True)

def main():
    """Main application function"""
    initialize_session_state()
    
    # Header
    st.title("🤖 GPT-4o-mini Chat Interface1")
    st.markdown("Chat with OpenAI's GPT-4o-mini model in real-time!")
    
    # Sidebar
    with st.sidebar:
        st.header("Settings")
        
        # API Key status
        if validate_api_key():
            st.success("✅ API Key is valid")
            st.session_state.api_key_valid = True
        else:
            st.error("❌ API Key not found or invalid")
            st.session_state.api_key_valid = False
            st.info("Please set your OPENAI_API_KEY in the environment variables or Streamlit secrets.")
        
        # Clear chat button
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.rerun()
        
        # Chat statistics
        st.subheader("Chat Statistics")
        st.metric("Total Messages", len(st.session_state.messages))
        
        # Instructions
        st.subheader("Instructions")
        st.markdown("""
        1. Ensure your OpenAI API key is set
        2. Type your message in the input box
        3. Press Enter or click Send
        4. Wait for GPT-4o-mini's response
        """)
    
    # Main chat interface
    if not st.session_state.api_key_valid:
        st.warning("Please configure your OpenAI API key to start chatting.")
        return
    
    # Display chat history
    chat_container = st.container()
    
    with chat_container:
        for message in st.session_state.messages:
            display_chat_message(message["role"], message["content"])
    
    # Chat input form
    with st.form("chat_form", clear_on_submit=True):
        col1, col2 = st.columns([4, 1])
        
        with col1:
            user_input = st.text_input(
                "Type your message here...",
                placeholder="Ask me anything!",
                label_visibility="collapsed"
            )
        
        with col2:
            send_button = st.form_submit_button("Send", type="primary", use_container_width=True)
    
    # Handle user input
    if send_button and user_input.strip():
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Display user message
        display_chat_message("user", user_input)
        
        # Prepare messages for API
        api_messages = [{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.messages]
        
        # Get and display bot response
        with st.spinner("GPT-4o-mini is thinking..."):
            response_stream = get_gpt_response(api_messages)
            
            if response_stream:
                # Create placeholder for streaming response
                response_placeholder = st.empty()
                full_response = ""
                
                # Stream the response
                for chunk in response_stream:
                    if chunk.choices[0].delta.content is not None:
                        full_response += chunk.choices[0].delta.content
                        # Update the placeholder with current response
                        response_placeholder.markdown(f"""
                        <div class="chat-message bot">
                            <div class="message">
                                <strong>GPT-4o-mini:</strong><br>{full_response}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Add bot response to chat history
                st.session_state.messages.append({"role": "assistant", "content": full_response})
        
        # Rerun to update the interface
        st.rerun()

if __name__ == "__main__":
    main()

