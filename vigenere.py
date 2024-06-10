from collections import Counter
import numpy as np

# Given Vigenère ciphertext
ciphertext = 'DAZFISFSPAVQLSNPXYSZWXALCDAFGQUISMTPHZGAMKTTFTCCFXKFCRGGLPFETZMMMZOZDEADWVZWMWKVGQSOHQSVHPWFKLSLEASEPWHMJEGKPURVSXJXVBWVPOSDETEQTXOBZIKWCXLWNUOVJMJCLLOEOFAZENVMJILOWZEKAZEJAQDILSWWESGUGKTZGQZVRMNWTQSEOTKTKPBSTAMQVERMJEGLJQRTLGFJYGSPTZPGTACMOECBXSESCIYGUFPKVILLTWDKSZODFWFWEAAPQTFSTQIRGMPMELRYELHQSVWBAWMOSDELHMUZGPGYEKZUKWTAMZJMLSEVJQTGLAWVOVVXHKWQILIEUYSZWXAHHUSZOGMUZQCIMVZUVWIFJJHPWVXFSETZED'
#ciphertext = 'RIJVSFYVYRSUKVCISSISSORABCNDIBDLGCQCCWYQIQEGAOWQPYJVC'

def calculate_ic(text):
    # Calculate the frequency of each letter in the text
    frequency = Counter(text)
    n = len(text)
    ic = sum(f * (f - 1) for f in frequency.values()) / (n * (n - 1))
    return ic

def kasiski_examination(text):
    # Calculate the IC for assumed key lengths from 1 to 20
    ics = []
    for key_len in range(1, 20):
        ic_sum = 0
        for i in range(key_len):
            subtext = text[i::key_len]
            ic_sum += calculate_ic(subtext)
        ics.append(ic_sum / key_len)
    return ics

# Estimate the key length using Kasiski examination
ics = kasiski_examination(ciphertext)
key_length_estimates = np.argsort(ics)[::-1] + 1  # Sort estimates by IC in descending order

print(key_length_estimates[:5])  # Show the top 5 estimates for key length


from string import ascii_uppercase

def frequency_analysis(segment):
    # English letter frequency (approximate)
    english_freq = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002,
                    0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091,
                    0.028, 0.010, 0.023, 0.001, 0.020, 0.001]
    n = len(segment)
    segment_freq = Counter(segment)
    
    # Calculate Chi-squared statistic for each possible shift
    chi_squared = []
    for shift in range(26):
        chi2 = 0
        for i in range(26):
            expected_count = n * english_freq[i]
            actual_count = segment_freq[ascii_uppercase[(i + shift) % 26]]
            chi2 += (actual_count - expected_count) ** 2 / expected_count
        chi_squared.append(chi2)
    
    # Return the shift with the minimum Chi-squared statistic
    return np.argmin(chi_squared)

def decrypt_vigenere(ciphertext, key):
    key_length = len(key)
    plaintext = []
    for i, char in enumerate(ciphertext):
        shift = ascii_uppercase.index(key[i % key_length])
        decrypted_char = ascii_uppercase[(ascii_uppercase.index(char) - shift) % 26]
        plaintext.append(decrypted_char)
    return ''.join(plaintext)

# Divide the ciphertext into segments based on the estimated key length
for i in range(5):
    key_length = key_length_estimates[i]
    segments = ['' for _ in range(key_length)]
    for i, char in enumerate(ciphertext):
        segments[i % key_length] += char

    # Perform frequency analysis on each segment to find the key
    key = ''.join(ascii_uppercase[frequency_analysis(segment)] for segment in segments)

    # Decrypt the ciphertext using the derived key
    plaintext = decrypt_vigenere(ciphertext, key)

    print(key,'\n', plaintext)
