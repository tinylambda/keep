import hmac


digest_maker = hmac.new(b"secret-shared-key-goes-here")

with open("../pymotw.crt", "rb") as f:
    while True:
        block = f.read(1024)
        if not block:
            break
        digest_maker.update(block)

digest = digest_maker.hexdigest()
print(digest)
