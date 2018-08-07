# sha256sum_linux_iso

## Usage

### Make *.sha256

Download the hash value and save as `***.sha256`. 

>e.g. ubuntu-18.04.1-desktop-amd64.iso <br>
>ubuntu-18.04.1-desktop-amd64.sha256

### check hash value

```
$ python3 ~/Git/sha256_linux_iso/main.py ubuntu-18.04.1-desktop-amd64.iso
OK  # when the value is correct
```

