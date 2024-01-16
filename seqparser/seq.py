# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    rna = []
    for i in range(len(seq)):
        rna.append(seq[i] if seq[i] != "T" else "U")
    
    return "".join(rna)

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    
    rna = []
    for i in range(len(seq)):
        rna.append(seq[i] if seq[i] != "T" else "U")
    
    return "".join(rna)[::-1]