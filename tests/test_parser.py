from changelogs.parser import get_head, parse


def test_get_head():
    assert "1.1.2" == get_head("django", "Django 1.1.2 release notes", ["1.1.2"])
    assert "4.5.0" == get_head("mayavi", "Mayavi 4.5.0", ["4.5.0"])


# Test that parse removes #'s from .md and .rst formats, but keeps # in urls'
def test_parser():
    test_content = "### 1.2.3\n\n#### Updated changelog - Test url https://www.pyup.io/fake_url#thisection"
    changelog = parse("test_changelog", test_content, ["1.2.3"], get_head)
    assert changelog["1.2.3"] == "\n Updated changelog - Test url https://www.pyup.io/fake_url#thisection\n"
