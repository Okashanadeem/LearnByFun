# --- Step 1: Reverse Symbol Mapping ---
def unmap_symbols(text):
    REVERSE_SYMBOL_MAP = {
        ".": " ", " ": ".",
        "!": "?", "?": "!",
        "%": '"', "^": ",",
        "&": ";", "~": ":",
        "#": "'",  # Added reverse mapping for apostrophe
        ";": "&"   # Added reverse mapping for ampersand
    }
    return ''.join(REVERSE_SYMBOL_MAP.get(ch, ch) for ch in text)


# --- Step 2: Reverse Letter Mirroring ---
def mirror_letters(text):
    result = []
    for ch in text:
        if ch.isalpha():
            if ch.islower():
                result.append(chr(ord('z') - (ord(ch) - ord('a'))))
            else:
                result.append(chr(ord('Z') - (ord(ch) - ord('A'))))
        else:
            result.append(ch)
    return ''.join(result)


# --- Step 3: Reverse Text Reversal ---
def reverse_text(text):
    return text[::-1]


# --- Step 4: Reverse ROT5 for numbers ---
def unrotate_numbers(text):
    return ''.join(str((int(ch) - 5) % 10) if ch.isdigit() else ch for ch in text)


# --- Step 5: Reverse Alternating Caesar Shift ---
def alternating_caesar_unshift(text):
    result = []
    letter_position = 0
    i = 0
    while i < len(text):
        if text[i] == "@":  # uppercase escape (changed from ^ to @)
            i += 1
            if i < len(text):
                ch = text[i]
                shift = 7 if letter_position % 2 == 0 else 3
                letter_position += 1
                base = ord('a')
                unshifted = chr((ord(ch) - base - shift) % 26 + base)
                result.append(unshifted.upper())
        elif text[i].isalpha():
            shift = 7 if letter_position % 2 == 0 else 3
            letter_position += 1
            base = ord('a')
            unshifted = chr((ord(text[i]) - base - shift) % 26 + base)
            result.append(unshifted)
        else:
            result.append(text[i])
        i += 1
    return ''.join(result)


# --- Decoding Pipeline ---
DECODING_STEPS = [
    unmap_symbols,
    mirror_letters,
    reverse_text,
    unrotate_numbers,
    alternating_caesar_unshift
]


# --- Decoder ---
def decode_message(text, verbose=True):
    if verbose: 
        print(f'Cipher: "{text}"')
    for i, func in enumerate(DECODING_STEPS, 1):
        text = func(text)
        if verbose: 
            print(f"Step {i}: \"{text}\" ({func.__name__})")
    return text


# --- Test Runner ---
def run_tests():
    print("=" * 50)
    print("RUNNING BUILT-IN TEST CASES")
    print("=" * 50)

    # First encode some test cases to get the correct cipher text
    from caesarCipherEncode import encode_message as encode_test
    
    test_cases = [
        "Hello World!",
        "ABC123",
        'Say "Hello, friend!"'
    ]

    for i, test in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: '{test}'")
        print("-" * 30)
        # Encode first to get correct cipher
        cipher = encode_test(test, verbose=False)
        print(f"Cipher: '{cipher}'")
        
        # Then decode
        decoded = decode_message(cipher, verbose=True)
        print(f"Decoded back: \"{decoded}\"")
        if decoded == test:
            print("✅ PASS")
        else:
            print("❌ FAIL")
        print()


# --- Main ---
if __name__ == "__main__":
    print("Caesar Cipher Decoder By Okasha Nadeem")
    print("=" * 40)

    choice = input("Run built-in tests? (y/n): ").lower().strip()
    if choice == 'y':
        run_tests()
        print("\n" + "=" * 50)

    verbose = input("Show steps? (y/n): ").lower().strip() == 'y'
    cipher_input = input("Enter cipher text to decode: ")

    result = decode_message(cipher_input, verbose)
    print(f"\nDecoded message: {result}")