# Practice using the Python interpreter as a calculator / Volume of Sphere
# 2.2.1 Volume of a Sphere
r = 5.0;
pi = 3.14159265;
volumeSphere = 4 / 3 * pi * r**3;

print('Volume of Sphere = ', volumeSphere);

# 2.2.2 Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
# $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
# 60 copies?

bookPrice = 24.95;
bookStoreDiscount = 0.4; #40% discount
shippingCostsFirstCopy = 3;
shippingCostAdditional = 0.75;
noOfCopies = 60;

shippingCosts = shippingCostsFirstCopy + noOfCopies * shippingCostAdditional;
wholesaleCost = noOfCopies * bookPrice * (1 - bookStoreDiscount) + shippingCosts;

print('Wholesale Cost = $', wholesaleCost);

# 2.2.3 If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
# tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

easyPace = 8 * 60 + 15 #8:15 per mile
fastPace = 7 * 60 + 12 #7:12 per mile
startHour = 6;
startMinute = 52;

timeTakenForBreakfast = 1 * easyPace + 3 * fastPace + 1 * easyPace; #in seconds
print('timeTakenForBreakfast = ', timeTakenForBreakfast, ' seconds')

timeTakenForBreakfastHours = timeTakenForBreakfast  // (60*60); #convert to hours (floor division)
print('timeTakenForBreakfastHours = ', timeTakenForBreakfastHours);

timeTakenForBreakfastMinutes = timeTakenForBreakfast // 60; #convert to minutes and mod.
print('timeTakenForBreakfastMinutes = ', timeTakenForBreakfastMinutes);

if (timeTakenForBreakfastMinutes + startMinute) >= 60:
    timeTakenForBreakfastHours = timeTakenForBreakfastHours + (timeTakenForBreakfastMinutes + startMinute) // 60;
    timeTakenForBreakfastMinutes = timeTakenForBreakfastMinutes - 60;
else:
    pass
print('timeTakenForBreakfastMinutes = ', timeTakenForBreakfastMinutes);
print('Breakfast Time = ', startHour + timeTakenForBreakfastHours, ':', startMinute + timeTakenForBreakfastMinutes);
