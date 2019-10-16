# Perform standard imports:
import spacy
nlp = spacy.load('en_core_web_sm')
tokens = nlp("(B) Borrower is JUAN PABLO CAMPOS AND DAYSI MIRIAN OLIVARES, HUSBAND AND WIFE, AS JOINT TENANTS, Borrower is the trustor under this Security Instrument.")
print(tokens[0],tokens[1],tokens[2])