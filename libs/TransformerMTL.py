import torch
import tBasedMTL as tBasedMTL
import sentencepiece as spm
from sacremoses import MosesTokenizer

SRC_VOCAB_SIZE = 32000
TGT_VOCAB_SIZE = 32000
D_MODEL = 512
NUM_HEADS = 4
NUM_LAYERS = 3
D_FF = 1024
MAX_SEQ_LENGTH = 700
DROPOUT = 0.1

def ENG2TH_preprocessing(src_sentence):
    src_vocab = spm.SentencePieceProcessor(model_file='spm_en-th.model')
    moses_tokenizer = MosesTokenizer()
    tokens = moses_tokenizer.tokenize(src_sentence)
    encoded_tokens = src_vocab.encode(tokens, out_type=int)
    flattened_encoded_tokens = [item for sublist in encoded_tokens for item in (sublist if isinstance(sublist, list) else [sublist])]
    src_tensor = torch.tensor([flattened_encoded_tokens], dtype=torch.long)
    return src_tensor

ENG2TH_model = tBasedMTL.Transformer(SRC_VOCAB_SIZE, TGT_VOCAB_SIZE, D_MODEL, NUM_HEADS, NUM_LAYERS, D_FF, MAX_SEQ_LENGTH, DROPOUT)
ENG2TH_model.load_state_dict(torch.load('src/models/Transformer_en-th.h5'))
ENG2TH_model.eval()
output = ENG2TH_model(ENG2TH_preprocessing("Hello World"))
print(output)
# TH2ENG_model = tBasedMTL.Transformer(SRC_VOCAB_SIZE, TGT_VOCAB_SIZE, D_MODEL, NUM_HEADS, NUM_LAYERS, D_FF, MAX_SEQ_LENGTH, DROPOUT)
# TH2ENG_model.load_state_dict(torch.load('src/models/Transformer_th-en.h5'))
# TH2ENG_model.eval()