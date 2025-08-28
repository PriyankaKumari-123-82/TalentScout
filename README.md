# TalentScout Hiring Assistant Chatbot

## Project Overview
The TalentScout Hiring Assistant is an AI-powered chatbot designed to streamline the initial screening process for technology placements. Built with Streamlit and Python, it collects candidate information, validates inputs, and generates tailored technical questions based on the candidate's declared tech stack. The chatbot ensures a seamless user experience, handles sensitive data securely, and integrates with an external API for dynamic question generation.

## Features
- **Greeting and Introduction**: Welcomes candidates and explains the screening process.
- **Information Collection**: Gathers full name, email, phone, experience, position, location, and tech stack.
- **Input Validation**: Validates email and phone number formats.
- **Technical Questions**: Generates 3-5 questions via an external API or fallback question bank.
- **Secure Data Handling**: Hashes sensitive information (email, phone) for storage.
- **Context-Aware Conversation**: Maintains conversation flow and handles unexpected inputs.
- **Environment Variables**: Uses `.env` file to securely store API keys.
- **Conversation Termination**: Gracefully ends the conversation with keywords like "exit" or "quit".

## Project Structure
```
talentscout-hiring-assistant/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   ├── config.py
│   └── question_bank.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/PriyankaKumari-123-82/TalentScout.git
   cd talentscout-hiring-assistant
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file**:
   - In the project root, create a `.env` file with:
     ```env
     TALENTSCOUT_API_KEY=your_api_key_here
     TALENTSCOUT_API_ENDPOINT=https://api.talentscout.mock/v1/questions
     ```
   - Replace `your_api_key_here` with the actual API key.

5. **Run the application**:
   ```bash
   streamlit run src/main.py
   ```

## Usage Guide
1. Open the application in your browser (usually at `http://localhost:8501`).
2. Follow the chatbot's prompts to provide your information.
3. List your tech stack (e.g., "Python, Django, JavaScript").
4. Answer the technical questions provided.
5. Use keywords like "exit" or "quit" to end the conversation.
6. The chatbot will save your data (in-memory for demo) and inform you of next steps.

## Technical Details
- **Programming Language**: Python 3.8+
- **Libraries**:
  - `streamlit`: For the frontend interface.
  - `python-dotenv`: For loading environment variables.
  - `requests`: For API calls.
  - `hashlib`: For hashing sensitive data.
- **Architecture**:
  - Modular design with separate modules for UI, utilities, configuration, and question bank.
  - Session state management using Streamlit's `st.session_state`.
  - Fallback mechanism to a local question bank if API fails.
- **API Integration**:
  - Uses a mock API endpoint for question generation.
  - API key stored securely in `.env` file.
- **Data Privacy**:
  - Sensitive information (email, phone) is hashed using SHA-256.
  - In-memory storage for demo purposes (GDPR-compliant for simulated data).

## Prompt Design
- **Information Gathering**: Prompts are clear and sequential, ensuring candidates provide all required details.
- **Technical Questions**: The API is queried with the tech stack to generate relevant questions. Fallback prompts use a predefined question bank for reliability.
- **Context Handling**: Session state tracks conversation stage and maintains flow.
- **Fallback Mechanism**: Generic responses for unexpected inputs, guiding users back to the required information.

## Challenges & Solutions
- **Challenge**: Securely handling sensitive data.
  - **Solution**: Hash email and phone numbers using SHA-256 before storage.
- **Challenge**: API reliability for question generation.
  - **Solution**: Implement a fallback question bank to ensure functionality if the API fails.
- **Challenge**: Maintaining conversation context.
  - **Solution**: Use Streamlit's session state to track progress and store responses.
- **Challenge**: Secure API key storage.
  - **Solution**: Use `.env` file with `python-dotenv` to avoid hardcoding sensitive information.

## Future Enhancements
- Integrate sentiment analysis to gauge candidate confidence.
- Add multilingual support for broader accessibility.
- Deploy on a cloud platform (e.g., AWS) for scalability.
- Enhance UI with custom Streamlit themes and interactive elements.

## Demo
A video walkthrough demonstrating the chatbot's features is available at [Loom link or local file]. Alternatively, run the application locally to test the functionality.

## License
MIT License
```

### Setup Instructions
1. **Create the project directory**:
   ```bash
   mkdir talentscout-hiring-assistant
   cd talentscout-hiring-assistant
   ```

2. **Create the file structure**:
   - Create the `src` directory and place `main.py`, `utils.py`, `config.py`, `question_bank.py`, and `__init__.py` inside it.
   - Create `.env`, `.gitignore`, `requirements.txt`, and `README.md` in the root directory.

3. **Initialize Git**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit with modular project structure"
   ```

4. **Set up the virtual environment and install dependencies**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

5. **Configure the `.env` file**:
   - Add the API key and endpoint as shown in the `.env` file above.

6. **Run the application**:
   ```bash
   streamlit run src/main.py
   ```

### Explanation of Segregation
- **Modularity**: Separating the code into `main.py` (UI and conversation logic), `utils.py` (business logic), `config.py` (environment variables), and `question_bank.py` (static data) improves maintainability and scalability.
- **Security**: The `.env` file stores sensitive API keys, excluded from version control via `.gitignore`.
- **Reusability**: Utility functions in `utils.py` can be reused across other parts of the application.
- **Documentation**: The `README.md` provides clear setup and usage instructions, meeting the documentation requirements.
- **Dependencies**: `requirements.txt` ensures consistent dependency installation.

### Notes
- **API Integration**: The code assumes a mock API (`https://api.talentscout.mock/v1/questions`). If you have a real API (e.g., xAI's API at `https://x.ai/api`), provide its documentation, and I can adjust the `utils.py` API call accordingly.
- **Data Storage**: In-memory storage is used for simplicity. For production, consider integrating a database like SQLite or PostgreSQL in `utils.py`.
- **Bonus Features**: To add sentiment analysis or multilingual support, I can extend `utils.py` with libraries like `textblob` or `googletrans`.
- **Cloud Deployment**: For AWS/GCP deployment, specify the platform, and I can provide detailed steps.

### Deliverables
- **Source Code**: Provided as separate files in a modular structure.
- **Documentation**: Comprehensive `README.md` included.
- **Demo**: Run locally or create a Loom video showcasing the chatbot. For cloud deployment, deploy on AWS EC2 and share the public URL.

Let me know if you need help with deployment, additional features, or specific API integration!
