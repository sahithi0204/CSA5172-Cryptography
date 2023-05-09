mport numpy as np

def hill_cipher(message, key):
    msg_num = [ord(char) - 65 for char in message.upper()]
    msg_len = len(msg_num)
    while msg_len % len(key) != 0:
        msg_num.append(23)
        msg_len += 1
    msg_mat = np.reshape(msg_num, (-1, len(key)))
    enc_mat = np.matmul(msg_mat, key) % 26
    enc_num = np.reshape(enc_mat, (-1,)).tolist()
    ciphertext = ''.join([chr(num + 65) for num in enc_num])

    return ciphertext
