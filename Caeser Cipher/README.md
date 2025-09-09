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
- Verbose mode to show step-by-step transformations.

Note: The cipher is for educational or fun purposes and not cryptographically secure.

## Encoding Process

The encoding process applies five steps in sequence to transform the input text. Each step processes only specific characters (e.g., letters, digits, symbols), leaving others intact. The steps are demonstrated with print statements during execution for transparency.

### Step 1: Alternating Caesar Shift (on Letters Only)
- Processes alphabetic characters only.
- Tracks the position of letters (ignoring non-letters).
- Applies a shift of +7 for even positions (0-based) and +3 for odd positions.
- **Uppercase letters** are converted to lowercase, shifted, and prepended with an `@` symbol to mark them for restoration during decoding.
- Lowercase letters are shifted and remain lowercase.
- Wraps around the alphabet using modulo 26.
- Example: 'A' (position 0) → shifted by +7 to 'h', becomes `@h`.

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
- The `@` symbols and non-letters pass through unchanged.
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
  - `'` ↔ `#` (apostrophe mapping)
  - `&` ↔ `;` (ampersand mapping)
- Other characters remain unchanged.
- This is also self-inverse.

The final output is the result after all steps.

## Decoding Process

Decoding reverses the encoding steps in the opposite order, applying inverse operations. Like encoding, it prints each step for visibility when verbose mode is enabled.

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
- For marked uppercase (`@` followed by a lowercase letter): Removes `@`, reverses the shift (-7 or -3 based on position), and converts to uppercase.
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
5. Then: "Show steps? (y/n):"
   - Enter `y` to see detailed step-by-step transformations.
   - Enter `n` for output only.
6. Finally: "Enter a sentence to encode:"
   - Input your text (e.g., "My name is Okasha Nadeem & I'm 19 yo.").
7. The script prints each encoding step (if verbose) and the final cipher.

### Running the Decoder (`caeserCipherDecode.py`)
1. Run: `python caeserCipherDecode.py`
2. Prompt: "Run built-in tests? (y/n):"
   - `y` runs tests with round-trip verification (automatically encodes test cases first, then decodes them).
   - The tests now dynamically generate correct cipher text for accurate verification.
3. Then: "Show steps? (y/n):"
   - `y` shows detailed step-by-step reverse transformations.
   - `n` shows only the final result.
4. Finally: "Enter cipher text to decode:"
   - Input the cipher (e.g., "iu.46.k#k@.&.kospwf@.wlesme@.ek.sgwf.yg@").
5. The script prints each decoding step (if verbose) and the original text.

### Testing Round-Trip
- Encode a message, copy the cipher, then decode it—it should match the original exactly.
- Use the built-in tests for quick verification.

## Test Cases

Here are the built-in test cases that work with the current implementation:

### Example 1:
- **Original:** "Hello World!"
- **Encoded:** (dynamically generated by encoder)
- **Decoded:** "Hello World!" ✅

### Example 2:
- **Original:** "ABC123"
- **Encoded:** (dynamically generated by encoder)
- **Decoded:** "ABC123" ✅

### Example 3:
- **Original:** 'Say "Hello, friend!"'
- **Encoded:** (dynamically generated by encoder)
- **Decoded:** 'Say "Hello, friend!"' ✅

### Real-World Example:
- **Original:** "My name is Okasha Nadeem & I'm 19 yo."
- **Encoded:** "iu.46.k#k@.&.kospwf@.wlesme@.ek.sgwf.yg@"
- **Decoded:** "My name is Okasha Nadeem & I'm 19 yo." ✅

## Key Improvements Made

### Fixed Issues:
1. **Uppercase Escape Character Conflict**: Changed from `^` to `@` to avoid conflict with comma mapping.
2. **Symbol Mapping Completeness**: Added mappings for apostrophes (`'` ↔ `#`) and ampersands (`&` ↔ `;`).
3. **Bidirectional Consistency**: Ensured all symbol mappings are perfectly reversible.
4. **Dynamic Test Cases**: Decoder tests now generate cipher text using the encoder for accurate verification.

### Enhanced Features:
- **Verbose Mode**: Optional step-by-step display during encoding/decoding.
- **Comprehensive Symbol Support**: Handles common punctuation marks including apostrophes and ampersands.
- **Robust Testing**: Built-in tests verify round-trip accuracy automatically.
- **Error Prevention**: Eliminated character conflicts that caused decoding errors.

## Supported Characters

### Letters:
- Uppercase (A-Z): Converted to lowercase, shifted, and marked with `@`
- Lowercase (a-z): Shifted and remain lowercase

### Numbers:
- Digits (0-9): ROT5 transformation

### Symbols (with mapping):
- Space ` ` ↔ `.`
- Period `.` ↔ Space ` `
- Question mark `?` ↔ `!`
- Exclamation `!` ↔ `?`
- Quote `"` ↔ `%`
- Comma `,` ↔ `^`
- Semicolon `;` ↔ `&`
- Colon `:` ↔ `~`
- Apostrophe `'` ↔ `#`
- Ampersand `&` ↔ `;`

### Other Characters:
- Pass through unchanged (parentheses, brackets, mathematical symbols, etc.)

## Technical Details

### Alternating Caesar Shifts:
- Even letter positions (0, 2, 4, ...): +7 shift
- Odd letter positions (1, 3, 5, ...): +3 shift
- Position counting ignores non-alphabetic characters

### ROT5 for Numbers:
- Simple Caesar cipher for digits: (digit + 5) % 10

### Atbash Mirroring:
- Maps each letter to its mirror position: a→z, b→y, etc.
- Self-inverse operation

## Known Limitations

- **Non-ASCII Characters**: May not handle Unicode characters properly—stick to standard ASCII.
- **Security**: This is an educational cipher, not suitable for real cryptographic applications.
- **Case Sensitivity**: Relies on `@` markers for uppercase restoration.

## Troubleshooting

### Common Issues:
1. **Encoding/Decoding Mismatch**: Ensure you're using the same version of both scripts.
2. **Missing Characters**: Check that all symbols in your input are supported or pass through unchanged.
3. **Extra Spaces**: Input and output should match exactly—check for trailing spaces.

### Verification Steps:
1. Run built-in tests first to ensure scripts work correctly.
2. Try simple inputs like "Hello" before complex sentences.
3. Use verbose mode to see where transformations might be going wrong.

## Contributing

Feel free to fork and improve! Suggested enhancements:
- File I/O support for batch processing
- Command-line arguments for automation
- Additional symbol mappings
- GUI interface
- Support for Unicode characters

For questions or suggestions, visit my [portfolio](https://okashadev.vercel.app).

## License

This project is open source and available for educational purposes. Feel free to use, modify, and distribute.