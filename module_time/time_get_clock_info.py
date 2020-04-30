import textwrap
import time


available_clocks = [
    # The monotonic() clock can be used to measure elapsed time in a long-running process
    ('monotonic', time.monotonic),
    # For performance testing, perf_counter() provides access to the clock with the highest available resolution
    # to make short time measurements more accurate.
    ('perf_counter', time.perf_counter),
    # process_time() returns the combined processor time and system time.
    ('process_time', time.process_time),
    ('time', time.time),
]


for clock_name, func in available_clocks:
    print(
        '''
        {name}:
            adjustable: {info.adjustable}
            implementation: {info.implementation}
            monotonic: {info.monotonic}
            resolution: {info.resolution}
            current: {current}
        '''.format(
            name=clock_name,
            info=time.get_clock_info(clock_name),
            current=func()
        )
    )

