message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar_decode(message, offset):
    decoded_message = []
    for ch in message:
        if ch == " ": decoded_message.append(" ")
        elif ch == ".": decoded_message.append(".")
        elif ch == "!": decoded_message.append("!")
        elif ch == "?": decoded_message.append("?")
        i = 0
        while i < len(alphabet):
            if ch == alphabet[i]: 
                if i > (25 - offset):
                    i = (offset - 1) - (25 - i)
                else: i += offset
                decoded_message.append(alphabet[i])
                break
            i += 1
    return "".join(decoded_message)

def caesar_encode(message, offset):
    encoded_message = []
    for ch in message:
        if ch == " ": encoded_message.append(" ")
        elif ch == ".": encoded_message.append(".")
        elif ch == "!": encoded_message.append("!")
        elif ch == "?": encoded_message.append("?")
        i = 0
        while i < len(alphabet):
            if ch == alphabet[i]: 
                if i < offset:
                    i = 26 - (offset - i)
                else: 
                    i -= offset
                encoded_message.append(alphabet[i])
                break
            i += 1
    return "".join(encoded_message)

decoded = caesar_decode(message, 7)
print(decoded)

#encoded = caesar_encode(message, 10)
#print(encoded)
 
