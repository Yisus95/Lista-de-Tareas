from pathlib import Path

def test_manage_exists():
    assert Path("src/proyecto/manage.py").exists(), "manage.py should exist at src/proyecto/manage.py"
