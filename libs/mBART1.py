from transformers import MBartForConditionalGeneration, MBart50Tokenizer
import os
import sys

if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
else:
    app_path = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(os.path.dirname(app_path), "src/models")
model_en_th = MBartForConditionalGeneration.from_pretrained(os.path.join(model_path, 'mBART1_Eng2Thai'))
model_th_en = MBartForConditionalGeneration.from_pretrained(os.path.join(model_path, 'mBART1_Thai2Eng'))

tokenizer = MBart50Tokenizer.from_pretrained(os.path.join(model_path, 'mBART1_Tokenizer'))

def en2th(input_text):
    input_tokens = tokenizer(input_text, return_tensors="pt")
    translated_ids = model_en_th.generate(input_tokens.input_ids, max_length=len(input_text)+20, num_beams=7, early_stopping=True)
    translated_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True)
    return translated_text

def th2en(input_text):
    input_tokens = tokenizer(input_text, return_tensors="pt")
    translated_ids = model_th_en.generate(input_tokens.input_ids, max_length=len(input_text)+20, num_beams=7, early_stopping=True)
    translated_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True)
    return translated_text