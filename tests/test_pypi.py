from changelogs.pypi import get_releases


def test_get_releases():
    data = {
        "releases": {
            "4.5.0": [],
            "4.1.0": [],
            "4.4.4": [],
        },
    }
    expected = ['4.5.0', '4.4.4', '4.1.0']
    assert expected == get_releases(data)
