# SHA-2 Verifier

This script simplifies verifications of files using sha256sum or sha512sum.

## Usage

### Create \*.sha256 file (or \*.sha512)

Download the hash value of the file which you want to verify, and save it to text file as `***.sha256` (or `***.sha512` for sha512sum).

### Launch this application

```shell-session:lauch-the-application
python3 sha-2-verifier/sha-2-verifier.py [THE_FILE_NAME_WHICH_YOU_WANT_TO_VERIFY]
```

### Example

e.g. arduino-1.8.9-linux64.tar.xz

```bash:example
$ echo 1cea9714...(The rest is omitted) > arduino-1.8.9-linux64.tar.xz.sha512
$ python3 /path/to/script/sha-2-verifier.py arduino-1.8.9-linux64.tar.xz
Hash value: 1cea9714...
.sha512: 1cea9714...
OK
```
