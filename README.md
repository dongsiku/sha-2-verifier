# SHA-2 Verifier

This script simplifies verifications of files using sha256sum or sha512sum.

## Required

- Python: `>=3.6`
- PyPI

## Installation

There two ways to install this application.

1. Write alias to `.bash_aliases` or `.bashrc`
   
   ```bash:alias
   alias sha2-verifier="/PATH_TO_APPLICATION/sha2-verifier/sha2_verifier/sha2_verifier.py"
   ```

2. Use pip (It **cannot** work well)
    
    ```bash:with_pip
    pip install -e "git+https://github.com/dongsiku/sha2-verifier#egg=sha2-verifier"
    ```

## Usage

### Create \*.sha256 file (or \*.sha512)

Download the hash value of the file which you want to verify, and save it to text file as `***.sha256` (or `***.sha512` for sha512sum).

### Run this application

```shell-session:lauch-the-application
verify-sha2 TARGET_FILENAME
```

### Example

e.g. arduino-1.8.9-linux64.tar.xz

```bash:example
$ echo 1cea9714...(The rest is omitted) > arduino-1.8.9-linux64.tar.xz.sha512
$ verify-sha2 arduino-1.8.9-linux64.tar.xz
arduino-1.8.9-linux64.tar.xz: 1cea9714...
arduino-1.8.9-linux64.tar.xz.sha512: 1cea9714...
OK
```
