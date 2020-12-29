a) The volume of a sphere with radius r is 4/3pr3. What is the volume of a sphere with radius 5?

Hint: 392.7 is wrong!





pi=3.14

radius=float(input("Enter the radius : "))

v=4/3*pi*radius*radius*radius

print("The volume of the sphere is : " ,v)



-------------------------



b)Suppose the cover price of a book is Rs.24.95, but bookstores get a 40% discount. Shipping costs

Rs.3 for the first copy and 0.75p for each additional copy. What is the total wholesale cost for

60 copies?





book_price=24.95

discount=0.4

first_copy_cost=3.0

additional_copy_cost=0.75

total_book=60



single_book_price=book_price*discount

sale_price=book_price-single_book_price



first_copy=sale_price+first_copy_cost

additional_copy=sale_price*59+additional_copy_cost*59



print("The additional copy price is " ,additional_copy)

print("The first copy price is  ",first_copy)

print("The total whole sale cost is ",additional_copy+first_copy)



----------------------------



c)If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at

tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?



starttimehr = 6 + (52 / 60.0)

easypacehr = (8 + 15 / 60.0 ) / 60.0

tempopacehr = (7 + 12 / 60.0) / 60.0

runtimehr = 2 * easypacehr + 3 * tempopacehr

breakfasthr = starttimehr + runtimehr

breakfastmin = (breakfasthr-int(breakfasthr))*60

breakfastsec= (breakfastmin-int(breakfastmin))*60

print ('Finish time was %d:%d' % (breakfasthr,breakfastmin))



