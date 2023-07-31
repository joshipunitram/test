def decode(message_file):
    # Step 1: Read the encoded message file and create the mapping dictionary
    with open(message_file, 'r') as file:
        encoded_text = file.readlines()
    word_dict = {}
    for line in encoded_text:
        parts = line.strip().split(' ')
        number = int(parts[0].strip())
        word = parts[1].strip()
        word_dict[number] = word

    # Step 2: Sort the dictionary based on the numbers in ascending order
    sorted_dict = dict(sorted(word_dict.items()))

    # Step 3: Rearrange the sorted dictionary in the form of a pyramid
    pyramid = []
    row = []
    row_length = 1
    for number, word in sorted_dict.items():
        row.append(word)
        if len(row) == row_length:
            pyramid.append(row)
            row = []
            row_length += 1

    # Step 4: Choose the last word from each row of the pyramid to form the decoded output
    decoded_output = ' '.join(row[-1] for row in pyramid)

    return decoded_output

# Example usage:
encoded_file_path = 'message_file.txt'
decoded_message = decode(encoded_file_path)
print(decoded_message)
