pledges = ["Never gonna give you up",
           "Never gonna let you down",
           "Never gonna run around and desert you",
           "Never gonna make you cry",
           "Never gonna say goodbye",
           "Never gonna tell a lie and hurt you",
           "Never gonna stop"]
N = int(input())
pledgesCheck = "No"
for _ in range(N):
    pledge = input().rstrip()
    if pledge not in pledges:
        pledgesCheck = "Yes"
print(pledgesCheck)