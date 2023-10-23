# to encode string
import base64

some_string = "Each Base64 character represents 6 bits of data"
some_string_bytes = some_string.encode("ascii")
base64_bytes = base64.b64encode(some_string_bytes)
base64_string = base64_bytes.decode("ascii")
print(f"Result: {base64_string}")
