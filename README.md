# Practice_Chat_Bot 
🤖 Practice Chatbot using Hugging Face Transformers Project Description:  Developed a conversational AI chatbot using the Hugging Face Transformers library and pretrained models like DialoGPT or BlenderBot. The project focused on understanding the architecture of transformer-based models for natural language understanding and generation.  Key Features:  Integrated Hugging Face’s transformers and datasets libraries to utilize pretrained conversational models.  Implemented an interactive user interface using Python (CLI or Streamlit for web-based version).  Fine-tuned response formatting and dialogue flow for natural conversations.  Employed tokenization, attention masks, and contextual embeddings for managing dynamic input/output.  Added functionality to handle greetings, FAQs, and small talk for a realistic chatbot experience.  Skills Used: Python, NLP, Hugging Face Transformers, Pretrained Models, Tokenization, Chatbot Design, Dialog Management.

# Local CLI Chatbot

Simple chatbot using Hugging Face models. Runs entirely on your machine.

## Setup
1. Install requirements:
```bash
pip install transformers torch
```

2. Files:
- model_loader.py
- chat_memory.py
- interface.py

## Usage
Run the chatbot:
```bash
python interface.py
```

Example conversation:
```
User: What's the capital of France?
Bot: The capital of France is Paris.
User: And Italy?
Bot: Rome is the capital of Italy.
User: /exit
Exiting chatbot. Goodbye!
```

## Customization
- Change model: Edit `model_name` in `model_loader.py`
- Adjust memory: Modify `window_size` in `interface.py`
