from filesys import FileSystem

if __name__ == "__main__":
    fs = FileSystem()


    while True:
        print("Current directory:", fs.get_current_path())
        command = input("$ ").split(" ")
        operation = command[0]
        args = command[1:]

        if operation == "mkdir":
            print(fs.mkdir(*args))
        elif operation == "cd":
            print(fs.cd(*args))
        elif operation == "ls":
            print(fs.ls(*args))
        elif operation == "grep":
            print(fs.grep(*args))
        elif operation == "cat":
            print(fs.cat(*args))
        elif operation == "touch":
            print(fs.touch(*args))
        elif operation == "echo":
            text, file = " ".join(args[:-1]), args[-1]
            print(fs.echo(text, file))
        elif operation == "mv":
            src, dest = args
            print(fs.mv(src, dest))
        elif operation == "cp":
            if len(args) == 1:
                src = dest = args[0]
            else:
                src, dest = args
            print(fs.cp(src, dest))
        elif operation == "rm":
            print(fs.rm(*args))
        elif operation == "load_state":
            if args:
                fs.load_state(args[0])
            else:
                print("Please provide a file name")
        elif operation == "exit":
            if len(args) >= 2 and args[0] == "save":
                fs.save_state(args[1])
            break
        else:
            print("Invalid command")
