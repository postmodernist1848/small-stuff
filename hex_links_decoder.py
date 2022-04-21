
BYTES_WIDTH = 5
link = 'https://navopros.ru/chto-takoe/preview#:~:text=%D0%9F%D1%80%D0%B5%D0%B2%D1%8C%D1%8E%20(%D1%83%D0%B4%D0%B0%D1%80%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%B0%20%C2%AB%D1%8E%C2%BB,%D1%82%D0%BE%20%D1%82%D0%B8%D0%BF%D0%B0%20%C2%AB%D0%BF%D1%80%D0%B5%D0%B4%2D%C2%BB.'
def decode_hex_link(link):
    hex = ''
    for char in link:
        if char.isdigit() or char.isupper():
            hex += char
    print(hex, 'translates to:')
    bytes = [hex[i:i + 2] for i in range(0, len(hex) - 1, 2)]
    
    while bytes:
        byte_portion = ' '.join(bytes[:BYTES_WIDTH])
        conversion = ' '.join(chr(int(byte, 16)) for byte in bytes[:BYTES_WIDTH])
        print(f'{conversion}')
        del bytes[:BYTES_WIDTH]
    
decode_hex_link(link)
