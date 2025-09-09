# --- Step 1: Alternating Caesar Shift ---
def alternating_caesar_shift(text):
    """Apply alternating Caesar shift (+7 / +3) to letters only.
       Uppercase letters are escaped with '@' before the shifted letter."""
    result = []
    letter_position = 0

    for ch in text:
        if ch.isalpha():
            shift = 7 if letter_position % 2 == 0 else 3
            letter_position += 1

            if ch.isupper():
                base = ord('A')
                shifted = chr((ord(ch) - base + shift) % 26 + ord('a'))  # store lowercase
                result.append("@" + shifted)  # escape uppercase with @
            else:
                base = ord('a')
                shifted = chr((ord(ch) - base + shift) % 26 + base)
                result.append(shifted)
        else:
            result.append(ch)
    return ''.join(result)


# --- Step 2: ROT5 for numbers ---
def rotate_numbers(text):
    """Apply ROT5 to digits."""
    return ''.join(str((int(ch) + 5) % 10) if ch.isdigit() else ch for ch in text)


# --- Step 3: Reverse text ---
def reverse_text(text):
    return text[::-1]


# --- Step 4: Mirror letters ---
def mirror_letters(text):
    """Mirror all letters in the alphabet (a↔z, b↔y, etc.)."""
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


# --- Step 5: Symbol mapping ---
SYMBOL_MAP = {
    " ": ".", ".": " ",
    "?": "!", "!": "?",
    '"': "%", ",": "^",
    ";": "&", ":": "~",
    "'": "#",  # Added mapping for apostrophe
    "&": ";"   # Added mapping for ampersand
}

def map_symbols(text):
    return ''.join(SYMBOL_MAP.get(ch, ch) for ch in text)


# --- Encoding Pipeline ---
ENCODING_STEPS = [
    alternating_caesar_shift,
    rotate_numbers,
    reverse_text,
    mirror_letters,
    map_symbols
]


# --- Encoder ---
def encode_message(text, verbose=True):
    if verbose: 
        print(f'Original: "{text}"')
    for i, func in enumerate(ENCODING_STEPS, 1):
        text = func(text)
        if verbose: 
            print(f"Step {i}: \"{text}\" ({func.__name__})")
    return text


# --- Test Runner ---
def run_tests():
    print("=" * 50)
    print("RUNNING BUILT-IN TEST CASES")
    print("=" * 50)

    test_cases = [
        "Hello World!",
        "ABC123",
        'Say "Hello, friend!"'
    ]

    for i, test in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print("-" * 20)
        encoded = encode_message(test, verbose=True)
        print(f"Final Cipher: \"{encoded}\"")
        print()


# --- Main ---
if __name__ == "__main__":
    print("Caesar Cipher Encoder By Okasha Nadeem")
    print("=" * 40)

    choice = input("Run built-in tests? (y/n): ").lower().strip()
    if choice == 'y':
        run_tests()
        print("\n" + "=" * 50)

    verbose = input("Show steps? (y/n): ").lower().strip() == 'y'
    sentence = input("Enter a sentence to encode: ")

    result = encode_message(sentence, verbose)
    print(f"\nCipher output: {result}")