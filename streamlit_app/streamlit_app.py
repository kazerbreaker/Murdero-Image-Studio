import streamlit as st
import requests
import os
from dotenv import load_dotenv
from PIL import Image
import io
import time

# Load environment variables - try multiple locations for local dev and Streamlit Cloud
# Try parent directory first (local development), then current directory (Streamlit Cloud)
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
if not os.path.exists(env_path):
    env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

def generate_image(prompt, model):
    """Handles the Text-to-Image generation using the selected model."""
    api_key = os.getenv("CHUTES_API_TOKEN")
    if not api_key or api_key == "YOUR_API_KEY_HERE":
        st.error("""
        API key not found. Please set your Chutes AI API key:
        
        **For Local Development:**
        - Create a `.env` file in the project root with: `CHUTES_API_TOKEN="your_actual_api_key"`
        
        **For Streamlit Cloud:**
        - Go to your app settings → Secrets
        - Add: `CHUTES_API_TOKEN = "your_actual_api_key"`
        """)
        st.stop()
    if not prompt:
        st.error("Prompt is required.")
        st.stop()

    # Optimized negative prompt without redundancy
    negative_prompt = "low quality, blurry, watermark, text, anatomical issues, extra limbs, mutated hands, asymmetrical features"

    width = 1024
    height = 1024

    url = "https://image.chutes.ai/generate"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": st.session_state.internal_model,
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "guidance_scale": st.session_state.guidance_scale,
        "width": width,
        "height": height,
        "num_inference_steps": st.session_state.steps
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        image_bytes = response.content
        try:
            image = Image.open(io.BytesIO(image_bytes))
        except Exception as img_e:
            st.error(f"Invalid image response from API: {img_e}")
            st.stop()
        
        return image
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}\nTried endpoint: {url}\nModel: {model}")
        st.stop()

# Custom CSS for enhanced beauty (modern, clean theme with better spacing and shadows)
st.markdown("""
<style>
    :root {
        --primary: #1a73e8;
        --secondary: #4a90e2;
    }

    .stApp {
        padding: 0 !important;
        margin: 0 !important;
    }

    .stButton>button {
        background: linear-gradient(45deg, var(--primary), var(--secondary)) !important;
        transition: transform 0.2s ease;
    }

    .image-container {
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
# Initialize all runtime parameters
if 'generated_image' not in st.session_state:
    st.session_state.guidance_scale = 7.5
    st.session_state.steps = 50
    st.session_state.generated_image = None
if 'prompt' not in st.session_state:
    st.session_state.prompt = ""
if 'selected_model_display' not in st.session_state:
    st.session_state.selected_model_display = "Chroma"
if 'internal_model' not in st.session_state:
    st.session_state.internal_model = "chroma"

st.title('El Murdero Image Studio')
st.write('Generate stunning visuals powered by Chutes AI Models: Chroma & Qwen Image')

# Rate limit note
st.markdown('<div class="note">Note: Qwen Image and FLUX-1 Schnell models are rate-limited; Chroma, JuggernautXL, and Neta Lumina are available for free.</div>', unsafe_allow_html=True)

# Main controls (no sidebar, all in main area)
st.subheader("Generation Controls")

# Model selection with display names
display_to_internal = {
    "Chroma": "chroma",
    "Qwen Image": "qwen-image",
    "JuggernautXL": "JuggernautXL",
    "Neta Lumina": "neta-lumina",
    "FLUX-1 Schnell": "FLUX.1-schnell"
}

# Calculate index based on current selected_model_display
index = 0
if 'selected_model_display' in st.session_state and st.session_state.selected_model_display in display_to_internal:
    index = list(display_to_internal.keys()).index(st.session_state.selected_model_display)

st.session_state.selected_model_display = st.selectbox(
    "Select AI Model",
    options=list(display_to_internal.keys()),
    index=index,
    help="Chroma/JuggernautXL/Neta Lumina: Free generation | Qwen Image/FLUX-1 Schnell: Rate-limited"
)

# Map display to internal model value
st.session_state.internal_model = display_to_internal[st.session_state.selected_model_display]

# Dynamic negative prompt in expander (collapsible for better space management)
with st.expander("Negative Prompt Details (Fixed for Model)", expanded=False):
    negative_prompt = "low quality, blurry, watermark, text, anatomical issues, extra limbs, mutated hands, asymmetrical features"
    st.info("Robust negative prompt optimized for both models to ensure proper anatomy and high-quality outputs.")
    
    st.text_area(
        "Negative Prompt",
        value=negative_prompt,
        height=120,
        disabled=True,
        help="This fixed prompt is automatically applied based on the selected model for optimal results."
    )

# Prompt input
st.session_state.prompt = st.text_area(
    "Describe Your Image",
    value=st.session_state.prompt,
    placeholder="e.g., A serene mountain landscape at sunset with vibrant colors and misty valleys",
    height=150,
    help="Provide a detailed description to guide the AI in generating your desired image."
)

# Generation parameters
with st.expander("Advanced Settings"):
    st.session_state.guidance_scale = st.slider("Guidance Scale", 1.0, 20.0, 7.5, 0.5)
    st.session_state.steps = st.slider("Inference Steps", 10, 150, 50, 10)

# Buttons
col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    generate_clicked = st.button("Generate Image", type="primary", use_container_width=True)
with col_btn2:
    clear_clicked = st.button("New Image", type="secondary", use_container_width=True)

# Main area for image output (improved layout)
st.markdown("---")
st.subheader("Generated Image Preview")

if generate_clicked:
    if st.session_state.prompt.strip():
        with st.spinner("Creating your image... This may take a few moments."):
            progress_bar = st.progress(0)
            status_text = st.empty()
            status_text.text("Initializing generation...")
            progress_bar.progress(10)
            
            image = generate_image(st.session_state.prompt, st.session_state.internal_model)
            st.session_state.generated_image = image
            
            progress_bar.progress(100)
            status_text.text("Image generated successfully!")
            time.sleep(1)  # Brief pause for user to see completion
            st.rerun()
    else:
        st.error("Please enter a detailed prompt to generate an image.")

if clear_clicked:
    if st.session_state.generated_image:
        st.session_state.generated_image.close()  # Close the image to free memory
    st.session_state.generated_image = None
    st.session_state.prompt = ""
    st.session_state.selected_model_display = "Chroma"
    st.session_state.internal_model = "chroma"
    st.rerun()

# Image display with download option
if st.session_state.generated_image:
    with st.container():
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(st.session_state.generated_image, width='stretch', caption="Your Generated Image")
        
        # Download button using BytesIO
        img_bytes = io.BytesIO()
        st.session_state.generated_image.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        st.download_button(
            label="Download Image",
            data=img_bytes.getvalue(),
            file_name=f"generated_image_{time.strftime('%Y%m%d-%H%M%S')}.png",
            mime="image/png",
            use_container_width=True
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.success("Image generated successfully!")
else:
    st.markdown('<div class="info-box">Enter a prompt above and click Generate to create your first image!</div>', unsafe_allow_html=True)

# Footer with author
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #64748b; font-size: 0.9rem;'>
        Powered By <strong>Chutes AI</strong> | Created by <strong>El Murdero</strong>
    </div>
    """,
    unsafe_allow_html=True
)