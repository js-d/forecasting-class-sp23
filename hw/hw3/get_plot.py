from datetime import datetime, timedelta
import matplotlib.pyplot as plt

l = [
    1714280,
    1070691,
    1632406,
    1555773,
    1198339,
    1059741,
    1397281,
    1648529,
    1241792,
    1514369,
    1471161,
    1201583,
    1301462,
    1699242,
    1379403,
    1403734,
    1728383,
    1541835,
    1231419,
    1125952,
    1449550,
    1693518,
    1449698,
    1502714,
    1533544,
    1493235,
    1666715,
    1916499,
    2023309,
    1616316,
]


def date_range(start, end):
    delta = end - start  # as timedelta
    days = [start + timedelta(days=i) for i in range(delta.days + 1)]
    return days


start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 1, 30)

# t_values = date_range(start_date, end_date)
t_values = list(range(1, 31))

tsa_values = l
tsa_values.reverse()

fig, ax = plt.subplots()
ax.plot(t_values, tsa_values)
ax.set_title("TSA checkpoint travel numbers in January 2022")
ax.set_xlabel("Date")
ax.set_ylabel("TSA checkpoint travel numbers")
fig.savefig("tsa_checkpoint.png")
