import itertools


solutions = [
    'acoltoe', 
    'acoltpd',
    'acoltqc',
    'acoltrb',
    'acoltsa',
    'acoluar',
    'acolubq',
    'acolucp',
    'acoludo',
    'acoluen',
    'acolufm'
]


def get_loop_number(password):
    total = 0
    for c in password:
        total += ord(c)
    return total


def get_crc(lpn):
    crc = 0
    for i in "1M953":  # first 5 bytes
        z = (ord(i) & 0xff) ^ lpn
        crc += z
    return hex(crc)


def find_passwords_matching_crc(crc='0xdca'):
    passwords = []
    for j in range(7,9):
        for i in itertools.product([chr(i) for i in range(97, 122)], repeat=j):
            word = "".join(i)
            if get_crc(get_loop_number(word + "\n")) == crc:
                passwords.append(word)
    return passwords


def find_password_matching_crc(crc='0xdca'):
    for i in itertools.product([chr(i) for i in range(97, 122)], repeat=7):
        word = "".join(i)
        if get_crc(get_loop_number(word + "\n")) == crc:
            return word


def write_list_to_file(word_list):
    with open("word_list", "w") as f:
        for word in word_list:
            f.write(word + "\n")


if __name__ == "__main__":
    password = find_password_matching_crc()
    print(password)
