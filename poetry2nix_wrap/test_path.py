import subprocess
import sys


def test_python_path():
    expected = sys.executable
    sub_exec = subprocess.run(['python', '-c', 'import sys;print(sys.executable)'], check=True, stdout=subprocess.PIPE, encoding="utf8").stdout.strip()
    assert expected == sub_exec
