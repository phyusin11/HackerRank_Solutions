
s = input()
print(''.join(sorted(s, key=lambda x: (x.isdigit() and int(x)%2==0, x.isdigit(), x.isupper(), x.islower(), x))))


# low = sorted(list(filter(lambda x: x.islower(), characters)))
# upper = sorted(list(filter(lambda x: x.isupper(), characters)))
# odd = sorted(list(filter(lambda x: x.isdigit() and int(x)%2!=0, characters)))
# even = sorted(list(filter(lambda x: x.isdigit() and int(x)%2==0, characters)))
# print("".join(low+upper+odd+even))