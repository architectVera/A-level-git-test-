import os
file_name = 'file_2.txt'
fl = open(file_name, 'r')
output = ""

while True:
    line = fl.readline()
    if not line:
        break
    try:
        output += line.strip() + "=" + str(eval(line)) + os.linesep
    except Exception as e:
        output += line.strip() + "=" + f"Exception has happened, {e=}" + os.linesep
    finally:
        pass
fl.close

with open(file_name, "w") as text_file:
    text_file.write(output)
