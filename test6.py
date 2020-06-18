def gotInfo():
    var1 = input("Pleae peovide the first numeric value: ")
    var2 = input("Please provide the second numeric value: ")
    return(var1,var2):



def compute(var1,var2):
    go = True
    while go:
        var1, var2 = get info()
    try:
        var3 = int(var1) + int(var2)
        print("{} + {} = {}".format(var1,var2,var3))
        go = False
    except ValueError as e:
        print("{}: \n\You did not provide a numeric value!".format(e))
    except:
        print("\n\Oops, you provided invalid input, program will close now!")
    print("{} + {} = {}".format(var1,var2,var3))
        
    """finally:
        print("Moving on...")"""

if __name__ == "__main__":
    getInfo()
