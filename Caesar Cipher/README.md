# 🔐 Enhanced Caesar Cipher Tool

## 📋 Overview

This project implements a sophisticated multi-layer Caesar cipher with an intuitive web-based user interface built using Streamlit. The system combines five sequential transformation algorithms to create a robust encoding/decoding mechanism that handles letters, numbers, and symbols with advanced features like case preservation and comprehensive symbol mapping.

### 🏗️ Project Structure

The project consists of three main components:

- **`caeserCipherEncode.py`**: Core encoding engine with five sequential transformation steps
- **`caeserCipherDecode.py`**: Core decoding engine that reverses transformations in opposite order
- **`streamlit_app.py`**: Modern Streamlit web application with interactive UI and operation history
- **`README.md`**: Comprehensive documentation (this file)

### ✨ Key Features

- **🎯 Multi-Layer Encryption**: Five sequential transformation steps for enhanced complexity
- **🔄 Perfect Reversibility**: Every operation is mathematically reversible
- **📱 Modern Web Interface**: Responsive Streamlit UI with professional styling
- **📊 Operation History**: Comprehensive chat-like history with timestamps and statistics
- **🔤 Case Preservation**: Sophisticated uppercase letter handling with escape markers
- **🔢 Number Transformation**: ROT5 cipher for digits
- **🔣 Symbol Mapping**: Bidirectional mapping for common punctuation
- **🧪 Built-in Testing**: Comprehensive test cases for verification
- **📥 Export Functionality**: Download results as text files
- **🎨 Professional Design**: Modern UI with color-coded operations and animations

## 🚀 Getting Started

### Prerequisites

```bash
# Required Python version
Python 3.7+

# Required packages
streamlit>=1.28.0
datetime (built-in)
```

### 🔧 Installation

1. **Clone or Download** the project files:
   ```bash
   git clone https://github.com/Okashanadeem/LearnByFun.git
   cd LearnByFun/Caeser/Caesar Cipher
   ```

2. **Install Dependencies**:
   ```bash
   pip install streamlit
   ```

3. **Verify File Structure**:
   ```
   caesar-cipher-tool/
   ├── streamlit_app.py
   ├── caeserCipherEncode.py
   ├── caeserCipherDecode.py
   └── README.md
   ```

### 🖥️ Running the Application

#### Web Interface (Recommended)
```bash
streamlit run app.py
```
The application will open in your default browser at `http://localhost:8501`

#### Command Line Interface
```bash
# For encoding
python caeserCipherEncode.py

# For decoding  
python caeserCipherDecode.py
```
### Live Demo
A live demo of the web interface is available at: [Caesar Cipher Tool By Okasha Nadeem](https://caesar-cipher-okasha-nadeem.streamlit.app)

## 🌐 Web Interface Guide

### 🎨 Main Interface Features

#### **🏠 Dashboard Layout**
- **Wide Layout**: Optimized for desktop and tablet viewing
- **Responsive Design**: Adapts to different screen sizes
- **Professional Styling**: Modern color scheme with custom CSS
- **Intuitive Navigation**: Clean, user-friendly interface

#### **🔄 Operation Modes**
- **🔒 Encode Mode**: Transform plain text into cipher text
- **🔓 Decode Mode**: Convert cipher text back to original message
- **Radio Button Selection**: Easy switching between modes

#### **📝 Input/Output Areas**
- **Large Text Areas**: Comfortable typing and pasting space
- **Smart Placeholders**: Context-aware placeholder text
- **Character Counter**: Real-time text length feedback
- **Syntax Highlighting**: Code-style display for cipher text

#### **⚡ Processing Controls**
- **Dynamic Buttons**: Context-aware button text and icons
- **One-Click Processing**: Instant encoding/decoding
- **Error Handling**: User-friendly error messages and warnings
- **Input Validation**: Automatic empty input detection

#### **📊 Results Display**
- **Color-Coded Results**: Green containers for successful operations
- **Formatted Output**: Monospace font for cipher text clarity
- **Copy-Friendly Format**: Easy selection and copying
- **Download Integration**: Direct file download functionality

### 📜 Chat History Sidebar

#### **🗂️ History Management**
- **Persistent Storage**: Operations saved during session
- **Chronological Order**: Newest operations appear first
- **Operation Limit**: Automatically maintains last 20 operations
- **Clear Function**: One-click history reset

#### **📋 Entry Details**
- **Timestamp Display**: Precise time (HH:MM:SS) for each operation
- **Mode Indicators**: Visual icons (🔒 for encode, 🔓 for decode)
- **Color Coding**: Yellow backgrounds for encode, blue for decode
- **Border Styling**: Left-border color matching for quick identification

#### **🔍 Text Management**
- **Smart Previews**: First 100 characters shown by default
- **Expandable Content**: "Full Input/Output" buttons for complete text
- **Scrollable Container**: Smooth scrolling for long histories
- **Text Wrapping**: Proper display of long cipher texts

#### **📈 Statistics Panel**
- **Total Operations**: Real-time count of all operations
- **Operation Breakdown**: Separate counters for encodings and decodings
- **Live Updates**: Statistics update automatically with each operation
- **Visual Metrics**: Clean metric display with icons

### 🎯 Advanced UI Features

#### **📱 Responsive Design**
- **Desktop Optimized**: Full-width layout with sidebar
- **Tablet Friendly**: Adaptive column layouts
- **Mobile Compatible**: Stack-friendly responsive design
- **Cross-Browser**: Tested on Chrome, Firefox, Safari, Edge

#### **🎨 Visual Enhancements**
- **Custom CSS Styling**: Professional color schemes and typography
- **Hover Effects**: Interactive button states
- **Loading States**: Smooth processing feedback
- **Animation Transitions**: Subtle UI animations for better UX

#### **♿ Accessibility Features**
- **High Contrast**: Readable color combinations
- **Semantic Markup**: Proper HTML structure
- **Keyboard Navigation**: Full keyboard accessibility
- **Screen Reader Friendly**: Proper ARIA labels and descriptions

## 🔧 Cipher Algorithm Documentation

### 🔄 Encoding Process (5 Sequential Steps)

#### **Step 1: Alternating Caesar Shift** 
*Target: Alphabetic characters only*

```python
# Algorithm Logic
letter_position = 0  # Only count actual letters
for each alphabetic character:
    if position is even: shift = +7
    if position is odd:  shift = +3
    if uppercase: convert to lowercase, shift, add '@' prefix
    if lowercase: shift normally
    wrap around using modulo 26
```

**Examples:**
- `'A'` (pos 0) → shift +7 → `'h'` → `'@h'` (marked as original uppercase)
- `'b'` (pos 1) → shift +3 → `'e'`
- `'Hello'` → `'@oixzs'` (H marked, e+7=l, l+3=o, l+7=s, o+3=r)

#### **Step 2: ROT5 Number Rotation**
*Target: Numeric digits only*

```python
# ROT5 Algorithm
for each digit (0-9):
    new_digit = (old_digit + 5) % 10
```

**Transformation Table:**
```
0→5, 1→6, 2→7, 3→8, 4→9
5→0, 6→1, 7→2, 8→3, 9→4
```

#### **Step 3: Text Reversal**
*Target: Entire string*

```python
# Complete string reversal
result = input_string[::-1]
```

**Example:** `"@hello123"` → `"321olleh@"`

#### **Step 4: Atbash Letter Mirroring**
*Target: Alphabetic characters only*

```python
# Atbash cipher algorithm
for each letter:
    if lowercase: new_char = chr(ord('z') - (ord(char) - ord('a')))
    # @ symbols pass through unchanged
```

**Mirror Mapping:**
```
a↔z, b↔y, c↔x, d↔w, e↔v, f↔u, g↔t, h↔s, i↔r, j↔q
k↔p, l↔o, m↔n, n↔m, o↔l, p↔k, q↔j, r↔i, s↔h, t↔g
u↔f, v↔e, w↔d, x↔c, y↔b, z↔a
```

#### **Step 5: Symbol Mapping**
*Target: Specific punctuation marks*

```python
# Bidirectional symbol substitution
symbol_map = {
    ' ': '.', '.': ' ',    # Space and period swap
    '?': '!', '!': '?',    # Question and exclamation swap  
    '"': '%',              # Quote to percent
    ',': '^',              # Comma to caret
    ';': '&',              # Semicolon to ampersand
    ':': '~',              # Colon to tilde
    "'": '#',              # Apostrophe to hash
    '&': ';',              # Ampersand to semicolon
}
```

### 🔄 Decoding Process (Reverse Order)

The decoding process applies the inverse of each step in **reverse order**:

1. **Reverse Symbol Mapping** → Step 5 inverse
2. **Reverse Atbash Mirroring** → Step 4 inverse (self-inverse)
3. **Reverse Text Reversal** → Step 3 inverse (self-inverse) 
4. **Reverse ROT5** → Step 2 inverse (subtract 5)
5. **Reverse Caesar Shift** → Step 1 inverse (process @ markers)

## 🧪 Testing & Verification

### 🔬 Built-in Test Cases

The system includes comprehensive test cases that verify round-trip accuracy:

#### **Test Case 1: Basic Text**
```
Original: "Hello World!"
Encoded:  (dynamically generated)
Decoded:  "Hello World!" ✅
```

#### **Test Case 2: Mixed Case & Numbers**
```
Original: "ABC123"
Encoded:  (dynamically generated) 
Decoded:  "ABC123" ✅
```

#### **Test Case 3: Complex Punctuation**
```
Original: 'Say "Hello, friend!"'
Encoded:  (dynamically generated)
Decoded:  'Say "Hello, friend!"' ✅
```

#### **Test Case 4: Real-World Example**
```
Original: "My name is Okasha Nadeem & I'm 19 yo."
Encoded:  "iu.46.k#k@.&.kospwf@.wlesme@.ek.sgwf.yg@"
Decoded:  "My name is Okasha Nadeem & I'm 19 yo." ✅
```

### 🧪 Running Tests

#### **Web Interface Testing**
1. Click any operation mode (Encode/Decode)
2. Expand "ℹ️ About Advanced Cipher"
3. Use provided test cases to verify functionality
4. Check operation history for test results

#### **Command Line Testing**
```bash
python caeserCipherEncode.py
# Choose 'y' for built-in tests
# Choose 'y' for verbose step-by-step display

python caeserCipherDecode.py  
# Choose 'y' for built-in tests with round-trip verification
# Choose 'y' to see decoding steps
```

## 📋 Character Support Matrix

### ✅ Fully Supported Characters

| Category | Characters | Transformation |
|----------|------------|----------------|
| **Uppercase Letters** | A-Z | Caesar shift → lowercase + @ marker |
| **Lowercase Letters** | a-z | Caesar shift (alternating +7/+3) |
| **Digits** | 0-9 | ROT5 transformation |
| **Mapped Symbols** | ` . ? ! " , ; : ' &` | Bidirectional symbol mapping |

### 🔄 Symbol Transformation Table

| Original | Encoded | Operation |
|----------|---------|-----------|
| Space ` ` | `.` | Swap |
| Period `.` | Space ` ` | Swap |
| Question `?` | `!` | Swap |
| Exclamation `!` | `?` | Swap |
| Quote `"` | `%` | Map |
| Comma `,` | `^` | Map |
| Semicolon `;` | `&` | Map |
| Colon `:` | `~` | Map |
| Apostrophe `'` | `#` | Map |
| Ampersand `&` | `;` | Map |

### ⚡ Pass-Through Characters

Characters not in the above categories pass through unchanged:
- Parentheses: `( )`
- Brackets: `[ ] { }`
- Mathematical: `+ - * / = < >`
- Other punctuation: `@ # $ % ^ ~ _`
- Unicode and special characters


### 🧪 Debugging Steps

1. **Verify Installation**:
   ```bash
   python --version  # Should be 3.7+
   streamlit --version  # Should be 1.28.0+
   ```

2. **Test Core Functions**:
   ```bash
   python caeserCipherEncode.py  # Run built-in tests
   python caeserCipherDecode.py  # Run built-in tests
   ```


3. **Validate Input Characters**:
   - Use only ASCII characters for best results
   - Check for hidden Unicode characters
   - Verify no trailing newlines or spaces

## 🔒 Security Considerations

### ⚠️ Important Disclaimers

- **Educational Purpose Only**: This cipher is designed for learning and entertainment
- **Not Cryptographically Secure**: Should never be used for actual sensitive data
- **Predictable Patterns**: The alternating shifts create detectable patterns
- **Symbol Mapping**: Limited symbol set makes frequency analysis possible
- **No Key Management**: No secret key system implemented

### 🛡️ Recommended Use Cases

✅ **Appropriate Uses:**
- Educational cryptography demonstrations
- Fun puzzles and games  
- Basic text obfuscation for casual purposes
- Learning about multi-layer transformations
- Programming exercise and algorithm study

❌ **Inappropriate Uses:**
- Protecting sensitive personal information
- Business or financial data encryption
- Password or authentication systems
- Legal document protection
- Any security-critical applications


## 🤝 Contributing

### 🛠️ Development Setup

1. **Fork the Repository**
2. **Create Development Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Install Development Dependencies**:
   ```bash
   pip install streamlit pytest black flake8
   ```
4. **Make Changes and Test**
5. **Submit Pull Request**


### 👨‍💻 Author
**Okasha Nadeem**
- Portfolio: [okashadev.vercel.app](https://okashadev.vercel.app)
- GitHub: [Okasha Nadeem](https://github.com/Okashanadeem/)
- Email: [Mail me](mailto:okasha.code@gmail.com)