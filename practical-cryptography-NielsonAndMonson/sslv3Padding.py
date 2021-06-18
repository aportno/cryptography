def sslv3Pad(message):
    padNeeded = (16 - (len(message) % 16)) - 1
    padding = padNeeded.to_bytes(padNeeded+1, "big")
    return message+padding


def sslv3Unpad(padded_message):
    paddingLen = padded_message[-1] + 1
    return padded_message[:paddingLen]
