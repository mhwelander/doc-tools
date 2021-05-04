import re
import requests


def removeSpaceAfterMessage(match):
    replaced = re.sub(r"\n", " ", match.group(1))
    replaced = re.sub(r"\"\\ ", '"', replaced)
    return replaced


url1 = "https://raw.githubusercontent.com/prisma/prisma-engines/master/libs/user-facing-errors/src/migration_engine.rs"
r1 = requests.get(url1, allow_redirects=True)
open("migration_engine.txt", "wb").write(r1.content)

url2 = "https://raw.githubusercontent.com/prisma/prisma-engines/master/libs/user-facing-errors/src/query_engine.rs"
r2 = requests.get(url2, allow_redirects=True)
open("query_engine.txt", "wb").write(r2.content)

url3 = "https://raw.githubusercontent.com/prisma/prisma-engines/master/libs/user-facing-errors/src/common.rs"
r3 = requests.get(url3, allow_redirects=True)
open("common.txt", "wb").write(r3.content)

url4 = "https://raw.githubusercontent.com/prisma/prisma-engines/master/libs/user-facing-errors/src/introspection_engine.rs"
r4 = requests.get(url4, allow_redirects=True)
open("introspection_engine.txt", "wb").write(r4.content)

#    print(reg4)


for n in [
        ["common.txt", "Common"],
    ["query_engine.txt", "Prisma Client (Query Engine)"],
    ["migration_engine.txt", "Prisma Migrate (Migration Engine)"],
    ["introspection_engine.txt", "<inlinecode>prisma db pull</inlinecode> (Introspection Engine)"],
]:

    print()
    print()
    print("### " + n[1])
    print()

    with open(n[0], "r") as sf4:
        data = sf4.read()

        with open(n[0], "w") as sf5:

            bleh = re.sub(r"((?:message = )[^\]]+)", removeSpaceAfterMessage, data)
            blah = re.sub("\#\[user_facing\(code", "\#\[user_facing\(\ncode", bleh)
            bloh = re.sub(", message \= ", ",\nmessage = ", blah)
            blih = re.sub(
                "\#\[user_facing\(message = ", "\#\[user_facing\(\nmessage = ", bloh
            )

            blup = re.sub("const ERROR_CODE: &'static str = ", "code =", blih)
            blarp = re.sub("format!\(", "message = ", blup)
            foop = re.sub("message = \n", "message =", blarp)

            sf5.write(foop)

    with open(n[0], "r") as fp:

        line = fp.readline()
        cnt = 1
        while line:
            strippedLine = line.strip()
            if strippedLine.startswith("code ="):
                str1 = strippedLine.strip('",')
                str1 = str1.strip(")]")
                str1 = str1.strip('";')
                print()
                print("#### <inlinecode>" + str1.strip('code = "') + "</inlinecode>", end="")                
                print();

            if strippedLine.startswith("message ="):
                str2 = strippedLine.strip(")]")
                print();
                str3 = str2.replace("\\n", "<br />")
                print(str3.strip("message ="), end="")
                print();

            # print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
