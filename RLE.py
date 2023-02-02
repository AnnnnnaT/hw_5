def rle (text: str):
    res = ""
    count= 1
    for i in range(len(text)-1):
        
        if text[i] == text[i+1]:
            count+=1
        else:
            res+=(str(count))
            res+=(text[i])
            count = 1
    res+=(str(count))+text[len(text)-1]
       
    return res
    
# a = input('Input text to compress: ')
# print(rle(a))

def decom (text: str) -> str:
    string = ''
    for i in range(len(text)-1):
        if i%2==0:
            a = int(text[i]) * text[i+1]
            string+=a
    return string

# b = (input('Text to decompress: '))
# print(decom(b))

with open("rle1.txt", 'r') as data:
    s = data.readlines()
    res = rle(s[0])
    res2 = decom(s[1])
    with open("rle2.txt", "w") as file:
        file.write(res)
        file.write(res2)
        # file.write(res2)

# with open("rle2.txt", "r") as s:
#     output = s.read()
