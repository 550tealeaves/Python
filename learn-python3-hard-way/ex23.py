# STRINGS, BYTES, AND CHARACTER ENCODINGS
# uses utf-8, utf-16, and big5 encodings to show conversion and types of errors you get
# Aforementioned names = "codec" but you use the parameter "encoding"
# What is an encode? - Standard for how sequence of bits shoudl represent a number
## Ex: byte = sequence of 8 bits (1s & 0s)
# UTF-8 - unicode transformation format 8 bits - convention that encodes Unicode characters into sequences of bytes, which are sequences of bits, which turn sequences of switches on/off
# String = UTF-8 encoded sequence of characters for handling text


import sys
# script, input_encoding, error = sys.argv  # Removed sys.argv

def main(language_file, encoding, errors):
  line = language_file.readline()
  if line:
    print_line(line, encoding, errors)
    return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
  next_lang = line.strip()
  raw_bytes = next_lang.encode(encoding, errors=errors)
  # Corrected typo in decode arguments
  cooked_string = raw_bytes.decode(encoding, errors=errors)


  print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

# Directly providing the encoding and error handling values
main(languages, "utf-8", "strict")