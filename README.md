
# Voice-Powered Chatbot using Blenderbot-400M  

This project is a voice-enabled chatbot that listens to user inputs, generates intelligent responses using **Blenderbot-400M**, and replies using text-to-speech. It provides a seamless, hands-free conversational experience powered by advanced AI and speech recognition.  







## Features:  
- **Speech Recognition:** Captures and transcribes voice input using `SpeechRecognition` and Google Web Speech API.  
- **Conversational AI:** Utilizes `Blenderbot-400M` from Hugging Face to generate human-like responses.  
- **Text-to-Speech:** Uses `pyttsx3` to convert text replies into spoken words.  
- **Continuous Interaction:** Listens and responds until the user says "exit," "quit," or "bye."  

---

## Prerequisites:  
- **Python 3.x**  
- **Microphone** for voice input  
- **Internet Connection** for speech recognition and model processing  

---

## Installation:  
1. Clone the repository:  
```bash
git clone <REPOSITORY_URL>
cd <REPOSITORY_FOLDER>
```

2. Install the required dependencies:  
```bash
pip install speechrecognition pyttsx3 transformers torch
```

3. For **PyAudio** (required for speech recognition):  
```bash
pip install pipwin
pipwin install pyaudio
```

---

## Usage:  
1. Run the Python script:  
```bash
python chatbot.py
```
2. Speak naturally into the microphone.  
3. The chatbot will listen, respond, and continue the conversation.  
4. Say "exit," "quit," or "bye" to end the conversation.  

---

## How It Works:  
1. **Listen:** Captures voice input and converts it to text using `SpeechRecognition`.  
2. **Generate Response:** Processes the input using `Blenderbot-400M` to generate a conversational reply.  
3. **Speak:** The chatbot's response is spoken aloud using `pyttsx3`.  
4. **Repeat:** Continuously listens for further inputs until an exit command is given.  

---

## Example:  
```
Listening...
You: What's your name?
Chatbot: I'm just a chatbot, but you can call me whatever you like!
```

---

## Future Enhancements:  
- Support for more voice recognition services.  
- Improved contextual understanding and personalized interactions.  
- Integration with advanced conversational models for richer dialogue.  

---

## Contributing:  
Contributions are welcome! Feel free to open issues or submit pull requests for improvements or bug fixes.  

---

## License:  
This project is open-source and available under the **MIT License**.  

---

## Acknowledgements:  
- [Hugging Face Transformers](https://huggingface.co/) for the Blenderbot-400M model  
- [Google Web Speech API](https://cloud.google.com/speech-to-text) for speech recognition  
- [Pyttsx3](https://pypi.org/project/pyttsx3/) for text-to-speech  

---

Feel free to contribute, suggest enhancements, or report issues!  

