class Codec:
    def encode(self, strs: list) -> str:
        """Encodes a list of strings to a single string."""
        encoded_string = ''
        for s in strs:
            # Length of string followed by the string itself
            encoded_string += str(len(s)) + '#' + s
        return encoded_string

    def decode(self, encoded_str: str) -> list:
        """Decodes a single string back to a list of strings."""
        decoded_strings = []
        i = 0
        while i < len(encoded_str):
            # Find the next '#' which separates length from the string
            j = i
            while encoded_str[j] != '#':
                j += 1

            # Length of the string
            length = int(encoded_str[i:j])
            # The string itself
            decoded_strings.append(encoded_str[j + 1:j + 1 + length])
            # Move i past the decoded part
            i = j + 1 + length

        return decoded_strings
