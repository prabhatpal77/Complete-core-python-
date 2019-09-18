# distionary type with list type..
x={"java":["spring","sturts","jsf"],
"python":["django","flask","pyramid"],
"hadoop":["hive","pig","sqoop"]}
print(x)
for k,v in x.items():
    print(k)
    print("____")
    for p in v:
        print(p)
