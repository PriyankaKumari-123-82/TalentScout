import re
import hashlib
import requests
from datetime import datetime
from src.config import API_KEY, API_ENDPOINT
from src.question_bank import QUESTION_BANK

# In-memory storage for demo
candidate_data = {}

def hash_sensitive_info(info):
    """Hash sensitive information like email and phone for storage."""
    return hashlib.sha256(info.encode()).hexdigest()

def validate_email(email):
    """Validate email format."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def validate_phone(phone):
    """Validate phone number format."""
    phone_regex = r'^\+?\d{10,15}$'
    return re.match(phone_regex, phone) is not None

def generate_technical_questions(tech_stack):
    """Generate 3-5 technical questions based on the tech stack via API or fallback to question bank."""
    techs = [tech.strip().lower() for tech in tech_stack.split(",")]
    questions = []

    if API_KEY and API_ENDPOINT:
        try:
            # Make API call to fetch questions
            headers = {"Authorization": f"Bearer {API_KEY}"}
            payload = {"tech_stack": techs, "num_questions": 5}
            response = requests.post(API_ENDPOINT, json=payload, headers=headers, timeout=5)
            
            if response.status_code == 200:
                questions = response.json().get("questions", [])
                if questions:
                    return questions[:5]
                else:
                    st.warning("API returned no questions. Using fallback question bank.")
            else:
                st.error(f"API request failed with status {response.status_code}. Using fallback.")
        except requests.RequestException as e:
            st.error(f"Error connecting to API: {e}. Using fallback question bank.")

    # Fallback to local question bank
    for tech in techs:
        if tech in QUESTION_BANK:
            questions.extend(QUESTION_BANK[tech][:3])
    
    if not questions:
        questions.append("Please describe your experience with the specified tech stack.")
    return questions[:5]  # Limit to 5 questions max

def save_candidate_data():
    """Save candidate data to in-memory storage with timestamp."""
    import streamlit as st
    candidate_id = hashlib.md5(st.session_state.candidate_info["email"].encode()).hexdigest()
    candidate_data[candidate_id] = {
        "info": st.session_state.candidate_info,
        "responses": st.session_state.responses,
        "timestamp": datetime.now().isoformat()
    }