import pytest
from trav import Travis, TRAVIS_BASE_URL, SvgRequestFailed


def test_get_travis_badge_url():
    result = Travis.get_travis_badge_url('coala', 'coala-bears', 'master')
    assert result == TRAVIS_BASE_URL + 'coala/coala-bears.svg?branch=master'


def test_get_svg_from_badge_url():
    with pytest.raises(SvgRequestFailed):
        Travis.get_svg_from_badge_url(TRAVIS_BASE_URL + 'apples/asdf/')

    svg = Travis.get_svg_from_badge_url(TRAVIS_BASE_URL +
                                        'kx-chen/travis-fail.svg'
                                        '?branch=master')
    assert svg is not None
    assert svg != ''
