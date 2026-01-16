def test_settings_loads():
    import importlib
    mod = importlib.import_module("proyecto.settings")
    # assert at least that INSTALLED_APPS exists
    assert hasattr(mod, "INSTALLED_APPS")
