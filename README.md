# sha256sum_linux_iso

This script also can use for sha512sum.

## Usage

### Make *.sha256 (or *.sha512)

Download the hash value and save as `***.sha256` (or `***.sha512` for sha512sum). 

### Launch this application

```shell-session:lauch-the-application
python3 main.py [THE_VERIFYING_FILE_NAME]
```

### Example

e.g. arduino-1.8.9-linux64.tar.xz

```bash:example
$ echo 1cea9714...(The rest is omitted) > arduino-1.8.9-linux64.tar.sha512 
$ python3 /path/to/script/main.py arduino-1.8.9-linux64.tar.xz 
Hash value: 1cea9714...
.sha512: 1cea9714...
OK
```
