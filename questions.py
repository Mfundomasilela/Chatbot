
# Question Generation and Answer Extraction

from transformers import pipeline T5Tokenizer, T5ForConditionalGeneration

#Load the pre-trained model
tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

def generate_questions(context):
    input_text = "generate question: " + context
    input_ids= tokenizer.encode( input_text, return_tensors="pt")
    outputs = model.generate(input_ids)
    question = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return question
