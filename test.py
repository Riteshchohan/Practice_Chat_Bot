from transformers import pipeline
test_model = pipeline('text-generation', model='gpt2')
print(test_model("Hello, world!", max_length=20)[0]['generated_text'])
