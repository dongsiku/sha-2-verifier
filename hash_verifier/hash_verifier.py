import hashlib
import argparse
from pathlib import Path
import re


class HashVerifier:
    def __init__(self, target_filename: Path) -> None:
        """Initialize HashVerifier

        Args:
            target_filename (Path): Absolute path of target binary file
        """
        self.TARGET_FILENAME = target_filename

    def get_hash_from_target_file(self, hash_file_suffix: str) -> str:
        """Get hash value from target binary file

        Args:
            hash_file_suffix (str): The suffix of hash file

        Returns:
            str: Hash value from target file
        """
        hash_value = ""
        with open(self.TARGET_FILENAME, "rb") as f:
            file_content = f.read()
        if hash_file_suffix == ".sha256":
            hash_value = hashlib.sha256(file_content).hexdigest()
        elif hash_file_suffix == ".sha512":
            hash_value = hashlib.sha512(file_content).hexdigest()
        elif hash_file_suffix == ".md5":
            hash_value = hashlib.md5(file_content).hexdigest()
        print(
            f"Target binary file: {self.TARGET_FILENAME.name} -> {hash_value}"
        )
        return hash_value

    def main(self) -> None:
        """Main script;
        Detect hash file and verify target file with the hash file

        Raises:
            FileExistsError: Several hash file exist
            FileNotFoundError: No hash file exists

        Returns:
            bool: Did verify the target file
        """
        HASH_FILE_SUFFIX_LIST = [".sha256", ".sha512", ".md5"]

        hash_filename = None
        # hash_file_suffix = ""
        for temp_hash_file_suffix in HASH_FILE_SUFFIX_LIST:
            temp_hash_filename = self.TARGET_FILENAME.with_suffix(
                self.TARGET_FILENAME.suffix + temp_hash_file_suffix
            )
            if temp_hash_filename.exists():
                if hash_filename is None:
                    hash_filename = temp_hash_filename
                    # hash_file_suffix = temp_hash_file_suffix
                else:
                    raise FileExistsError("There are several hash files.")
        if hash_filename is None:
            raise FileNotFoundError(
                "Save hash value to text file as "
                f"{self.TARGET_FILENAME.name}{HASH_FILE_SUFFIX_LIST}"
            )
        if self.verify_target_file_with_hash_file(hash_filename):
            print("\033[32mOK\033[0m")
            return True
        else:
            print("\033[31mError\033[0m")

        return False

    def verify_target_file_with_hash_file(self, hash_filename: Path):
        """Verify binary file with hash file

        Args:
            hash_filename (Path): File name of hash file

        Returns:
            bool: Did verify the target file
        """
        with hash_filename.open("r") as hash_f:
            hash_file_lines = hash_f.readlines()
            hase_from_hash_file = ""
            for hash_file_line in hash_file_lines:
                temp_hash_file_line = re.split("\\s+", hash_file_line, 1)
                # When only target hash value is written to hash file
                hase_from_hash_file = temp_hash_file_line[0]

                # When several hash value are written to hash file
                if len(temp_hash_file_line) > 1 and re.search(
                        self.TARGET_FILENAME.name, temp_hash_file_line[1]
                ):
                    hase_from_hash_file = temp_hash_file_line[0]
                    break

        hash_value = self.get_hash_from_target_file(hash_filename.suffix)
        print(f"Hash file: {hash_filename.name} -> {hase_from_hash_file}")
        if hase_from_hash_file == hash_value:
            return True

        return False


def main() -> None:
    """Main script for setup.cfg"""

    parser = argparse.ArgumentParser(
        description="Verify hash value of file(s)"
    )
    parser.add_argument(
        "target_filenames", type=Path, nargs="+",
        help="Select the file(s) which you want to verify",
    )
    # parser.add_argument(
    #     "--debug", help="Debug mode", action="store_true",
    # )
    args = parser.parse_args()

    for basename in args.target_filenames:
        filename = basename.resolve()
        hash_verifier = HashVerifier(filename)
        hash_verifier.main()


if __name__ == "__main__":
    main()
