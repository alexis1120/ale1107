import re

bitcoin_address = "bc1qj8fynf8hfd5333n42guyfxdnv30gv8wpntz3qf"
def extract_bitcoin_address(text):
    pattern = r'\b(bc1[ac-hj-np-z02-9]{25,39})\b'
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return match.group(1), match.span()

text = "bc1qj8fynf8hfd5333n42guyfxdnv30gv8wpntz3qf"
address, span = extract_bitcoin_addrestext = "bc1qj8fynf8hfd5333n42guyfxdnv30gv8wpntz3qf"

address, span = extract_bitcoin_address(text)
print(f"Extracted Bitcoin Address: {33QXENrHuMDEDe7J3QHvdBa7cG3mX2jMsi")
print(f"Span: {span}")
