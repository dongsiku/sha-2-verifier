from pathlib import Path
import pytest

from hash_verifier import hash_verifier, __version__

PROJ_DIRNAME = Path(__file__).resolve().parent
TARGET_FILENAME = PROJ_DIRNAME / "sample_target_file.png"


def test_version():
    assert __version__ == '3.1.0'


def test_all_hash_files():
    """Test with sample_target_file.png{.sha512, .md5}
    """
    hv = hash_verifier.HashVerifier(TARGET_FILENAME)
    for hash_suffix in [".sha512", ".md5"]:
        hash_dirname = TARGET_FILENAME.parent / "hash_files"
        hash_filename = hash_dirname / f"{TARGET_FILENAME.name}{hash_suffix}"
        assert hv.verify_target_file_with_hash_file(hash_filename) is True


def test_sha256():
    """Test main script
    """
    hv = hash_verifier.HashVerifier(TARGET_FILENAME)
    assert hv.main() is True
