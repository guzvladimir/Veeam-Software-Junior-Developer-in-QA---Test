import pytest
from check_checksum import check_checksum, checksum


def test_file_exists():
    with pytest.raises(FileNotFoundError):
        check_checksum("path_file", "directory")


@pytest.mark.parametrize(
    ["data", "algorithm", "expected_result"],
    [
        (b"Hello world!", "md5", "86fb269d190d2c85f6e0468ceca42a20"),
        (b"Test text", "sha1", "82022e1782b92dce5461ee636a6c5bea8509ffee"),
        (
            b"Another algorithm\n",
            "sha256",
            "536f15e4f6e41e1029550ee362c6ff3b626b9f3695ec8dedd86a6607375ea9ee",
        ),
        (b"No such algorithm", "sha224", None),
    ],
)
def test_checksum(data, algorithm, expected_result):
    assert checksum(data, algorithm) == expected_result
