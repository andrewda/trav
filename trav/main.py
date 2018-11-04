import os
import requests

TRAVIS_BASE_URL = 'https://api.travis-ci.org/'
TRAVIS_BADGE_URL = TRAVIS_BASE_URL + '{group}/{repo}.svg?branch={branch}'


class SvgRequestFailed(Exception):
    pass


def var_is_true(var):
    if os.environ.get(var) and os.environ.get(var).lower() == 'true':
        return True
    else:
        return False


class Travis(object):
    @staticmethod
    def get_svg_from_badge_url(url):
        svg = requests.get(url)
        if svg.status_code != 200:
            raise SvgRequestFailed("Unable to complete the SVG request")
        return svg

    @staticmethod
    def get_travis_badge_url(group, repo, branch):
        return TRAVIS_BADGE_URL.format(
            group=group, repo=repo, branch=branch)


    CI = var_is_true('CI')
    TRAVIS = var_is_true('TRAVIS')
    CONTINUOUS_INTEGRATION = var_is_true('CONTINUOUS_INTEGRATION')
    DEBIAN_FRONTEND = os.environ.get('DEBIAN_FRONTEND')
    HAS_JOSH_K_SEAL_OF_APPROVAL = var_is_true('HAS_JOSH_K_SEAL_OF_APPROVAL')
    USER = os.environ.get('USER')
    HOME = os.environ.get('HOME')
    LANG = os.environ.get('LANG')
    LC_ALL = os.environ.get('LC_ALL')
    RAILS_ENV = os.environ.get('RAILS_ENV')
    RACK_ENV = os.environ.get('RACK_ENV')
    MERB_ENV = os.environ.get('MERB_ENV')

    ALLOW_FAILURE = var_is_true('TRAVIS_ALLOW_FAILURE')
    BRANCH = os.environ.get('TRAVIS_BRANCH')
    BUILD_DIR = os.environ.get('TRAVIS_BUILD_DIR')
    BUILD_ID = os.environ.get('TRAVIS_BUILD_ID')
    BUILD_NUMBER = os.environ.get('TRAVIS_BUILD_NUMBER')
    BUILD_STAGE_NAME = os.environ.get('TRAVIS_BUILD_STAGE_NAME')
    BUILD_WEB_URL = os.environ.get('TRAVIS_BUILD_WEB_URL')
    COMMIT = os.environ.get('TRAVIS_COMMIT')
    COMMIT_MESSAGE = os.environ.get('TRAVIS_COMMIT_MESSAGE')
    COMMIT_RANGE = os.environ.get('TRAVIS_COMMIT_RANGE')
    EVENT_TYPE = os.environ.get('TRAVIS_EVENT_TYPE')
    JOB_ID = os.environ.get('TRAVIS_JOB_ID')
    JOB_NUMBER = os.environ.get('TRAVIS_JOB_NUMBER')
    JOB_WEB_URL = os.environ.get('TRAVIS_JOB_WEB_URL')
    OS_NAME = os.environ.get('TRAVIS_OS_NAME')
    OSX_IMAGE = os.environ.get('TRAVIS_OSX_IMAGE')
    PULL_REQUEST = os.environ.get('TRAVIS_PULL_REQUEST')
    PULL_REQUEST_BRANCH = os.environ.get('TRAVIS_PULL_REQUEST_BRANCH')
    PULL_REQUEST_SHA = os.environ.get('TRAVIS_PULL_REQUEST_SHA')
    PULL_REQUEST_SLUG = os.environ.get('TRAVIS_PULL_REQUEST_SLUG')
    REPO_SLUG = os.environ.get('TRAVIS_REPO_SLUG')
    SECURE_ENV_VARS = var_is_true('TRAVIS_SECURE_ENV_VARS')
    SUDO = var_is_true('TRAVIS_SUDO')
    TEST_RESULT = os.environ.get('TRAVIS_TEST_RESULT')
    TAG = os.environ.get('TRAVIS_TAG')

    DART_VERSION = os.environ.get('TRAVIS_DART_VERSION')
    GO_VERSION = os.environ.get('TRAVIS_GO_VERSION')
    HAXE_VERSION = os.environ.get('TRAVIS_HAXE_VERSION')
    JDK_VERSION = os.environ.get('TRAVIS_JDK_VERSION')
    JULIA_VERSION = os.environ.get('TRAVIS_JULIA_VERSION')
    NODE_VERSION = os.environ.get('TRAVIS_NODE_VERSION')
    OTP_RELEASE = os.environ.get('TRAVIS_OTP_RELEASE')
    PERL_VERSION = os.environ.get('TRAVIS_PERL_VERSION')
    PHP_VERSION = os.environ.get('TRAVIS_PHP_VERSION')
    PYTHON_VERSION = os.environ.get('TRAVIS_PYTHON_VERSION')
    R_VERSION = os.environ.get('TRAVIS_R_VERSION')
    RUBY_VERSION = os.environ.get('TRAVIS_RUBY_VERSION')
    RUST_VERSION = os.environ.get('TRAVIS_RUST_VERSION')
    SCALA_VERSION = os.environ.get('TRAVIS_SCALA_VERSION')
    MARIADB_VERSION = os.environ.get('TRAVIS_MARIADB_VERSION')
    XCODE_SDK = os.environ.get('TRAVIS_XCODE_SDK')
    XCODE_SCHEME = os.environ.get('TRAVIS_XCODE_SCHEME')
    XCODE_PROJECT = os.environ.get('TRAVIS_XCODE_PROJECT')
    XCODE_WORKSPACE = os.environ.get('TRAVIS_XCODE_WORKSPACE')
