import hashlib
import sys
from pathlib import Path
import re


class VerifySHA:
    def __init__(self) -> None:
        if len(sys.argv) != 1:
            target_basename = sys.argv[1]
        else:
            target_basename = sys.argv[0]
        self.TARGET_FILENAME = Path(target_basename).resolve()

    def return_hash_from_target_file(self, sha_num: str) -> str:
        checksum = ""
        with open(self.TARGET_FILENAME, 'rb') as f:
            if sha_num == "256":
                checksum = hashlib.sha256(f.read()).hexdigest()
            elif sha_num == "512":
                checksum = hashlib.sha512(f.read()).hexdigest()
            print(f"{self.TARGET_FILENAME.name}: {checksum}")
        return checksum

    def check_hash_key(self) -> None:
        SHA_BASENAME_LIST = {
            "256": f"{self.TARGET_FILENAME}.sha256",
            "512": f"{self.TARGET_FILENAME}.sha512"
        }
        sha_num = False
        for sha_basename_key in SHA_BASENAME_LIST.keys():
            if (self.TARGET_FILENAME.parent /
                    SHA_BASENAME_LIST[sha_basename_key]).exists():
                sha_num = sha_basename_key
        if sha_num is False:
            raise FileNotFoundError(
                "Save hash value to text file as "
                f"{self.TARGET_FILENAME.name}.sha256 or .sha512"
            )

        SHA_FILENAME = self.TARGET_FILENAME.parent / SHA_BASENAME_LIST[sha_num]
        with SHA_FILENAME.open("r") as sha_f:
            sha_lines = sha_f.readlines()
            saved_hase_value = ""
            for sha_line in sha_lines:
                temp_sha_line = re.split("\\s+", sha_line, 1)
                saved_hase_value = temp_sha_line[0]
                if len(temp_sha_line) > 1 and \
                        temp_sha_line[1] == self.TARGET_FILENAME:
                    saved_hase_value = temp_sha_line[0]
                    break

        hash_value = self.return_hash_from_target_file(sha_num)
        print(f"{SHA_FILENAME.name}: {saved_hase_value}")
        if saved_hase_value == hash_value:
            print("OK")
        else:
            print("Error")


if __name__ == "__main__":
    vsha = VerifySHA()
    vsha.check_hash_key()
