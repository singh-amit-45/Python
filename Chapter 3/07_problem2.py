# Write a Python program to replace the placeholders <|Name|> and <|Date|> in a letter template with actual values."
letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "amit").replace("<|Date|", "24 September 2080"))