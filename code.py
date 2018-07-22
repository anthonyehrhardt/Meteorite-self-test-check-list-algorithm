while True:
    ı=input(str("If you find stones, extreme heat, radioactive, fossils in it and you can break it, is there at least one of them?,'y' for yes, 'n' for no:"))
    if ı=="y":
        print("Unfortunately, the stone you find is not a meteorite")
        break
    else:
        print("your meteorite test is starting please try to give correct answers to your questions")
        while True:
            a=input(str("İs a magnet attracted to it ?,'y' for yes, 'n' for no:"))
            if a=="y"or"n":
                b=input(str("İs it heavier than other rocks ?,'y' for yes, 'n' for no:"))
                if b=="y":
                    c=input(str("it have the color look like steel?,'y' for yes, 'n' for no:"))
                    if c=="y":
                        s=input(str("stone surface is have any holes ?,'y' for yes, 'n' for no:"))
                        if s=="y":
                            print("it is not a meteorite you find")
                            break
                        else:
                            h=input(str("Does it have regmaglypts?,'y' for yes, 'n' for no:"))
                            if h=="y":
                                print("I think you found a meteorite")
                                break
                            else:
                                f=input(str("Did you see it fall?,'y' for yes, 'n' for no:"))
                                if f=="y":
                                    print("it is not a meteorite you find")
                                    break
                                else:
                                    print("you do not seem so sure about the answers you give, think well ...")
                                    break
                    else:
                        print("it is not a meteorite you find")
                        break
                else:
                    d=input(str("Has a dark thin crust outside ?,'y' for yes, 'n' for no:"))
                    if d=="y":
                        e=input(str("Are there any metallic, reddish regions in the stone inside ?,'y' for yes, 'n' for no:"))
                        g=input(str("Are there bright regions in the stone?,'y' for yes, 'n' for no"))
                        if g=="y":
                            print("I think you found a meteorite")
                            break
                        if e=="y":
                            h=input(str("Does it have regmaglypts?,'y' for yes, 'n' for no:"))
                            if h=="y":
                                print("I think you found a meteorite")
                                break
                            else:
                                f=input(str("Did you see it fall?,'y' for yes, 'n' for no:"))
                                if f=="y":
                                    print("it is not a meteorite you find")
                                    break
                                else:
                                    print("you do not seem so sure about the answers you give, think well ...")
                                    break
                        else:
                            print("it is not a meteorite you find")
                            break
                    else:
                        f=input(str("Did you see it fall?,'y' for yes, 'n' for no:"))
                        if f=="y":
                            print("it is not a meteorite you find")
                            break
                        else:
                            print("you do not seem so sure about the answers you give, think well ...")
                            break
                
            else:
                print("you made the wrong choice, exiting...")
                break
t=input("press a key to close:")

