import streamlit as st
from datetime import datetime

# Import the encoder and decoder functions
from caesarCipherEncode import encode_message
from caesarCipherDecode import decode_message

def initialize_session_state():
    """Initialize session state for chat history"""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

def add_to_history(mode, input_text, output_text):
    """Add a new entry to chat history"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    entry = {
        'timestamp': timestamp,
        'mode': mode,
        'input': input_text,
        'output': output_text
    }
    st.session_state.chat_history.insert(0, entry)  # Add to beginning for newest first
    
    # Keep only last 20 entries to prevent memory issues
    if len(st.session_state.chat_history) > 20:
        st.session_state.chat_history = st.session_state.chat_history[:20]

def display_chat_history():
    """Display the chat history in the sidebar"""
    with st.sidebar:
        st.markdown("### 📜 Operation History")
        
        # Clear history button
        if st.button("🗑️ Clear History", type="secondary", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()
        
        if not st.session_state.chat_history:
            st.info("No operations yet. Start encoding or decoding!")
            return
        
        st.markdown("---")
        
        for i, entry in enumerate(st.session_state.chat_history):
            # Create a container for each history entry
            with st.container():
                # Header with timestamp and mode
                mode_emoji = "🔒" if entry['mode'] == "Encode" else "🔓"
                st.markdown(f"""
                <div style="
                    background-color: {'#fef3c7' if entry['mode'] == 'Encode' else '#dbeafe'};
                    padding: 0.5rem;
                    border-radius: 8px;
                    margin-bottom: 0.5rem;
                    border-left: 4px solid {'#f59e0b' if entry['mode'] == 'Encode' else '#3b82f6'};
                ">
                    <small style="color: #6b7280; font-weight: 600;">
                        {entry['timestamp']} - {mode_emoji} {entry['mode']}
                    </small>
                </div>
                """, unsafe_allow_html=True)
                
                # Input section
                st.markdown("**Input:**")
                input_preview = entry['input'][:100] + "..." if len(entry['input']) > 100 else entry['input']
                st.code(input_preview, language=None)
                
                # Output section
                st.markdown("**Output:**")
                output_preview = entry['output'][:100] + "..." if len(entry['output']) > 100 else entry['output']
                st.code(output_preview, language=None)
                
                # Show full text buttons
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📄 Full Input", key=f"input_{i}", use_container_width=True):
                        st.session_state[f'show_full_input_{i}'] = not st.session_state.get(f'show_full_input_{i}', False)
                
                with col2:
                    if st.button("📄 Full Output", key=f"output_{i}", use_container_width=True):
                        st.session_state[f'show_full_output_{i}'] = not st.session_state.get(f'show_full_output_{i}', False)
                
                # Display full text if requested
                if st.session_state.get(f'show_full_input_{i}', False):
                    st.markdown("**Full Input:**")
                    st.code(entry['input'], language=None)
                
                if st.session_state.get(f'show_full_output_{i}', False):
                    st.markdown("**Full Output:**")
                    st.code(entry['output'], language=None)
                
                st.markdown("---")

def main():
    # Initialize session state
    initialize_session_state()
    
    # Page configuration
    st.set_page_config(
        page_title="Caesar Cipher Tool",
        page_icon="🔐",
        layout="wide"  # Changed to wide layout for sidebar
    )
    
    # Custom CSS for professional styling
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 2rem;
        color: #1f2937;
    }
    
    .step-header {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1e40af;
        margin-bottom: 0.5rem;
    }
    
    .step-text {
        color: #4b5563;
        line-height: 1.6;
    }
    
    .result-container {
        background-color: #ecfdf5;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #10b981;
        margin-top: 1rem;
    }
    
    .result-header {
        font-size: 1.1rem;
        font-weight: 600;
        color: #047857;
        margin-bottom: 0.5rem;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #f8fafc;
    }
    
    /* Make sidebar scrollable */
    .css-1lcbmhc {
        max-height: 80vh;
        overflow-y: auto;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Display chat history in sidebar
    display_chat_history()
    
    # Main content area
    # Main header
    st.markdown('<h1 class="main-header">Caesar Cipher by Okasha</h1>', unsafe_allow_html=True)
    
    # Mode selection
    mode = st.radio(
        "Select Operation Mode:",
        options=["Encode", "Decode"],
        horizontal=True,
        key="mode_selection"
    )
    
    # Information section
    with st.expander("ℹ About Caesar Cipher"):
        if mode == "Encode":
            st.write("""
            This advanced cipher combines multiple encryption techniques:
            - **Alternating Caesar Shift**: Letters shifted by +7/+3 alternating pattern
            - **ROT5 Number Rotation**: Digits 0-9 rotated by 5 positions (0→5, 1→6, etc.)
            - **Text Reversal**: Entire string order reversed
            - **Atbash Letter Mirroring**: A↔Z, B↔Y, C↔X pattern for all letters
            - **Symbol Mapping**: Spaces, punctuation mapped to different symbols
            
            **Special Features:**
            - Uppercase letters escaped with '@' prefix
            - Complex symbol mappings for punctuation
            """)
        else:
            st.write("""
            The decoding process reverses all encryption steps in exact reverse order:
            - **Step 1**: Reverse symbol mapping back to originals
            - **Step 2**: Un-mirror letters (reverse Atbash)
            - **Step 3**: Un-reverse text order
            - **Step 4**: Reverse ROT5 on digits (-5 shift)
            - **Step 5**: Reverse alternating Caesar shift (-7/-3 pattern)
            
            **Special Handling:**
            - '@' prefixes indicate original uppercase letters
            - All symbol mappings restored to original punctuation
            """)
    
    # Create two columns for better layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Input section
        if mode == "Encode":
            input_text = st.text_area(
                "Enter Plain Text:",
                placeholder="Type your message here...",
                height=120,
                key="input_area"
            )
        else:
            input_text = st.text_area(
                "Enter Cipher Text:",
                placeholder="Paste your encrypted message here...",
                height=120,
                key="input_area"
            )
        
        # Process button
        if mode == "Encode":
            process_button = st.button("🔒 Encode Text", type="primary", use_container_width=True)
        else:
            process_button = st.button("🔓 Decode Text", type="primary", use_container_width=True)
    
    with col2:
        # Quick stats
        st.markdown("### Quick Stats")
        st.metric("Total Operations", len(st.session_state.chat_history))
        
        if st.session_state.chat_history:
            encode_count = sum(1 for entry in st.session_state.chat_history if entry['mode'] == 'Encode')
            decode_count = len(st.session_state.chat_history) - encode_count
            st.metric("Encodings", encode_count)
            st.metric("Decodings", decode_count)
    
    # Process and display results
    if process_button and input_text.strip():
        try:
            if mode == "Encode":
                result = encode_message(input_text, verbose=False)
                result_title = "Encrypted Cipher Text"
            else:
                result = decode_message(input_text, verbose=False)
                result_title = "Decrypted Plain Text"
            
            # Add to history
            add_to_history(mode, input_text, result)
            
            # Display result
            st.markdown(f"""
            <div class="result-container">
                <div class="result-header">{result_title}:</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.code(result, language=None)
            
            # Download and copy buttons
            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    label="Download Result",
                    data=result,
                    file_name=f"caesar_{'encoded' if mode == 'Encode' else 'decoded'}_text.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            
            with col2:
                # Copy to clipboard button (using JavaScript)
                if st.button("Copy to Clipboard", use_container_width=True):
                    st.code(f"Text ready to copy: {result}")
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    
    elif process_button and not input_text.strip():
        st.warning("Please enter some text to process!")


if __name__ == "__main__":
    main()