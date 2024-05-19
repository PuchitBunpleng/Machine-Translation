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

def preprocessing(src_sentence):
    src_vocab = spm.SentencePieceProcessor(model_file='spm.model')
    moses_tokenizer = MosesTokenizer()
    tokens = moses_tokenizer.tokenize(src_sentence)
    encoded_tokens = src_vocab.encode(tokens, out_type=int)
    flattened_encoded_tokens = [item for sublist in encoded_tokens for item in (sublist if isinstance(sublist, list) else [sublist])]
    src_tensor = torch.tensor([flattened_encoded_tokens], dtype=torch.long)

def translate(model, src_tensor, src_vocab, tgt_vocab, max_len):
    batch_size = src.size(0)
    tgt_input = torch.tensor([[tgt_vocab.bos_id()]] * batch_size)

    for _ in range(max_len):
        src_mask, tgt_mask = model.generate_mask(src, tgt_input)
        with torch.no_grad():
            output = model1(src, tgt_input)
        last_token_logits = output[:, -1, :]
        next_tokens = last_token_logits.argmax(dim=-1)
        next_tokens = next_tokens.unsqueeze(1)
        tgt_input = torch.cat([tgt_input, next_tokens], dim=1)

        if (next_tokens == tgt_vocab.eos_id()).all():
            break

    tgt_tokens_list = tgt_input.tolist()
    translations = [tgt_vocab.decode(tokens) for tokens in tgt_tokens_list]

    return translations

ENG2TH_model = tBasedMTL.Transformer(SRC_VOCAB_SIZE, TGT_VOCAB_SIZE, D_MODEL, NUM_HEADS, NUM_LAYERS, D_FF, MAX_SEQ_LENGTH, DROPOUT)
ENG2TH_model.load_state_dict(torch.load('src/models/Transformer_en-th.h5'))
ENG2TH_model.eval()

TH2ENG_model = tBasedMTL.Transformer(SRC_VOCAB_SIZE, TGT_VOCAB_SIZE, D_MODEL, NUM_HEADS, NUM_LAYERS, D_FF, MAX_SEQ_LENGTH, DROPOUT)
TH2ENG_model.load_state_dict(torch.load('src/models/Transformer_th-en.h5'))
TH2ENG_model.eval()