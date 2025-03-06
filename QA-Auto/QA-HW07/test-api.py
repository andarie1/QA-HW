from comp_empl_api_common import CompanyApi, EmployeeApi

if __name__ == "__main__":
    company_api = CompanyApi("http://5.101.50.27:8000")
    token = company_api.get_token("harrypotter", "expelliarmus")
    employee_api = EmployeeApi("http://5.101.50.27:8000")
    response = employee_api.change_employee(employee_id=2, token=token)
    for k, v in response.items():
        print(k, v)



