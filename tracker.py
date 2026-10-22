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
def list_applications(applications: list) -> None:
    for apps in applications:
        print(f"{apps['company']} - {apps['role']} - {apps['status']}")

def add_application(applications: list, company: str, role: str, status:str) -> None:
    new_application = {
        "company": company,
        "role": role,
        "status": status
        }
    applications.append(new_application)

print("1. View applications")
print("2. Add application")
print("3. Update application")
print("4. Delete application")
print("5. Quit")


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

    elif choice == "3":
        found = False
        company_check = input("Company: ")
        new_status = input("Status: ")
        for app in applications:
            if app["company"] == company_check:
                app["status"] = new_status
                found = True
                break
        if not found:
            print("Application not found.")
        
    elif choice == "4":
        found = False
        delete_company = input("Company: ")
        for app in applications:
            if delete_company == app["company"]:
                found = True
                applications.remove(app)
                print("Application deleted.")
                break
        if not found:
            print("Application not found.")
    
    elif choice == "5":
        print("Exited.")
        break
    


    else:
        print("invalid input")
        
