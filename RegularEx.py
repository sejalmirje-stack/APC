import re

# ==========================================
# 1. Extract Digits
# ==========================================
print("=== 1. Extract Digits ===")
text1 = "User ID: 1042, Code: 987, Age: 25"
digits = re.findall(r"\d+", text1)
print("Input:", text1)
print("Extracted Digits:", digits)

# ==========================================
# 2. Words Beginning with 'A' or 'a'
# ==========================================
print("\n=== 2. Words Beginning with 'A' or 'a' ===")
text2 = "An apple a day keeps any doctor away, Absolutely!"
words_a = re.findall(r"\b[aA]\w*", text2)
print("Input:", text2)
print("Words starting with A/a:", words_a)

# ==========================================
# 3. Count Vowels
# ==========================================
print("\n=== 3. Count Vowels ===")
text3 = "Regular Expressions are Powerful!"
vowels = re.findall(r"[aeiouAEIOU]", text3)
print("Input:", text3)
print("Vowels found:", vowels)
print("Total Vowel Count:", len(vowels))

# ==========================================
# 4. Extract Uppercase Letters
# ==========================================
print("\n=== 4. Extract Uppercase Letters ===")
text4 = "PyThOn ReGeX ExAmPlE"
uppercase_letters = re.findall(r"[A-Z]", text4)
print("Input:", text4)
print("Uppercase Letters:", uppercase_letters)

# ==========================================
# 5. Identify Spaces, Tabs, and Newlines
# ==========================================
print("\n=== 5. Identify Spaces, Tabs, and Newlines ===")
text5 = "Line 1\tTabbed\nLine 2 with spaces"
whitespace_chars = re.findall(r"\s", text5)
print("Input Repr:", repr(text5))
print("Whitespace characters found:", [repr(c) for c in whitespace_chars])

# ==========================================
# 6. Replace Multiple Spaces with Single Space
# ==========================================
print("\n=== 6. Replace Multiple Spaces ===")
text6 = "This   is   a    sentence   with   extra   spaces."
cleaned_text6 = re.sub(r" +", " ", text6)
print("Original:", text6)
print("Cleaned: ", cleaned_text6)

# ==========================================
# 7. Words Containing Exactly 5 Characters
# ==========================================
print("\n=== 7. Words with Exactly 5 Characters ===")
text7 = "Apple zebra train elephant group high world"
five_letter_words = re.findall(r"\b[a-zA-Z]{5}\b", text7)
print("Input:", text7)
print("5-Letter Words:", five_letter_words)

# ==========================================
# 8. Words Ending with 's'
# ==========================================
print("\n=== 8. Words Ending with 's' ===")
text8 = "The cats and dogs run across the fields quickly"
ending_s = re.findall(r"\b\w+[sS]\b", text8)
print("Input:", text8)
print("Words ending with 's':", ending_s)

# ==========================================
# 9. Remove Special Characters
# ==========================================
print("\n=== 9. Remove Special Characters ===")
text9 = "Hello, World! @2026 #Python$%^&*()"
clean_text9 = re.sub(r"[^\w\s]", "", text9)
print("Original:", text9)
print("Cleaned: ", clean_text9)

# ==========================================
# 10. Count Words in a Sentence
# ==========================================
print("\n=== 10. Count Words ===")
text10 = "Python's regex library makes pattern matching easy!"
words = re.findall(r"\b\w+\b", text10)
print("Input:", text10)
print("Word Count:", len(words))

# ==========================================
# 11. Validate 10-Digit Indian Mobile Number
# ==========================================
print("\n=== 11. Validate 10-Digit Mobile Number ===")


def validate_mobile(mobile):
    pattern = r"^[6-9]\d{9}$"
    return bool(re.match(pattern, mobile))


test_numbers = ["9876543210", "5876543210", "987654321", "98765432100"]
for num in test_numbers:
    print(f"Number {num}: {'Valid' if validate_mobile(num) else 'Invalid'}")

# ==========================================
# 12. Validate Email Format
# ==========================================
print("\n=== 12. Validate Email Format ===")


def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


test_emails = [
    "user@example.com",
    "user.name@domain.co.in",
    "invalid-email@",
    "user@domain",
]
for em in test_emails:
    print(f"Email {em}: {'Valid' if validate_email(em) else 'Invalid'}")

# ==========================================
# 13. Extract Dates (DD-MM-YYYY)
# ==========================================
print("\n=== 13. Extract Dates (DD-MM-YYYY) ===")
text13 = "Events scheduled on 15-08-1947, 26-01-1950, and 20-10-2026."
dates = re.findall(r"\b\d{2}-\d{2}-\d{4}\b", text13)
print("Input:", text13)
print("Extracted Dates:", dates)

# ==========================================
# 14. Identify Web Addresses (http/https)
# ==========================================
print("\n=== 14. Identify Web Addresses ===")
text14 = "Visit https://www.google.com or http://example.org for info."
urls = re.findall(r"https?://[^\s]+", text14)
print("Input:", text14)
print("Extracted URLs:", urls)

# ==========================================
# 15. Extract Hashtags
# ==========================================
print("\n=== 15. Extract Hashtags ===")
text15 = "Learning #Python and #RegEx is fun! #coding2026 #AI"
hashtags = re.findall(r"#\w+", text15)
print("Input:", text15)
print("Extracted Hashtags:", hashtags)

# ==========================================
# 16. Password Strength Validation
# ==========================================
print("\n=== 16. Password Strength Validation ===")


def validate_password(pwd):
    pattern = (
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    )
    return bool(re.match(pattern, pwd))


passwords = ["Pass@1234", "weakpass", "Pass1234", "P@12"]
for p in passwords:
    print(f"Password '{p}': {'Strong' if validate_password(p) else 'Weak'}")

# ==========================================
# 17. Identify Consecutive Repeated Words
# ==========================================
print("\n=== 17. Consecutive Repeated Words ===")
text17 = "This is is a test test sentence sentence."
repeated_words = re.findall(r"\b(\w+)\s+\1\b", text17, flags=re.IGNORECASE)
print("Input:", text17)
print("Repeated Words Found:", list(set(repeated_words)))

# ==========================================
# 18. Extract 6-Digit Indian PIN Codes
# ==========================================
print("\n=== 18. Extract PIN Codes ===")
text18 = "Addresses: Mumbai 400001, Kolhapur 416012, Invalid 12345 or 1234567."
pin_codes = re.findall(r"\b[1-9]\d{5}\b", text18)
print("Input:", text18)
print("PIN Codes:", pin_codes)

# ==========================================
# 19. Validate Indian Vehicle Registration
# ==========================================
print("\n=== 19. Vehicle Registration Format ===")


def validate_vehicle_reg(v_num):
    pattern = r"^[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}$"
    return bool(re.match(pattern, v_num))


vehicle_numbers = ["MH12AB1234", "DL01A9999", "MH121234", "12MHAB1234"]
for vn in vehicle_numbers:
    print(
        f"Vehicle No '{vn}': {'Valid' if validate_vehicle_reg(vn) else 'Invalid'}"
    )

# ==========================================
# 20. Extract File Extensions
# ==========================================
print("\n=== 20. Extract File Extensions ===")
text20 = "Files: report.pdf, image.png, script.py, archive.tar.gz"
extensions = re.findall(r"\b\w+\.([a-zA-Z0-9]+)\b", text20)
print("Input:", text20)
print("Extracted Extensions:", extensions)

# ==========================================
# 21. Clean HTML Document Text
# ==========================================
print("\n=== 21. Clean HTML Text ===")
html_doc = "<html><body><h1>Title</h1><p>Hello,   World!  </p></body></html>"
clean_html = re.sub(r"<[^>]+>", "", html_doc)  # Remove tags
clean_html = re.sub(r"\s+", " ", clean_html).strip()  # Normalize whitespace
print("Original HTML:", html_doc)
print("Cleaned Text :", clean_html)

# ==========================================
# 22. Extract Invoice Details
# ==========================================
print("\n=== 22. Extract Invoice Details ===")
invoice_text = (
    "Invoice INV-2026-001 issued on 15-10-2026. Total Amount due: ₹45,500.50"
)
invoice_no = re.findall(r"\bINV-\d{4}-\d{3}\b", invoice_text)
inv_dates = re.findall(r"\b\d{2}-\d{2}-\d{4}\b", invoice_text)
inv_amounts = re.findall(r"[₹$]\d+(?:,\d+)*(?:\.\d{2})?", invoice_text)

print("Invoice Text:", invoice_text)
print("Invoice Number:", invoice_no)
print("Invoice Date:", inv_dates)
print("Amount:", inv_amounts)

# ==========================================
# 23. Python Single-Line Comments & Discussion
# ==========================================
print("\n=== 23. Single-line Comments Extraction & Discussion ===")
code_sample = """
# Main function start
x = 10  # Initialize variable
y = "# Not a comment"
"""
comments = re.findall(r"#.*", code_sample)
print("Extracted Comments:", comments)

print("\n--- Discussion ---")
print(
    "Why Regular Expressions alone may not correctly handle Python code comments:"
)
print(
    "1. String Literals: A '#' inside quotes (e.g., '# Not a comment') is treated as a comment by simple regex."
)
print(
    "2. Multiline Strings: Triple-quoted docstrings (''' or \"\"\") can span multiple lines and can contain '#' symbols."
)
print(
    "3. Context Parsing: Full Python grammar requires tracking token state (strings vs comments vs code), which full AST parsers or lexical analyzers handle better than simple regular expressions."
)

# ==========================================
# 24. Validate Product Code Pattern (ABC-1234-XY)
# ==========================================
print("\n=== 24. Validate Product Code Pattern ===")


def validate_product_code(p_code):
    pattern = r"^[A-Z]{3}-\d{4}-[A-Z]{2}$"
    return bool(re.match(pattern, p_code))


product_codes = ["ABC-1234-XY", "abc-1234-xy", "ABCD-1234-XY", "ABC-123-XY"]
for pc in product_codes:
    print(
        f"Product Code '{pc}': {'Valid' if validate_product_code(pc) else 'Invalid'}"
    )

# ==========================================
# 25. Extract Student Records (Name, Roll, Marks)
# ==========================================
print("\n=== 25. Extract Student Records ===")
student_data_text = """
Name: Alice, Roll: 101, Marks: 88
Name: Bob, Roll: 102, Marks: 92
Name: Charlie, Roll: 103, Marks: 79
"""
pattern25 = r"Name:\s*([A-Za-z]+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)"
matches25 = re.findall(pattern25, student_data_text)

print("Parsed Records:")
for name, roll, marks in matches25:
    print(f"Name: {name:<10} | Roll: {roll:<5} | Marks: {marks}")

# ==========================================
# 26. Extract Academic Reference Fields
# ==========================================
print("\n=== 26. Extract Academic Reference Fields ===")
ref_text = """
Reference 1: Author (2024). Article Title. DOI: 10.1000/182, Contact: author@univ.edu, Link: https://journal.org/paper1
Reference 2: Author2 (2026). Paper Title. DOI: 10.1016/j.pas.2026.01.002, Contact: research2@lab.io, Link: http://research.com/p2
"""

dois = re.findall(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+\b", ref_text)
years = re.findall(r"\b(19\d{2}|20\d{2})\b", ref_text)
emails = re.findall(
    r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b", ref_text
)
urls_ref = re.findall(r"https?://[^\s,]+", ref_text)

print("DOIs:", dois)
print("Publication Years:", years)
print("Email Addresses:", emails)
print("URLs:", urls_ref)