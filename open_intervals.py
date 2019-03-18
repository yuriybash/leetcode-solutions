"""
We are writing a tool to help users manage their calendars. Given an unordered list of times of day when people are busy, write a function that tells us the intervals during the day when ALL of them are available.

# Sample input:

# p1_meetings = [
#   ( 845, 900),
#   (1230, 1300),
#   (1300, 1500),
# ]
#
# p2_meetings = [
#   ( 930, 1200),
#   (1600, 2359),
# ]
#
# p3_meetings = [
#   ( 845, 915),
#   (1515, 1545),
# ]

# schedules = [p1_meetings, p2_meetings, p3_meetings]

# Expected output:

# find_available_time(schedules)
#  => [    0,  845 ],
#     [  915,  930 ],
#     [ 1200, 1230 ],
#     [ 1500, 1515 ],
#     [ 1545, 1600 ]
"""

import datetime


def find_available_time(meetings):

    if not meetings:
        return []

    reformatted_intervals = []

    for meeting_group in meetings:
        for start, end in meeting_group:
            start_hour, start_minutes = int(str(start)[:-2]), int(str(start)[-2:])
            end_hour, end_minutes = int(str(end)[:-2]), int(str(end)[-2:])

            reformatted_intervals.append([60 * start_hour + start_minutes,
                                          60 * end_hour + end_minutes])

    reformatted_intervals.sort(key=lambda x: x[0])
    merged = [[None, 0]] + merge_intervals(reformatted_intervals) + [[24*60-1]]

    open_slots = []
    for idx in xrange(len(merged)-1):
        if merged[idx+1][0] > merged[idx][1]:
            open_slots.append([merged[idx][1], merged[idx+1][0]])

    ans = []
    for start, end in open_slots:
        start_str = str(datetime.timedelta(seconds=start))
        end_str = str(datetime.timedelta(seconds=end))
        ans.append((start_str[2:4] + start_str[5:],
                    end_str[2:4] + end_str[5:]))
    return ans


def merge_intervals(intervals):

    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(interval[1], merged[-1][1])
    return merged
