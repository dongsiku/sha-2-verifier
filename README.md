# Hash Verifier

This script simplifies verifications of files using sha256sum or sha512sum.

## Required

- Python: `>=3.8`
- PyPI

## Installation

There two ways to install this application.

1. Use pip (Recommended)

    ```bash:with_pip
    pip install -e "git+https://github.com/muneue-suwa/hash-verifier@v3.1.1#egg=hash-verifier"
    ```

1. Write alias to `.bash_aliases` or `.bashrc` (Linux user)

   ```bash:alias
   alias sha2-verifier="/PATH_TO_APPLICATION/sha2-verifier/sha2_verifier/sha2_verifier.py"
   ```

## Usage

### Create \*.sha256 file (or \*.sha512)

Download the hash value of the file which you want to verify, and save it to text file as `***.sha256` (or `***.sha512` for sha512sum).

### Run this application

```shell-session:lauch-the-application
vh TARGET_FILENAME
```

### Example

e.g. arduino-1.8.9-linux64.tar.xz

```bash:example
$ echo 1cea9714...(The rest is omitted) > arduino-1.8.9-linux64.tar.xz.sha512
$ vh arduino-1.8.9-linux64.tar.xz
arduino-1.8.9-linux64.tar.xz: 1cea9714...
arduino-1.8.9-linux64.tar.xz.sha512: 1cea9714...
OK
```
