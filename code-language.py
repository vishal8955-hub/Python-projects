def encrypt(message):
  conversion_table = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ","zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA")
  return message.translate(conversion_table)


message = ''
encrypted_message = encrypt(message)
print(encrypted_message)

 