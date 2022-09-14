import re

if __name__ == "__main__":
    s = "【UPDATE_TIME: 2022-09-13 00:04:46 -> 2022-09-07 01:35:55】【MATERIAL_STATUS: 0(Opted Out) -> 50(Prospect)】"
    p = re.compile(r".*?【MATERIAL_STATUS:.*?(\d+).*? -> (\d+).*?】.*?")
    m = p.match(s)
    print(m.groups())

    s = "【MATERIAL_STATUS: 70(Proposal Send) -> 0(Opted Out)】"
    m = p.match(s)
    print(m.groups())
    print(m.groups()[0], m.groups()[1])
