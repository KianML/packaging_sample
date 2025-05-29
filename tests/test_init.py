from main import print_msg

def test_print_msg(capsys):
    print_msg()
    captured = capsys.readouterr()
    assert captured.out == 'This is my pip package!\n'
    assert captured.err == ''
