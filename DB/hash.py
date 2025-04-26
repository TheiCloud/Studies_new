import hashlib

def get_hash(data):

    string = "|".join(data).encode("utf-8")

    return hashlib.sha256(string).hexdigest()[:8]


a = ["Привет", "Андрей"]

print(get_hash(a))



