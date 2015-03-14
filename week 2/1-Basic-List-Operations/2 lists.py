languages = ["Python", "Ruby"]

languages = languages + ["C++", "Java", "C#"]

languages = ["Haskell"] + languages

languages = languages + ["Go"]

print(languages[0])
print(languages[1])
print(languages[4])

languages[5] = "F#"

print(languages[6])

last_element = len(languages) - 1

print(languages[last_element])

if "Haskell" in languages:

    print(True)

else:

    print(False)

if "Ruby" in languages:

    print(True)

else:

    print(False)

if "Go" in languages:

    print(True)

else:

    print(False)

if "Rust" in languages:

    print(True)

else:

    print(False)



