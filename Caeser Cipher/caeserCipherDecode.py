def reverse_symbol_mapping(text):
    """Step 1: Reverse symbol mapping back to original punctuation"""
    mapped = []
    for ch in text:
        if ch == ".":
            mapped.append(" ")
        elif ch == " ":
            mapped.append(".")
        elif ch == "!":
            mapped.append("?")
        elif ch == "?":
            mapped.append("!")
        elif ch == "%":
            mapped.append('"')
        elif ch == "^":
            mapped.append(",")
        elif ch == "&":
            mapped.append(";")
        elif ch == "~":
            mapped.append(":")
        else:
            mapped.append(ch)
    return ''.join(mapped)

def reverse_mirror_letters(text):
    """Step 2: Reverse letter mirroring (z↔a, y↔b, etc.)"""
    result = []
    for ch in text:
        if ch == '_':
            result.append(ch)
        elif ch.isalpha():
            if ch.islower():
                # Reverse mirror: z(25) ↔ a(0), y(24) ↔ b(1), etc.
                original = chr(ord('z') - (ord(ch) - ord('a')))
                result.append(original)
            else:
                # This shouldn't happen in our case
                original = chr(ord('Z') - (ord(ch) - ord('A')))
                result.append(original)
        else:
            result.append(ch)
    return ''.join(result)

def reverse_text_reversal(text):
    """Step 3: Reverse the string back to original order"""
    return text[::-1]

def reverse_number_rotation(text):
    """Step 4: Reverse ROT5 on numbers (subtract 5)"""
    result = []
    for ch in text:
        if ch.isdigit():
            # Reverse ROT5: subtract 5 instead of adding 5
            original = str((int(ch) - 5) % 10)
            result.append(original)
        else:
            result.append(ch)
    return ''.join(result)

def reverse_alternating_caesar_shift(text):
    """Step 5: Reverse alternating Caesar shift and restore uppercase"""
    result = []
    letter_position = 0
    i = 0
    
    while i < len(text):
        ch = text[i]
        
        if ch == '_' and i + 1 < len(text) and text[i + 1].isalpha():
            # This is an uppercase letter (now lowercase with _)
            next_ch = text[i + 1]
            
            # Determine the shift that was used (same pattern as encoder)
            current_shift = 7 if letter_position % 2 == 0 else 3
            letter_position += 1
            
            # Reverse the shift and convert back to uppercase
            base = ord('a')
            original = chr((ord(next_ch) - base - current_shift) % 26 + ord('A'))
            result.append(original)
            i += 2  # Skip the next character as we processed it
        elif ch.isalpha() and ch.islower():
            # Regular lowercase letter
            current_shift = 7 if letter_position % 2 == 0 else 3
            letter_position += 1
            
            base = ord('a')
            original = chr((ord(ch) - base - current_shift) % 26 + base)
            result.append(original)
            i += 1
        else:
            result.append(ch)
            i += 1
    
    return ''.join(result)

# Comment the steps if  see just the result

def decode_message(cipher_text):
    """Reverse all 5 encoding steps in opposite order"""
    print(f"Cipher:    \"{cipher_text}\"")
    
    # Step 1: Reverse Symbol Mapping
    step1 = reverse_symbol_mapping(cipher_text)
    print(f"Step 1:    \"{step1}\"  (symbols reversed)")
    
    # Step 2: Reverse Letter Mirroring
    step2 = reverse_mirror_letters(step1)
    print(f"Step 2:    \"{step2}\"  (letters unmirrored)")
    
    # Step 3: Reverse Text Reversal
    step3 = reverse_text_reversal(step2)
    print(f"Step 3:    \"{step3}\"  (text unreversed)")
    
    # Step 4: Reverse Number Rotation
    step4 = reverse_number_rotation(step3)
    print(f"Step 4:    \"{step4}\"  (numbers unrotated)")
    
    # Step 5: Reverse Caesar Shift
    step5 = reverse_alternating_caesar_shift(step4)
    print(f"Original:  \"{step5}\"  (shifts reversed + uppercase restored)")
    
    return step5

def run_tests():
    """Built-in test cases with round-trip verification"""
    print("=" * 50)
    print("RUNNING BUILT-IN TEST CASES")
    print("=" * 50)
    
    # Test cases from README
    test_cases = [
        ("Hello World!", "?shvdvW vh.qsl_"),
        ("ABC123", "876_v_t"),
        ('Say "Hello, friend!"', '?kwzvmy^.sojj vh%._yx')
    ]
    
    for i, (original, expected_cipher) in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print("-" * 30)
        print(f"Expected: {expected_cipher}")
        decoded = decode_message(expected_cipher)
        
        # Verify round-trip
        if decoded == original:
            print("PASS: Perfect round-trip decryption!")
        else:
            print("FAIL: Decryption mismatch!")
            print(f"Expected: {original}")
            print(f"Got:      {decoded}")
        print()

# Main Program
if __name__ == "__main__":
    print("Enhanced Caesar Cipher - Decoder")
    print("=" * 40)
    
    # Ask user if they want to run tests
    choice = input("Run built-in tests? (y/n): ").lower().strip()
    if choice == 'y':
        run_tests()
        print("\n" + "=" * 50)
    
    # Get user input
    cipher_input = input("Enter cipher text to decode: ")
    decoded = decode_message(cipher_input)
    print(f"\nDecoded message: {decoded}")