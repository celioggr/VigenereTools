# VigenereTools
> Simple tools that might help cracking Vigenère cipher

The scripts here presented may be used to crack Vigenere Cipher by providing you the key size used on the Ciphering process.
Please notice that `patterns.py` looks for patterns (on a specified interval of lengths) in the ciphered text. Which means that it may no be practical if the ciphered text is too big.
Nevertheless `IndexOfCoincidence.py` will work just fine for big texts. This method needs to know the Index of coincidence of the language's plaintext and the interval of probable key lengths.
