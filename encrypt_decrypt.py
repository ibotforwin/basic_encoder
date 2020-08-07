# Assuming codes is an argument that is different every time.

class Encryption:
    def __init__(self, codes):
        self.codes=codes

    def encrypt(self, message):
        encrypted_message=''
        for value in message:
            if value in self.codes:
                encrypted_message=encrypted_message+str(self.codes[value])
            else:
                encrypted_message=encrypted_message+str(value)
        return encrypted_message

    def decrypt(self, message):
        inv_codes = {v: k for k, v in codes.items()}
        decrypted_message=''
        for value in message:
            try:
                int(value)
                if int(value) in inv_codes:
                    decrypted_message=decrypted_message+str(inv_codes[int(value)])
            except:
                decrypted_message=decrypted_message+str(value)
        return decrypted_message

codes = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
e=Encryption(codes)

test_string='Hey bob, how is the weather in Vancouver?'
print(e.decrypt(e.encrypt(test_string)))


