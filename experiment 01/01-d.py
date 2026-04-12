import re
text = "Uh 123 hello!!! this is, um... a speech2text output?? with $pecial ch@racters & numbers 456!"
# remove everything except letters and spaces
text = re.sub(r'[^a-zA-Z ]', '', text)
# remove extra spaces
text = re.sub(r' +', ' ', text)
print(text)