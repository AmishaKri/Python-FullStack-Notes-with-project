import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
print(enc.encode("Hello, world!"))

decoded=enc.decode([9906, 11, 1917, 0])
print(decoded)