from my_sample_package import print_test


def test_print_test(capsys):
    print_test()
    captured = capsys.readouterr()
    assert captured.out == 'This is my pip package!\n'
    assert captured.err == ''
