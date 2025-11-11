T=('cat','cow','crow','dog','dog','elephant','cow','cow')
repeated=[item for item in set(T)if T.count(item)>1]
print("repeated tuple:",repeated)
