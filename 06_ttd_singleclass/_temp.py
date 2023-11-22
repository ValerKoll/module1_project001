def facorial(n):
    product = n
    while n > 1:
        n -= 1
        product *= n
    return product

print(facorial(5))
    
    
    
    

# di = {
#     '1':{'Title':'tes', 'content':'ssss','completed':True},
#     '2':{'Title':'no', 'content':'ddddd','completed':False}
# }

# d = [(f"{key} --- {i['Title'].upper()}: {i['content']}\n") for key, i in di.items() if i['completed']==True]
# print(''.join(d))

