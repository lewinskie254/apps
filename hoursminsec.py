import math 

def hoursMinutesSeconds(n):
    if n < 60:
        return f"{math.floor(n)}s"
    elif 60 < n < 3600:
        m = n/60
        s = n%60
        return f"{math.floor(m)}m {math.floor(s)}s"
    elif 3600 < n < 86400:
        h = n/3600
        r = (n)%3600
        m = r/60
        s = r%60
        if m < 1:
            m == 0
        return f"{math.floor(h)}h {math.floor(m)}m {math.floor(s)}s"
    else: 
        d = n/86400
        dr = n%86400
        h = dr/3600
        r = (n)%3600
        m = r/60
        s = r%60
        return f"{math.floor(d)}d {math.floor(h)}h {math.floor(m)}m {math.floor(s)}s"
    


def main():
    n = input("Number of seconds: ")
    if n.isdigit():
        n = int(n)
    result = hoursMinutesSeconds(n)
    print(result)

if __name__ == "__main__":
    main()