import random
def isCheck(sum):
    if 121 <= sum <= 140:
        return True
    elif 141 <= sum <= 160:
        return True
    else:
        return False

    return False


lottoNumbers = []
for i in range(45):
    lottoNumbers.append(i + 1)
# print(lottoNumbers)

sum = 0
sortArr = random.sample(lottoNumbers, 6)

for a in range(5):
    while True:
        for i in sortArr:
            sum += i
        # print(sum)
        if isCheck(sum):
            break
        else:
            sortArr = random.sample(lottoNumbers, 6)
            sum = 0
    sortArr.sort()
    # print(sum)
    print(sortArr, " sum=", sum)
    sortArr = random.sample(lottoNumbers, 6)
