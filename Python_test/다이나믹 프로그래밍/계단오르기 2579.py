n = int(input())
stair = []
for i in range(n):
    stair.append(int(input()))

dp = []
dp.append(stair[0])

for i in range(1, 3):
    if i == 1:
        dp.append(max(dp[i-1]+stair[i], stair[i]))
        continue
    dp.append(max(dp[i-2] + stair[i], stair[i-1] + stair[i]))

for i in range(3, n):
    dp.append(max(stair[i] + stair[i -1] + dp[i-3],stair[i] + dp[i-2]))


print(dp[-1])