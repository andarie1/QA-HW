from comp_empl_api_common import CompanyApi, EmployeeApi

if __name__ == "__main__":
# Обновление сотрудника
    company_api = CompanyApi("http://5.101.50.27:8000")
    token = company_api.get_token("harrypotter", "expelliarmus")
    employee_api = EmployeeApi("http://5.101.50.27:8000")
    response = employee_api.change_employee(employee_id=3, token=token)
    for k, v in response.items():
        print(k, v)

    new_company = company_api.create_company("Hogwarts", "Школа магии")
    assert "id" in new_company, "Ошибка: В ответе нет ID компании"
    company_id = new_company["id"]

# Создание сотрудника
    new_employee = employee_api.create_employee(company_id)

    assert new_employee["first_name"] == "Иван", "Ошибка: Имя сотрудника не совпадает"
    assert new_employee["email"] == "ivan@example.com", "Ошибка: Email не совпадает"
    assert new_employee["company_id"] == company_id, "Ошибка: Неверный company_id"

    employee_id = new_employee["id"]

# Получение информации о сотруднике
    employee_info = employee_api.get_employee(employee_id)
    assert employee_info["id"] == employee_id, "Ошибка: ID сотрудника не совпадает"
    assert employee_info["email"] == "ivan@example.com", "Ошибка: Email не совпадает"
    assert employee_info["company_id"] == company_id, "Ошибка: company_id не совпадает"

    print("✅ Все проверки пройдены")




