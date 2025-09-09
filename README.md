# Enhanced Caesar Cipher README

## Overview

This project implements an enhanced Caesar cipher with multiple transformation steps for encoding and decoding messages. It consists of two Python scripts:

- **`caeserCipherEncode.py`**: Encodes a plain text message into a cipher text by applying five sequential transformations.
- **`caeserCipherDecode.py`**: Decodes a cipher text back to the original plain text by reversing the transformations in the opposite order.

The cipher is designed to handle letters (with case sensitivity via markers), numbers, and specific symbols, while leaving other characters unchanged. It uses Python 3 and requires no external libraries.

Key features:
- Alternating shifts for letters to add complexity.
- Self-inverse operations where possible (e.g., mirroring and reversal).
- Built-in test cases for verification.
- Interactive mode for user input.

Note: The cipher is for educational or fun purposes and not cryptographically secure.

## Encoding Process

The encoding process applies five steps in sequence to transform the input text. Each step processes only specific characters (e.g., letters, digits, symbols), leaving others intact. The steps are demonstrated with print statements during execution for transparency.

### Step 1: Alternating Caesar Shift (on Letters Only)
- Processes alphabetic characters only.
- Tracks the position of letters (ignoring non-letters).
- Applies a shift of +7 for even positions (0-based) and +3 for odd positions.
- Uppercase letters are converted to lowercase, shifted, and prepended with an underscore (`_`) to mark them for restoration during decoding.
- Lowercase letters are shifted and remain lowercase.
- Wraps around the alphabet using modulo 26.
- Example: 'A' (position 0) → shifted by +7 to 'h', becomes `_h`.

### Step 2: Number Rotation (ROT5 on Digits)
- Processes digits (0-9) only.
- Adds 5 to each digit and wraps around modulo 10 (e.g., 0 → 5, 5 → 0, 9 → 4).
- This is a simple substitution for numbers.

### Step 3: Text Reversal
- Reverses the entire string from the previous step.
- Affects all characters, including transformed ones.

### Step 4: Letter Mirroring (Atbash Cipher on Letters)
- Processes alphabetic characters only (now all lowercase due to Step 1).
- Mirrors letters in the alphabet: a ↔ z, b ↔ y, c ↔ x, ..., m ↔ n.
- Formula: For a lowercase letter, new_char = chr(ord('z') - (ord(ch) - ord('a'))).
- Underscores (`_`) and non-letters pass through unchanged.
- This operation is self-inverse (applying it twice returns the original).

### Step 5: Symbol Mapping
- Applies pairwise substitutions to specific symbols:
  - Space (` `) ↔ `.`
  - `.` ↔ Space (` `)
  - `?` ↔ `!`
  - `!` ↔ `?`
  - `"` ↔ `%`
  - `,` ↔ `^`
  - `;` ↔ `&`
  - `:` ↔ `~`
- Other characters remain unchanged.
- This is also self-inverse.

The final output is the result after all steps.

## Decoding Process

Decoding reverses the encoding steps in the opposite order, applying inverse operations. Like encoding, it prints each step for visibility.

### Step 1: Reverse Symbol Mapping
- Reverses the substitutions from Encoding Step 5 (uses the same mapping since it's pairwise).

### Step 2: Reverse Letter Mirroring
- Applies the same mirroring as Encoding Step 4 (self-inverse).

### Step 3: Reverse Text Reversal
- Reverses the string again to restore original order (self-inverse).

### Step 4: Reverse Number Rotation
- Subtracts 5 from each digit and wraps modulo 10 (e.g., 5 → 0, 0 → 5, 4 → 9).

### Step 5: Reverse Alternating Caesar Shift
- Processes the text while tracking letter positions (ignoring non-letters).
- For marked uppercase (`_` followed by a lowercase letter): Removes `_`, reverses the shift (-7 or -3 based on position), and converts to uppercase.
- For lowercase letters: Reverses the shift (-7 or -3 based on position).
- Restores the original case and positions.

The final output is the decoded original text.

## How to Use

### Prerequisites
- Python 3.x installed.
- No additional packages needed.

### Running the Encoder (`caeserCipherEncode.py`)
1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run: `python caeserCipherEncode.py`
4. You'll be prompted: "Run built-in tests? (y/n):"
   - Enter `y` to run tests (shows encoding for sample inputs with step-by-step output).
   - Enter `n` to skip.
5. Then: "Enter a sentence:"
   - Input your text (e.g., "Do you know my name? I am Okasha! ; I'm 19 yo.").
6. The script prints each encoding step and the final cipher.
7. Example output includes the final "Cipher output: ?thfea_.elhsl_"

### Running the Decoder (`caeserCipherDecode.py`)
1. Run: `python caeserCipherDecode.py`
2. Prompt: "Run built-in tests? (y/n):"
   - `y` runs tests with round-trip verification (decodes sample ciphers and checks against originals).
   - Note: The built-in test ciphers in the code may need updating for accuracy (see Known Issues below). Correct expected ciphers are provided in Test Cases section.
3. Then: "Enter cipher text to decode:"
   - Input the cipher (e.g., "?thfea_.elhsl_").
4. The script prints each decoding step and the original text.
5. Example: "Decoded message: Hello World!"

### Testing Round-Trip
- Encode a message, copy the cipher, then decode it—it should match the original.
- Use the built-in tests for quick verification.

## Test Cases

Here are the built-in test cases with correct expected outputs (based on actual runs). If the decoder's test cases don't match these, update the `test_cases` list in `caeserCipherDecode.py` accordingly.

1. Original: "Hello World!"  
   Encoded: "?thfea_.elhsl_"  
   Decoded: "Hello World!" (PASS)

2. Original: "ABC123"  
   Encoded: "876q_v_s_"  
   Decoded: "ABC123" (PASS)

3. Original: 'Say "Hello, friend!"'  
   Encoded: "%?tfskfn.^ihlop_%.uwa_"  
   Decoded: 'Say "Hello, friend!"' (PASS)

## Known Issues and Notes
- The decoder's built-in test cases have incorrect expected ciphers (they don't match the encoder's output). Update them as shown above to fix round-trip tests.
- Non-ASCII characters may not be handled gracefully—stick to English letters, digits, and supported symbols.
- Letter positions for shifts ignore non-letters, ensuring consistent encoding/decoding.
- If you encounter mismatches, check for extra spaces or case issues in input.

## Contributing
Feel free to fork and improve! Suggestions: Add file I/O, more symbols, or CLI arguments.

For questions, visit my [portfolio](https://okashadev.vercel.app).