cipher_text = input()
dp = [0 for i in range(len(cipher_text) + 1)]

if cipher_text[0] == "0":
    print(0)
else:
    dp[0] = 1
    dp[1] = 1

    for i in range(2, len(dp)):
        one = int(cipher_text[i - 1])
        two = int(cipher_text[i - 2] + cipher_text[i - 1])

        if one > 0:
            dp[i] += dp[i - 1]

        if two >= 10 and two <= 26:
            dp[i] += dp[i - 2]

    print(dp[len(cipher_text)] % 1000000)
