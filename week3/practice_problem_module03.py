def default_value(name: str = "Tyler", salary: int = 9000) -> str:
    return f"Name: {name}, Salary: {salary}"

def test_default_value(formatted_str: str, name: str, salary: int) -> None:
    try:
        if name == None and salary == None:
            assert formatted_str == "Name: Tyler, Salary: 9000" 
            print("Passed", formatted_str)
        else:
            assert formatted_str == f"Name: {name}, Salary: {salary}"
            print("Passed", formatted_str)
    except AssertionError: 
        print("Test Failed", formatted_str)
    return

def main():
    test_default_value(default_value(), None, None)
    test_default_value(default_value("Steve", 100000), "Steve", 100000)

if __name__ == "__main__":
    main()