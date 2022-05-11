#!/usr/bin/env python3

# Print out the unicde block range

s = "".join(f"{chr(b)} " for b in range(0x2580, 0x25A0))
print(s)
print(s)
print(s)
print()

# Upper and lower block
print("\u2580\u2584")
print()

s = "".join(f"{chr(b)} " for b in range(0x1fb00, 0x1fb3c))
print(s)
print()
