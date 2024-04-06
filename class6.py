# #VARIABLES
# my_name = 'Achimugu Emmanuel'

# my_score = 45

# my_age = 62

# class_average = 50.50 

# passed = False

# my_scores = [45, 60, 38, 73, 85, 50.5, 0]


# #processing data
# my_sum = my_age + my_score

# # display information
# # print(my_sum)

# # print(my_scores[3])

# # LOOPING

# # for score in my_scores:
# #     print(score)
    


# # for sc in my_scores:
# #     if sc == class_average:
# #         print(sc) 
    

# for x in my_name:
#     if x == 'A' or x == 'm':
#         print(x)
    

# # print(len(my_name))



# if my_name == 'Achimgu Emmanuel' and my_age <= 62:
#     print('you are old')
# else:
#     print('you are young')


# my_balance = 120000

# min_balance = 5000

# to_withdraw = 116000

# can_withdraw = to_withdraw - my_balance


if can_withdraw > 0:
    print('you can withdraw')
elif  can_withdraw == 0:
    print('cannot withdraw')
elif can_withdraw < 5000:
    print('on minimum balance')
else:
    print('insuffucient Fund')


emma = 50
james = 40
samuel = 80
mohd = 35
samson = 2

scores = [ 
    james,
    samuel,
    mohd,
    samson
]

max_number = 0

for x in scores:
    if x > max_number:
        max_number = x

print(max_number)


