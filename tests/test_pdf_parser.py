from worker.pdf_parser import parse_pdf

def test_parse_pdf():

    result = parse_pdf(
        "tests/files/README.pdf"
    )

    assert result is not None
    assert "pages" in result