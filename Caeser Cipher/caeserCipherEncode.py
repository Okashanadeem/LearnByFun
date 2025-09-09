def alternating_caesar_shift(text):
    """Step 1: Apply alternating Caesar shift (+7/+3) to letters only"""
    result = []
    letter_position = 0
    
    for ch in text:
        if ch.isalpha():
            # Alternate between +7 and +3 shifts based on letter position
            current_shift = 7 if letter_position % 2 == 0 else 3
            letter_position += 1
            
            if ch.isupper():  # Uppercase: prepend "_"
                base = ord('A')
                shifted = chr((ord(ch) - base + current_shift) % 26 + ord('a'))  # make lowercase
                result.append("_" + shifted)
            else:  # lowercase
                base = ord('a')
                shifted = chr((ord(ch) - base + current_shift) % 26 + base)
                result.append(shifted)
        else:
            result.append(ch)
    return ''.join(result)

def rotate_numbers(text):
    """Step 2: Apply ROT5 to all digits (0→5, 1→6, ..., 5→0, 6→1, ...)"""
    result = []
    for ch in text:
        if ch.isdigit():
            # Apply ROT5: add 5 and wrap around
            rotated = str((int(ch) + 5) % 10)
            result.append(rotated)
        else:
            result.append(ch)
    return ''.join(result)

def reverse_text(text):
    """Step 3: Reverse the entire string"""
    return text[::-1]

def mirror_letters(text):
    """Step 4: Mirror all letters in the alphabet (a↔z, b↔y, etc.)"""
    result = []
    for ch in text:
        if ch == '_':
            result.append(ch)
        elif ch.isalpha():
            if ch.islower():
                # Mirror: a(0) ↔ z(25), b(1) ↔ y(24), etc.
                mirrored = chr(ord('z') - (ord(ch) - ord('a')))
                result.append(mirrored)
            else:
                # This shouldn't happen since we convert to lowercase in step 1
                mirrored = chr(ord('Z') - (ord(ch) - ord('A')))
                result.append(mirrored)
        else:
            result.append(ch)
    return ''.join(result)

def map_symbols(text):
    """Step 5: Apply symbol mapping (space↔., ?↔!, etc.)"""
    mapped = []
    for ch in text:
        if ch == " ":
            mapped.append(".")
        elif ch == ".":
            mapped.append(" ")
        elif ch == "?":
            mapped.append("!")
        elif ch == "!":
            mapped.append("?")
        elif ch == '"':
            mapped.append("%")
        elif ch == ",":
            mapped.append("^")
        elif ch == ";":
            mapped.append("&")
        elif ch == ":":
            mapped.append("~")
        else:
            mapped.append(ch)
    return ''.join(mapped)


# Comment the steps if  see just the result

def encode_message(text):
    """Apply all 5 encoding steps in sequence"""
    print(f"Original:  \"{text}\"")
    
    # Step 1: Alternating Caesar Shift
    step1 = alternating_caesar_shift(text)
    print(f"Step 1:    \"{step1}\"  (alternating shifts + uppercase marking)")
    
    # Step 2: Number Rotation (ROT5)
    step2 = rotate_numbers(step1)
    print(f"Step 2:    \"{step2}\"  (numbers rotated)")
    
    # Step 3: Text Reversal
    step3 = reverse_text(step2)
    print(f"Step 3:    \"{step3}\"  (reversed)")
    
    # Step 4: Letter Mirroring
    step4 = mirror_letters(step3)
    print(f"Step 4:    \"{step4}\"  (letters mirrored)")
    
    # Step 5: Symbol Mapping
    step5 = map_symbols(step4)
    print(f"Final:     \"{step5}\"")
    
    return step5

def run_tests():
    """Built-in test cases as mentioned in README"""
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
        encoded = encode_message(test)
        print()

# Main Program
if __name__ == "__main__":
    print("Enhanced Caesar Cipher - Encoder")
    print("=" * 40)
    
    # Ask user if they want to run tests
    choice = input("Run built-in tests? (y/n): ").lower().strip()
    if choice == 'y':
        run_tests()
        print("\n" + "=" * 50)
    
    # Get user input
    sentence = input("Enter a sentence: ")
    cipher = encode_message(sentence)
    print(f"\nCipher output: {cipher}")