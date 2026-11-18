from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_calculate_bonus():
    response = client.get("/employee/bonus")

    assert response.status_code == 200
    assert response.json()["bonus"] == 5000.0


def test_get_existing_employee():
    response = client.get("/employee/101")

    assert response.status_code == 200
    assert response.json()["name"] == "Rahul"


def test_get_missing_employee():
    response = client.get("/employee/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Employee 999 not found"


def test_average_salary():
    response = client.get(
        "/employee/average-salary",
        params={"total_salary": 150000, "employee_count": 3},
    )

    assert response.status_code == 200
    assert response.json()["average_salary"] == 50000.0


def test_zero_employee_count():
    response = client.get(
        "/employee/average-salary",
        params={"total_salary": 150000, "employee_count": 0},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Employee count must be greater than zero"