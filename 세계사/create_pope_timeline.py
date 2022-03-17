import pandas as pd


TEMPLATE_PREIX = """
```mermaid
gantt
    dateFormat YYYY-MM-DD
    axisFormat %Y
"""


def dateformat(s):
    if s[-1] == ".":
        s = s[:-1]
    s = list(s.split("."))
    while len(s[0]) < 4:
        s[0] = "0" + s[0]
    s = "-".join(s)
    return s


def main():
    p = "역대교황_나무위키.csv"
    df = pd.read_csv(p)

    res = TEMPLATE_PREIX
    for idx, row in df.iterrows():
        if "세기" in row["대수"]:
            res += "\n    section %s" % (row["대수"],)
            continue
        즉위 = row["즉위년일"]
        즉위 = dateformat(즉위)
        퇴위 = row["퇴위년일"]
        퇴위 = dateformat(퇴위)
        res += "\n    %s: %s, %s" % (row["교황명"], 즉위, 퇴위)
    res += "\n```"

    with open("역대교황연표.md", "w", encoding="utf-8") as f:
        f.write(res)


if __name__ == "__main__":
    main()
