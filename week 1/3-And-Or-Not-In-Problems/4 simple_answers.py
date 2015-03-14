a = input ("Type a text" + "\n")

if "hello" in a or "Hello" in a:
    
    print("Hello there, good stranger!")
    
elif "how are you?" in str(a):
    
    print("I am fine, thanks. How are you?")
    
elif "feelings" in str(a):
    
    print("I am a machine. I have no feelings")
    
elif "age" in str(a):
    
    print("I have no age. Only current timestamp")

else:

    print("I do not understand your talk")


