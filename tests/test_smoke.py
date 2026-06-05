import importlib
import os

from fastapi.testclient import TestClient

from src.core.config import get_settings


def get_test_client() -> TestClient:
    os.environ["DATABASE_URL"] = "sqlite:///./test.db"
    get_settings.cache_clear()

    import src.core.database as database
    import src.models.pipeline as pipeline_model
    import src.models.run as run_model
    import src.main as main

    # 1. Recargar la base de datos primero (crea un nuevo Base y engine para SQLite)
    importlib.reload(database)

    # 2. Recargar los modelos para que se re-registren en el NUEVO Base
    #    Sin este paso, create_all no conoce la tabla pipeline_runs
    importlib.reload(pipeline_model)
    importlib.reload(run_model)

    # 3. Recargar la app con todo configurado
    importlib.reload(main)

    # 4. Crear las tablas en la base de datos de pruebas SQLite limpia
    database.Base.metadata.drop_all(bind=database.engine)
    database.Base.metadata.create_all(bind=database.engine)

    return TestClient(main.app)


client = get_test_client()


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["estado"] == "Activo"


def test_pipeline_crud():
    create_response = client.post(
        "/pipelines",
        json={"nombre": "demo", "repositorio": "https://github.com/example/repo"},
    )
    assert create_response.status_code == 200
    created = create_response.json()["pipeline"]
    pipeline_id = created["id"]

    list_response = client.get("/pipelines")
    assert list_response.status_code == 200
    assert list_response.json()["total"] >= 1

    get_response = client.get(f"/pipelines/{pipeline_id}")
    assert get_response.status_code == 200

    update_response = client.put(
        f"/pipelines/{pipeline_id}",
        json={"nombre": "demo_actualizado"},
    )
    assert update_response.status_code == 200
    assert update_response.json()["pipeline"]["nombre"] == "demo_actualizado"

    # Test Run Creation
    run_response = client.post(f"/pipelines/{pipeline_id}/runs")
    assert run_response.status_code == 200
    assert run_response.json()["run"]["estado"] == "pendiente"
    
    # Test Run Listing
    runs_list_response = client.get(f"/pipelines/{pipeline_id}/runs")
    assert runs_list_response.status_code == 200
    assert runs_list_response.json()["total"] == 1

    delete_response = client.delete(f"/pipelines/{pipeline_id}")
    assert delete_response.status_code == 200
