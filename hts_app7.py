def get_loop_number(password):
    total = 0
    for c in password:
        total += ord(c)
    return total


if __name__ == "__main__":
    user_input = "1234\n"
    loop_number = get_loop_number(user_input)
    print(loop_number, hex(loop_number))
    with open("encrypted.enc", "rb") as f:
        enc_str = f.read(5)
    # print(len(enc_str), hex(len(enc_str)))

    crc = 0
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    idx = 0
    # loop_counter @0018FF20
    # encrypted char index idx; @0018FF24
    # encrypted string char value, i; @0018FF28
    # loop_number @0x0018FF2C
    # CRC @0x0018FF30
    # Result @0x0018FF34
    # ebp @0x0018FF48
    for i in enc_str:  # first 5 bytes
        z = (i & 0xff) ^ loop_number
        crc += z
        result[idx] = (i & 0xff) ^ loop_number
        loop_counter = 1  # 0 or 1?
        while loop_counter < loop_number:
            if result[idx] & 1 == 0:
                result[idx] = result[idx] >> 1
            else:
                result[idx] = result[idx] >> 1
                result[idx] |= 0x80
            loop_counter += 1
        result[idx] += 3
        idx += 1  # can be handled by enumerate(enc_str)
    print(result)
    if crc == 0x0dca:
        print("solved")
        exit()
    print("Invalid password")
    # for _c in result:
    #     y += chr(_c)
