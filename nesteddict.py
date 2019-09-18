x={"java":{"sprint":90, "sturts":70, "jsf":55},
"python":{"django":95, "flask":75, "pyramid":60},
"hadoop":{"hive":90, "pig":89, "sqoop":86}}
print(x)
for k,v in x.items():
    print(k)
    print("______")
    for p,q in v.items():
        print(p,q)
