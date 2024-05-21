from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForSeq2SeqLM
import os
import sys

if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
else:
    app_path = os.path.dirname(os.path.abspath(__file__))

en2th_model_path = os.path.join(os.path.dirname(app_path), "src/models/mBART2_Eng2Thai")
en2th_tokenizer = AutoTokenizer.from_pretrained(en2th_model_path)
en2th_model = ORTModelForSeq2SeqLM.from_pretrained(en2th_model_path)

th2en_model_path = os.path.join(os.path.dirname(app_path), "src/models/mBART2_Thai2Eng")
th2en_tokenizer = AutoTokenizer.from_pretrained(th2en_model_path)
th2en_model = ORTModelForSeq2SeqLM.from_pretrained(th2en_model_path)

def en2th(input_sentence):
  src_input = input_sentence
  encoded_input = en2th_tokenizer(src_input, return_tensors="pt")
  generated_tokens = en2th_model.generate(**encoded_input, forced_bos_token_id=en2th_tokenizer.lang_code_to_id["th_TH"])
  return en2th_tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

def th2en(input_sentence):
  src_input = input_sentence
  encoded_input = th2en_tokenizer(src_input, return_tensors="pt")
  generated_tokens = th2en_model.generate(**encoded_input, forced_bos_token_id=th2en_tokenizer.lang_code_to_id["en_XX"])
  return th2en_tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]