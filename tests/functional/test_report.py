import pytest

from pages.article import ArticlePage

ARTICLE_PATH = 'docs/User:anonymous:uitest'
ARTICLE_NAME = 'User:anonymous:uitest'
ARTICLE_TITLE_SUFIX = " | MDN"


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_report_content(base_url, selenium):
    page = ArticlePage(selenium, base_url, path=ARTICLE_PATH).open()
    assert page.header.is_feedback_submenu_trigger_displayed
    assert not page.header.is_feedback_submenu_displayed
    page.header.show_feedback_submenu()
    assert page.header.is_report_content_link_displayed
    # store url of reporting page
    report_url = selenium.current_url
    page.header.open_report_content()
    # bugzilla loads in new window
    selenium.switch_to_window(selenium.window_handles[1])
    # check form loaded
    assert page.header.is_report_content_url_expected(selenium, report_url)


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_report_bug(base_url, selenium):
    page = ArticlePage(selenium, base_url, path=ARTICLE_PATH).open()
    assert page.header.is_feedback_submenu_trigger_displayed
    assert not page.header.is_feedback_submenu_displayed
    page.header.show_feedback_submenu()
    assert page.header.is_report_bug_link_displayed
    page.header.open_report_bug()
    # check form loaded
    assert page.header.is_report_bug_url_expected(selenium)
