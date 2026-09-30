def decode_secret_message(filename):
    f = open(filename, 'rb')
    bs = f.read()
    
    
    text = bs.decode('cp500')
    return text
message = decode_secret_message('part2/secret_message.txt')
print(message)

out = open('part2/secret_message.utf8', 'w', encoding='utf-8')
out.write(message)
out.close()