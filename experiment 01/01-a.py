import re
text = "Call me at 9876543210 or 08123456789. Invalid: 12345, +919876543210, 9876543."
mobile_numbers = re.findall(r'\b[6-9]\d{9}\b', text)
print("Mobile Numbers Found:", mobile_numbers)