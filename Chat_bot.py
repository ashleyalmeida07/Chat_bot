

import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()


genai.configure(api_key=os.getenv("Gemini API Key"))

generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  safety_settings=safety_settings,
  generation_config=generation_config,
  system_instruction="Imagine you are a friendly, knowledgeable, and conversational chatbot assistant. You have broad general knowledge and can provide information on a wide range of topics, from technology and science to hobbies, travel, and personal advice. Your tone is friendly, approachable, and engaging, making you easy to talk to and helpful for users who need information or just want to chat.",

)



chat_session = model.start_chat(
    history=[]
)

print("Bot: Hello, how can I help you?")
print()

while True:

    user_input = input("You: ")
    print()

    response = chat_session.send_message(user_input)

    cleaned_response = response.text.replace("*", "").strip()

    print(f'Bot: {cleaned_response}')
    print()

    chat_session.history.append({"role": "user", "parts": [user_input]})
    chat_session.history.append({"role": "model", "parts": [cleaned_response]})

    
