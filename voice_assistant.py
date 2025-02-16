import speech_recognition as sr
import pyttsx3
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load the model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Adjust speaking speed
engine.setProperty("volume", 1.0)  # Adjust volume

# Initialize speech recognition
recognizer = sr.Recognizer()

def speak(text):
    """Converts text to speech and speaks it."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Captures voice input and converts it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        try:
            audio = recognizer.listen(source, timeout=5)  # Listen with a timeout
            text = recognizer.recognize_google(audio)  # Convert speech to text
            print(f"You: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError:
            print("Could not request results, check internet connection.")
            return None

while True:
    user_input = listen()
    if user_input is None:
        continue  # If speech is not recognized, keep listening

    if user_input in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        speak("Goodbye!")
        break

    # Process input through AI model
    inputs = tokenizer(user_input, return_tensors="pt")
    reply_ids = model.generate(**inputs)
    response = tokenizer.decode(reply_ids[0], skip_special_tokens=True)

    # Output response
    print(f"Chatbot: {response}")
    speak(response)
