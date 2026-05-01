"""scitex-str quickstart: string formatting and search helpers."""

import scitex_str


def main():
    # 1. printc — coloured terminal print (also returns rendered string).
    scitex_str.printc("hello world", c="green")

    # 2. readable_bytes — pretty byte sizes.
    print("readable_bytes(1500):", scitex_str.readable_bytes(1500))
    print("readable_bytes(2**30):", scitex_str.readable_bytes(2**30))

    # 3. squeeze_spaces — collapse runs of spaces.
    out = scitex_str.squeeze_spaces("a   b   c")
    print("squeeze_spaces:", out)
    assert out == "a b c"

    # 4. title_case — capitalise words, ignoring stopwords.
    print("title_case:", scitex_str.title_case("a tale of two cities"))

    # 5. clean_path — collapse path separators.
    print("clean_path:", scitex_str.clean_path("/tmp//foo/./bar"))


if __name__ == "__main__":
    main()
