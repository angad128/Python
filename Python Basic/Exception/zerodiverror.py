while True:
    try:
        x = int(input("Enter your number"))
        print(100/x)
        break
    except ValueError:
        print("make sure you have enter integer value.")
    except ZeroDivisionError:
        print("A number Cannot be divided by 0")
    except:
        break
    finally:
        print("loop complete")