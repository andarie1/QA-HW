import requests


class CompanyApi:
    def __init__(self, url):
        self.url = url.rstrip('/')

    def get_company_list(self):
        response = requests.get(f"{self.url}/company/list")
        assert response.status_code == 200, response.text
        return response.json()

    def get_token(self, username, password):
        credentials = {"username": username, "password": password}
        response = requests.post(f"{self.url}/auth/login", json=credentials)
        assert response.status_code == 200, response.text
        return response.json()["user_token"]

    def create_company(self, name, description):
        data = {"name": name, "description": description}
        response = requests.post(f"{self.url}/company/create", json=data)
        assert response.status_code == 201, response.text
        return response.json()

    def edit_company(self, company_id, new_name, new_description):
        token = self.get_token("harrypotter", "expelliarmus")
        url = f"{self.url}/company/update/{company_id}?client_token={token}"
        data = {"name": new_name, "description": new_description}
        response = requests.patch(url, json=data)
        assert response.status_code == 200, response.text
        return response.json()

    def get_company(self, company_id):
        response = requests.get(f"{self.url}/company/{company_id}")
        assert response.status_code == 200, response.text
        return response.json()


class EmployeeApi:
    def __init__(self, url):
        self.url = url.rstrip('/')

    def create_employee(self, company_id):
        data = {
            "first_name": "Иван",
            "last_name": "Иванов",
            "middle_name": "Иванович",
            "company_id": company_id,
            "email": "ivan@example.com",
            "phone": "+79990000000",
            "birthdate": "1990-01-01",
            "is_active": True
        }
        response = requests.post(f"{self.url}/employee/create", json=data)
        assert response.status_code == 201, response.text
        return response.json()

    def get_employee(self, employee_id):
        response = requests.get(f"{self.url}/employee/info/{employee_id}")
        assert response.status_code == 200, response.text
        return response.json()

    def change_employee(self, employee_id, token):
        data = {
            "last_name": "Петров",
            "email": "petr@example.com",
            "phone": "+79991112233",
            "is_active": False
        }
        url = f"{self.url}/employee/change/{employee_id}"
        response = requests.patch(url, json=data, params={"client_token": token})
        assert response.status_code == 200, response.text
        return response.json()
