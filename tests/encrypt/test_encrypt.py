import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(100, 10)
    with pytest.raises(TypeError):
        encrypt_message('', '')

    assert encrypt_message('encrypt', 2) == 'tpyrc_ne'
    assert encrypt_message('encrypt', 3) == 'cne_tpyr'
    assert encrypt_message('encrypt', 20) == 'tpyrcne'
