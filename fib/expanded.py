def expand(num):
    ans = []
    zeros = []
    num = list(num)
    idx = len(num)
    for x in num:
        if x != "0":
            count = 0
            ans.append(num)
            while count < idx:
                zeros.append("0")
                count+=1
                zeros.join(zeros)
        else:
            num.remove("0")
            zero = "0"
            print(num)

expand("100")

#put number into a list
#count index value and add zeros for every place in index
#remove number when used to lower index
#join the new values
