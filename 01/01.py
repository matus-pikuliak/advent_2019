print(
    sum(
        int(line) // 3 - 2
        for line
        in open('input')
    )
)
