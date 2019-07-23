def test_add_button_is_present(browser):
    assert browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket") != null, "No \'add to backet\' button!"