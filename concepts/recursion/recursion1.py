count = 0
def func1():
    global count
    if(count==3):
        return
    print(count)
    count+= 1
    func1()

def main():
    func1()

if __name__ == "__main__":
    main()