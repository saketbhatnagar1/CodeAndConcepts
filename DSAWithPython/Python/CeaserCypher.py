class CeaserCypher:

    def __init__(self):
        pass
    def encrypt(original_text, shift):
        alphabets = [chr(i) for i in range(97, 123)]  # a–z
        new_text = ""
        original_text = original_text.lower()

        for ch in original_text:
            if ch in alphabets:
                new_index = (alphabets.index(ch) + shift) % len(alphabets)
                new_text += alphabets[new_index]
            else:
                new_text += ch  # keep spaces or symbols unchanged
        print(new_text)
        return new_text

    def decrypt(cypher_text,shift):
        alphabets = [chr(i) for i in range(97, 123)]
        orignal_text = ""
        cypher_text = cypher_text.lower()
        for ch in cypher_text:
            if ch in alphabets:
                orignal_index = (alphabets.index(ch)-shift)%len(alphabets)
                orignal_text+=alphabets[orignal_index]
        print(orignal_text)
        return orignal_text
encryptedText = CeaserCypher.encrypt("saketz",1)
CeaserCypher.decrypt(encryptedText,1)