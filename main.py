def recurs(n, start, work, target):
    if n == 1:
        print(f"{start}에서 원반{n}를(을) {target}으로 옮김")
    else:
        recurs(n - 1, start, target, work)
        print(f"{start}에서 원반{n}를(을) {target}으로 옮김")
        recurs(n - 1, work, start, target)


if __name__ == '__main__':
    recurs(3, '시작봉', '작업봉', '목적봉')
