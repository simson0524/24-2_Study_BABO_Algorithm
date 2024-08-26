n = int(input())

meetings = dict()
end_time = []

for _ in range(n):
    start, end = map(int, input().split())
    if end in meetings:
        meetings[end].append(start)
    else:
        meetings[end] = [start]
        end_time.append(end)

end_time = set(end_time)
end_time = list(end_time)
end_time = sorted(end_time)

for key, value in meetings.items():
    meetings[key] = sorted(value)

curr_end_time = 0
meetings_avail =0

for END in end_time:
    if END >= curr_end_time:
        for START in meetings[END]:
            if START >= curr_end_time:
                meetings_avail += 1
                curr_end_time = END

print(meetings_avail)
