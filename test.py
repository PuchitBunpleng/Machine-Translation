from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForSeq2SeqLM

model_path = "./src/models/mBART_Eng2Thai"
new_tokenizer = AutoTokenizer.from_pretrained(model_path)
new_model = ORTModelForSeq2SeqLM.from_pretrained(model_path)

src_input = "I love train"
encoded_input = new_tokenizer(src_input, return_tensors="pt")
generated_tokens = new_model.generate(**encoded_input, forced_bos_token_id=new_tokenizer.lang_code_to_id["th_TH"])
print(new_tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0])