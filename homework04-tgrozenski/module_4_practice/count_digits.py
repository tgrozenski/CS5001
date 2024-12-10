def main():
    assert countDigits(0) == 1
    assert countDigits(12345) == 5
    assert countDigits(123456789) == 9
    assert countDigits(12345678912345678901) == 20
    print("All Good")


def countDigits(num: int):
    if(num == 0):
        return 1
    else:
        # return len(str(num))
        counter: int = 0
        while num > 0:
            num //= 10
            counter += 1
    return counter
    

if(__name__ == "__main__"):
    main()