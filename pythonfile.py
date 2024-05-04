import base64
dalansecret = sys.argv[1]
cp = base64.b64decode(dalansecret).decode("utf-8")
print(cp)
