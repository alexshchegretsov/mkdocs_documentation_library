abs = "Alex"

def a():
    abs = "in a()"

    def b():
        abs = "in b()"
        print(abs)
        print("locals b() ",locals())
        print("globals in b() ", globals())
    print("locals a() " ,locals())
    b()

if __name__ == "__main__":
    a()
