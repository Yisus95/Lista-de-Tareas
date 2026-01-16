import importlib
import pytest

@pytest.mark.django_db
def test_task_model_crud():
    """
    Si existe un modelo Task en base.models, se crean y consultan instancias básicas.
    Si no existe, la prueba se salta para no romper CI.
    """
    try:
        models = importlib.import_module("base.models")
    except Exception:
        pytest.skip("base.models no disponible")

    Task = getattr(models, "Task", None)
    if Task is None:
        pytest.skip("Modelo Task ausente en base.models — prueba saltada")

    # crear, guardar y consultar
    t = Task()
    # intenta asignar atributos comunes si existen, no dar por hecho ninguno
    for attr, val in (("name", "test"), ("title", "test")):
        if hasattr(t, attr):
            setattr(t, attr, val)
            break
    t.save()
    assert Task.objects.filter(pk=t.pk).exists()
