def gen_AB():
    print("start")
    yield "A"
    print("continue")
    yield "B"
    print("end")


res1 = [x * 3 for x in gen_AB()]
print(res1)

for i in res1:
    print("-->", i)

res2 = (x * 3 for x in gen_AB())
for i in res2:
    print(i)
