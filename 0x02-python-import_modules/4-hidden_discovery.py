#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for name in hidden_4:
        if name[0:2] != "__":
            print(name)
