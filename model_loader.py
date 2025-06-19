from transformers import pipeline, AutoTokenizer

def load_model():
    """Loads model and tokenizer from Hugging Face Hub"""
    model_name = "distilgpt2"  # Small model (~500MB)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    generator = pipeline(
        "text-generation", 
        model=model_name,
        tokenizer=tokenizer,
        device=-1  # -1 = CPU, 0+ = GPU
    )
    return generator

# Test locally: python model_loader.py
if __name__ == "__main__":
    print("Loading model...")
    model = load_model()
    print("Model loaded successfully!")