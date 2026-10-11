from src.decorators import log


@log("")
def add(a, b):
    return a + b


@log("")
def div(a, b):
    return a / b


@log("addlog.log")
def mult(a, b):
    return a * b


def test_log_console(capsys):
    result = add(1, 2)
    assert result == 3
    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_log_debug_console(capsys):
    result = div(3, 0)
    assert result is None
    captured = capsys.readouterr()
    print("1", captured)
    assert "div : ZeroDivisionError. Inputs: (3, 0), {}" in captured.out


def test_log_file(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def mmult(a, b):
        return a * b

    result = mmult(1, 2)
    assert result == 2
    assert log_file.exists()
    contents = log_file.read_text()
    assert contents.strip() == "mmult ok"
