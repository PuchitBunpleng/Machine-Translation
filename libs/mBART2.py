from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForSeq2SeqLM
import os

model_path = os.path.join(os.getcwd(), "src/models/mBART_Eng2Thai")
th2en_tokenizer = AutoTokenizer.from_pretrained(model_path)
th2en_model = ORTModelForSeq2SeqLM.from_pretrained(model_path)

def en2th(input_sentence):
  src_input = input_sentence
  encoded_input = th2en_tokenizer(src_input, return_tensors="pt")
  generated_tokens = th2en_model.generate(**encoded_input, forced_bos_token_id=th2en_tokenizer.lang_code_to_id["th_TH"])
  return th2en_tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]