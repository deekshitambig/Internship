import rsa
(public_key, private_key) =rsa.newkeys(786)
message="secret"
encrypted =rsa.encrypt(message.encode(),public_key)
print("encrypted:-",encrypted)
decrypted=rsa.decrypt(encrypted,private_key).decode()
print("decrypted:-",decrypted)
print(public_key)
