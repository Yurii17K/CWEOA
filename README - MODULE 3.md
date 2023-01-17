# List of files
- Task 1: `fast_addition_on_EC.py`
- Task 2: `public_private_keys.py`
- Task 3: `message_encoding_decoding.py`
- Task 4-5: `Elgamal_encryption_decryption_on_EC.py`

# Improvements
- no more negative numbers finally (fixed basic arithmetic to its peak)
- improvements in root finding due to the Tonneli Shanks alg
- FINALLY adding two points gives a correct result after days of me being apparently *brain-dead*. 
The lust bug (among all fixed) was in divison working not over FF but just as is: 
6 / 4 mod 7 would give (1,2), instead of a 5. That feeling when fixes something afer 2 weeks of struggling😅