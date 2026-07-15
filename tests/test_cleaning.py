from src.text_cleaner.cleaning import remove_extra_spaces


def test_remove_extra_spaces():
    assert remove_extra_spaces("  ciao    mondo  ") == "ciao mondo"
    assert remove_extra_spaces("ciao") == "ciao"
    assert remove_extra_spaces("") == ""
    assert remove_extra_spaces("   ") == ""