"""Unit tests for `scitex_str._print._printc` (mirrors `src/scitex_str/_print/_printc.py`)."""

from scitex_str._print import print_debug, printc


def test_printc_writes_message_to_stdout(capsys):
    # Arrange
    message = "hello"
    # Act
    printc(message)
    # Assert
    assert message in capsys.readouterr().out


def test_printc_stdout_is_byte_exact_bordered_block(capsys):
    # Arrange — uncolored so the expected bytes are fully literal
    border = "-" * 40
    # Act
    printc("hello", c=None)
    # Assert — same bytes the builtin print() produced (trailing newline)
    assert capsys.readouterr().out == f"\n{border}\nhello\n{border}\n\n"


def test_printc_accepts_color_keyword_without_error(capsys):
    # Arrange
    message = "colored"
    # Act
    printc(message, c="red")
    # Assert
    assert message in capsys.readouterr().out


def test_print_debug_emits_debug_mode_banner(capsys):
    # Arrange
    # (no inputs — print_debug() prints a fixed banner)
    # Act
    print_debug()
    # Assert
    assert "DEBUG MODE" in capsys.readouterr().out
