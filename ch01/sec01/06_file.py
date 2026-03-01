# File I/O
f = open("example.txt", "w", encoding="utf8") # write
f.write("첫째 줄\n")
f.write("둘째 줄\n")
f.write("셋쨰 줄\n")
f.close()

f = open("example.txt", "r", encoding="utf8") # read
content = f.read()
print(content)
f.close()