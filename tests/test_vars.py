from os import environ

import pytest

from trav import Travis
from trav.main import var_is_true


def test_vars():
    assert Travis.HAS_JOSH_K_SEAL_OF_APPROVAL == \
           var_is_true('HAS_JOSH_K_SEAL_OF_APPROVAL')
    assert Travis.TRAVIS_SUDO == var_is_true('TRAVIS_SUDO')

    assert Travis.DEBIAN_FRONTEND == environ.get('DEBIAN_FRONTEND')
    assert Travis.USER == environ.get('USER')

    with pytest.raises(AttributeError):
        Travis.HAS_KAI_CHEN_SEAL_OF_APPROVAL
