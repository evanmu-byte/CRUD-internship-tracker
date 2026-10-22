from tracker import add_application, update_application_status, delete_application, list_applications

def test_add_application():
    test_list = []
    add_application(test_list, "Radiant", "SWE Intern", "Applied")
    assert test_list == [{"company": "Radiant", "role": "SWE Intern", "status": "Applied" }]






def test_update_application_found():
    test_list = [{
    "company": "Microsoft",
    "role": "Software Engineer Intern",
    "status": "Applied"
}]
    result = update_application_status(test_list, "Microsoft", "Interview")
    assert test_list == [{
    "company": "Microsoft",
    "role": "Software Engineer Intern",
    "status": "Interview"
}]
    assert result is True

def test_update_application_not_found():
    test_list = [{
    "company": "Microsoft",
    "role": "Software Engineer Intern",
    "status": "Interview"}]

    result = update_application_status(test_list, "Google", "Interview")
    assert test_list == [{
    "company": "Microsoft",
    "role": "Software Engineer Intern",
    "status": "Interview"
}]
    assert result is False






def test_delete_application_found():
    test_list = [
        {
            "company": "Microsoft",
            "role": "Software Engineer Intern",
            "status": "Applied"
        }
    ]

    result = delete_application(test_list, "Microsoft")

    assert result is True
    assert test_list == []


def test_delete_application_not_found():
    test_list = [
        {
            "company": "Microsoft",
            "role": "Software Engineer Intern",
            "status": "Applied"
        }
    ]

    result = delete_application(test_list, "Google")

    assert result is False
    assert test_list == [
        {
            "company": "Microsoft",
            "role": "Software Engineer Intern",
            "status": "Applied"
        }
    ]