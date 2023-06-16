import sys

def encode(message):
    return " ".join([hex(ord(c))[2:] for c in message])

def encode_times(message, n):
    for _ in range(n):
        message = encode(message)

    return message

if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        message = str(file.read())

    with open(sys.argv[1] + "encoded.txt", "w") as file:
        file.write(encode_times(message, int(sys.argv[2])))