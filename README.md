# The-Vigenere-Cipher-Decryption
## Vigenère Cipher Decryption Using Frequency Analysis

This script decrypts a Vigenère cipher using frequency analysis. It includes functions to estimate the key length, perform frequency analysis, and decrypt the ciphertext.

### Features

- **Kasiski Examination**: Estimates the length of the Vigenère key.
- **Frequency Analysis**: Analyzes letter frequencies to determine the most likely key.
- **Decryption**: Uses the derived key to decrypt the ciphertext.

### How It Works

1. **Calculate Index of Coincidence (IC)**: 
    - The calculate_ic function computes the IC for a given text segment to help identify the key length.
2. **Kasiski Examination**:
    - The `kasiski_examination` function calculates the IC for various assumed key lengths to identify the most probable key lengths.
3. **Frequency Analysis**:
    - The `frequency_analysis` function analyzes the frequency of each letter in segments of the ciphertext to determine the most likely shift for each segment.
4. **Decrypt Vigenère Cipher**:
    - The `decrypt_vigenere` function uses the derived key to decrypt the entire ciphertext.

### Usage

1. **Set the Ciphertext**: Replace the `ciphertext` variable with your Vigenère encrypted message.

2. **Estimate Key Length**:
    - The script uses Kasiski examination to estimate the key length and prints the top 5 key length estimates.

3. **Decrypt the Ciphertext**:
    - The script performs frequency analysis for each estimated key length, derives the key, and decrypts the ciphertext.

