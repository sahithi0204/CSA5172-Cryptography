import re

def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I")  
    key = re.sub(r'[^A-Z]', '', key)  # Remove non-alphabetic characters
    key = key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Append remaining characters
    
    matrix = []
    for char in key:
        if char not in matrix:
            matrix.append(char)
    
    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def find_position(playfair_matrix, letter):
    for i in range(5):
        for j in range(5):
            if playfair_matrix[i][j] == letter:
                return i, j

def encrypt(plain_text, playfair_matrix):
    plain_text = plain_text.upper().replace("J", "I")  # Replace J with I
    plain_text = re.sub(r'[^A-Z]', '', plain_text)  # Remove non-alphabetic characters
    
    encrypted_text = ""
    i = 0
    while i < len(plain_text):
        pair = plain_text[i:i+2]
        
        if len(pair) == 1:  # Handle odd number of characters
            pair += 'X'
        
        if pair[0] == pair[1]:  # Handle repeated letters
            pair = pair[0] + 'X' + pair[1]
            i += 1
        
        row1, col1 = find_position(playfair_matrix, pair[0])
        row2, col2 = find_position(playfair_matrix, pair[1])
        
        if row1 == row2:  # Same row
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:  # Same column
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:  # Rectangle case
            col1, col2 = col2, col1
        
        encrypted_text += playfair_matrix[row1][col1] + playfair_matrix[row2][col2]
        i += 2
    
    return encrypted_text

# Main program
key = "MFHIJKUNOPQZVWXYELARGDSTBC"
message = "Must see you over Cadogan West. Coming at once."

playfair_matrix = generate_playfair_matrix(key)
encrypted_message = encrypt(message, playfair_matrix)

print("Playfair Matrix:")
for row in playfair_matrix:
    print(' '.join(row))

print("\nEncrypted Message:")
print(encrypted_message)
