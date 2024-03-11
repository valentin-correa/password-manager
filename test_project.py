from project import get_all, checker, delete_acc, get_specific, add_acc, update_acc

def test_get_all():
    assert get_all() == [('Test_service', 'test_user', 'test_password')]

def test_checker():
    service = "non_existing_service" # A non existing service
    assert checker(service) == False
    service = "Test_service" #A existing service
    assert checker(service) == True

def test_get_specific():
    assert get_specific("Test_service") == [('Test_service', 'test_user', 'test_password')]
    assert get_specific("Fake_service") == "\nSERVICE NOT FOUND\n"


### The following tests have problems with testing because they have prompts inside.

def test_add():
    assert add_acc("Test_service") == "\nSERVICE ALREADY EXISTS\n"

def test_update():
    assert update_acc("Non_existing_service") == "\nSERVICE NOT FOUND\n"

def test_delete():
    assert delete_acc("Non_existing_service") == "\nSERVICE NOT FOUND\n"