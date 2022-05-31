import bisect


farm = sorted(["haystack", "needle", "cow", "pig"])
print(farm)
r = bisect.bisect(farm, "needle")
print("needle", r, farm)
r = bisect.bisect_left(farm, "chicken")
print("chicken", r, farm)
r = bisect.bisect(farm, "eggs")
print("eggs", r, farm)
r = bisect.bisect_left(farm, "eggs")
print("eggs", r, farm)

print("-" * 64)

print(farm)
bisect.insort(farm, "eggs")
print(farm)
bisect.insort(farm, "turkey")
print(farm)
