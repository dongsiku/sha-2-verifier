import hashlib
import sys
from os import path


class VerifySHA:
    def __init__(self, target_filename):
        self.target_filename = target_filename

    def return_hash_from_target_file(self, sha_num):
        with open(self.target_filename, 'rb') as f:
            if sha_num == 256:
                checksum = hashlib.sha256(f.read()).hexdigest()
            elif sha_num == 512:
                checksum = hashlib.sha512(f.read()).hexdigest()
            print("Hash value: {}".format(checksum))

        return checksum

    def check_hash_key(self):
        sha256_filename = "{}.sha256".format(self.target_filename)
        sha512_filename = "{}.sha512".format(self.target_filename)
        if path.isfile(sha256_filename):
            sha_filename = sha256_filename
            sha_num = 256
        elif path.isfile(sha512_filename):
            sha_filename = sha512_filename
            sha_num = 512
        else:
            raise FileNotFoundError("No file *.sha256 or *.sh512")

        with open(sha_filename, "r") as sha_f:
            hash_value = self.return_hash_from_target_file(sha_num)
            sha_lines = sha_f.readlines()
            for sha_line in sha_lines:
                temp_sha_line = sha_line.strip().rsplit(" ", 1)
                if len(temp_sha_line) > 1:
                    if temp_sha_line[1] == self.target_filename:
                        saved_hase_value = temp_sha_line[0]
                        break
                else:
                    saved_hase_value = temp_sha_line[0]

            print(".sha{}: {}".format(sha_num, saved_hase_value))
            if saved_hase_value == hash_value:
                print("OK")
            else:
                print("Error")


if __name__ == "__main__":
    vsha = VerifySHA(sys.argv[1])
    vsha.check_hash_key()
