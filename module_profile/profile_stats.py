import cProfile as profile
import pstats
from profile_fibonacci_memoized import fib, fib_seq


for i in range(5):
    filename = "profile_stats_{}.stats".format(i)
    profile.run("print({}, fib_seq(20))".format(i), filename)

stats = pstats.Stats("profile_stats_0.stats")
for i in range(1, 5):
    stats.add(f"profile_stats_{i}.stats")

# cleanup filenames for the report
stats.strip_dirs()

# sort the statistics by the cumulative time spent in the function
stats.sort_stats("cumulative")
stats.print_stats()
