from composeenvcheck.report import generate_report

def test_generate_report():
    referenced = {"A", "B", "C"}
    defined = {"A": "1", "D": "2"}
    missing, unused = generate_report(referenced, defined)
    assert missing == {"B", "C"}
    assert unused == {"D"}
