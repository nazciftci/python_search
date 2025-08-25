import re

def normalize_spaces(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()

def split_sentences(text: str):
    """ Noktalama işaretlerine göre cümleleri böl ve işaretleri koru """
    sentences = re.findall(r'[^.!?]*[.!?]', text, re.MULTILINE | re.DOTALL)
    return [normalize_spaces(s) for s in sentences if s.strip()]
 ## metin işleniyor