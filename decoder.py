import sys

def decode(message):
    message = message.split(" ")
    message = [chr(int(c, 16)) for c in message]
    return "".join(message)

def main(message):
    i = 0
    while True:
        try:
            message = decode(message)
            i += 1
        except ValueError:
            break

    print(f"Encoded {i} times")
    print(message)

if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        message = str(file.readlines()[0])

    main(message)