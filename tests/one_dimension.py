import mip

MAP_SIZE=100
COVERAGE_DIST=7
map = MAP_SIZE*[0]

map[20]=1
map[50]=1
map[60]=1
map[75]=1
map[90]=1

m = mip.Model()

x = [m.add_var(var_type="B") for i in map]

m.objective = mip.minimize(mip.xsum(x))


for i in range(len(map)):
    if map[i]==1:
        m += mip.xsum([x[j]*(0<abs(i-j)<=COVERAGE_DIST) for j in range(len(x))]) >= 1

m.optimize()

for i in range(len(x)):
    if x[i].x == 1:
        print(i,end=" ")

print()