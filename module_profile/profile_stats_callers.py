import cProfile as profile
import pstats
from profile_fibonacci_memoized import fib, fib_seq

stats = pstats.Stats('profile_stats_0.stats')
for i in range(1, 5):
    stats.add(f'profile_stats_{i}.stats')

# cleanup filenames for the report
stats.strip_dirs()

# sort the statistics by the cumulative time spent in the function
stats.sort_stats('cumulative')


print('INCOMING CALLERS:')
stats.print_callers(r'\(fib')

print('OUTGOING CALLEES:')
stats.print_callees(r'\(fib')
