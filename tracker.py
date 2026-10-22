def list_applications(applications: list) -> None:
    for apps in applications:
        print(f"{apps['company']} - {apps['role']} - {apps['status']}")

def update_application_status(applications, company_check, new_status):
    for app in applications:
        if app["company"] == company_check:
            app["status"] = new_status
            return True
    return False

def delete_application(applications, company_name):
    for app in applications:
        if company_name == app["company"]:
            applications.remove(app)
            return True
    return False

def add_application(applications: list, company: str, role: str, status:str) -> None:
    new_application = {
        "company": company,
        "role": role,
        "status": status
        }
    applications.append(new_application)




applications = [{
    "company": "Microsoft",
    "role": "Software Engineer Intern",
    "status": "Applied"

}, {
    "company": "Google",
    "role": "Backend Engineer",
    "status": "Not Applied"


}, {
    "company": "MongoDB",
    "role": "Fullstack Intern",
    "status": "Not Applied"


}]


print("1. View applications")
print("2. Add application")
print("3. Update application")
print("4. Delete application")
print("5. Quit")

if __name__ == "__main__":
    while True:
        choice = input("Choice: ")
        if choice == "1":
            list_applications(applications)

        elif choice == "2":
            print("Add application selected")
            company = input("Company:")
            role = input("Role: ")
            status = input("Status: ")
            add_application(applications, company, role, status)
            list_applications(applications)
            
        elif choice == "4":
            company_name = input("Company: ")
            result = delete_application(applications, company_name)
            if result:
                print("Application deleted.")
            else:
                print("Company not found.")
        
        elif choice == "5":
            print("Exited.")
            break
        
        elif choice == "3":
            company_check = input("Company: ")
            new_status = input("New status: ")
            result = update_application_status(applications, company_check, new_status)
            if result:
                print("Application updated.")
            else:
                print("Company not found.")

        else:
            print("invalid input")
    



        
