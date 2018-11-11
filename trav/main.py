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


class TravisVariables(type):
    TRAVIS_BOOLEANS = ('CI',
                       'TRAVIS',
                       'HAS_JOSH_K_SEAL_OF_APPROVAL',
                       'CONTINUOUS_INTEGRATION',
                       'TRAVIS_ALLOW_FAILURE',
                       'TRAVIS_SECURE_ENV_VARS',
                       'TRAVIS_SUDO')

    TRAVIS_VARIABLES = ('DEBIAN_FRONTEND',
                        'USER',
                        'HOME',
                        'LANG',
                        'LC_ALL',
                        'RAILS_ENV',
                        'RACK_ENV',
                        'MERB_ENV',
                        'TRAVIS_BRANCH',
                        'TRAVIS_BUILD_DIR',
                        'TRAVIS_BUILD_ID',
                        'TRAVIS_BUILD_NUMBER',
                        'TRAVIS_BUILD_STAGE_NAME',
                        'TRAVIS_BUILD_WEB_URL',
                        'TRAVIS_COMMIT',
                        'TRAVIS_COMMIT_MESSAGE',
                        'TRAVIS_COMMIT_RANGE',
                        'TRAVIS_EVENT_TYPE',
                        'TRAVIS_JOB_ID',
                        'TRAVIS_JOB_NUMBER',
                        'TRAVIS_JOB_WEB_URL',
                        'TRAVIS_OS_NAME',
                        'TRAVIS_OSX_NAME',
                        'TRAVIS_OSX_IMAGE',
                        'TRAVIS_PULL_REQUEST',
                        'TRAVIS_PULL_REQUEST_BRANCH',
                        'TRAVIS_PULL_REQUEST_SLUG',
                        'TRAVIS_REPO_SLUG',
                        'TRAVIS_SECURE_ENV_VARS',
                        'TRAVIS_TEST_RESULT',
                        'TRAVIS_TAG',
                        'TRAVIS_DART_VERSION',
                        'TRAVIS_GO_VERSION',
                        'TRAVIS_HAXE_VERSION',
                        'TRAVIS_JDK_VERSION',
                        'TRAVIS_JULIA_VERSION',
                        'TRAVIS_NODE_VERSION',
                        'TRAVIS_OTP_RELEASE',
                        'TRAVIS_PERL_VERSION',
                        'TRAVIS_PHP_VERSION',
                        'TRAVIS_PYTHON_VERSION',
                        'TRAVIS_R_VERSION',
                        'TRAVIS_RUBY_VERSION',
                        'TRAVIS_RUST_VERSION',
                        'TRAVIS_SCALA_VERSION',
                        'TRAVIS_MARIADB_VERSION',
                        'TRAVIS_XCODE_SDK',
                        'TRAVIS_XCODE_SCHEME',
                        'TRAVIS_XCODE_PROJECT',
                        'TRAVIS_XCODE_WORKSPACE')

    def __getattr__(self, variable):
        if variable in self.TRAVIS_BOOLEANS:
            return var_is_true(variable)
        elif variable in self.TRAVIS_VARIABLES:
            return os.environ.get(variable)

        raise AttributeError


class Travis(metaclass=TravisVariables):
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
