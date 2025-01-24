# NAME: [Your Name]

# HIGHEST VALUE FUNCTION
def highest(data):
    """
    Finds the beach with the highest E. coli level.
    Pseudocode:
    1. Initialize variables for the highest value and beach name.
    2. Iterate through the dataset.
    3. If the current value is higher than the stored highest value, update the variables.
    4. Return the beach name and the highest value.
    """
    highest_value = 0
    highest_beach = ""
    for record in data:
        beach_name, ecoli = record
        if ecoli > highest_value:
            highest_value = ecoli
            highest_beach = beach_name
    return (highest_beach, highest_value)

# GEOMETRIC MEAN FUNCTION
import math

def geometricMean(data):
    """
    Calculates the geometric mean of E. coli levels.
    Pseudocode:
    1. Initialize a product variable and counter.
    2. Multiply all E. coli values together.
    3. Calculate the nth root of the product (n is the number of values).
    4. Return the geometric mean.
    """
    product = 1
    count = 0
    for record in data:
        ecoli = record[1]
        product *= ecoli
        count += 1
    geometric_mean = math.pow(product, 1 / count)
    return geometric_mean

# DATASET
beachData = [['Bay View East',1],
['Bay View',2.67],
['Bay View',24.11],
['Bay View',2.8],
['Bay View',32.5],
['Bay View',3.25],
['Bay View',45.25],
['Bay View',7],
['Bay View',24],
['Bay View',3.5],
['Camp Perry',25.83],
['Camp Perry',43.25],
['Camp Perry',14.6],
['Cat Island State Park ',42],
['Cedar Point',3],
['Cedar Point',31.5],
['Cedar Point',21.5],
['Cedar Point',42.13],
['Cedar Point',24],
['Century Beach',333],
['Century Beach',42.75],
['Century Beach',2.11],
['Century Beach',23.91],
['Beulah Beach',341.83],
['Beulah Beach',3.07],
['Beulah Beach',22.56],
['Beulah Beach',32.33],
['Township Park',42], 
['Township Park',22],
['Township Park',25],
['Cranberry Creek',3.5],
['Cranberry Creek',2],
['Cranberry Creek',3.2],
['Cranberry Creek',3],
['Darby Creek',16.33],
['Darby Creek',23.07],
['Darby Creek',13.25],
['Darby Creek',31.8],
['Harbor State Park',1],
['Harbor State Park',3],
['Harbor State Park',2.5],
['Edgewater Park',1.86],
['Edgewater Park',2.2],
['Edgewater Park',2.23],
['Edgewater Park',1.45],
['Edgewater State Park',2],
['Edison Creek',19.5],
['Edison Creek',56],
['Edison Creek',136.56],
['Edison Creek',436.7],
['Euclid Park',234.33],
['Euclid Park',223.2],
['Euclid Park',433.15],
['Euclid Park',22.18],
['Euclid Park',2.57],
['Fair Harbor',31],
['Fair Harbor',12.38],
['Fair Harbor',32.1],
['Fair Harbor',11.91],
['Fair Harbor',42],
['Hey Beach',2.25],
['Hey Beach',1.78],
['Hey Beach',1.9],
['Hey Beach',2],
['Geneva Park',2],
['Geneva Park',2],
['Headlands Park',431.5],
['Headlands Park',523.83],
['Headlands Park',91.78],
['Headlands Park',812.88],
['Headlands Park',354],
['Headlands Park',284.5],
['Headlands Park',168.8],
['Headlands Park',432.67],
['Headlands Park',327.44],
['Headlands Park',821],
['Hoffman Ravine',4.5],
['Hoffman Ravine',33.89],
['Hoffman Ravine',23.33],
['Hoffman Ravine',24.86],
['Hoffman Ravine',63],
['Hunt Beach',1.67],
['Hunt Beach',23.15],
['Hunt Beach',43.2],
['Hunt Beach',23.78],
['Hunt Beach',32],
['Nickel Beach',1.5],
['Nickel Beach',1.5],
['Nickel Beach',1.5],
['Nickel Beach',3.64],
['Nickel PBeach',2],
['Lake Park',21.25],
['Lake Park',24],
['Lake Park',332.09],
['Lake Park',233.8],
['Lake Park',323],
['Island Park',39.4],
['Island Park',72],
['Island Park',55],
['Island Park',34],
['Lakeshore Park',25],
['Lakeshore Park',2],
['Lakeshore Park',3],
['Lakeshore Park',7.8],
['Lakeshore Park',6],
['Lakeside Beach',2.2],
['Lakeside Beach',4],
['Lakeview Beach',133],
['Lakeview Beach',34],
['Lakeview Beach',327],
['Lakeview Beach',459],
['Lakeview Beach',195],
['Maple Beach',1],
['Maple Beach',3.82],
['Maple Beach',5.23],
['Maple Beach',5.93],
['Maple Beach',10.33],
['Maple Beach',4.5],
['Maple Beach',7.75],
['Maple Beach',5.08],
['Maple Beach',5],
['Oscar Beach',1],
['Oscar Beach',2.25],
['v Beach',1.25],
['Oscar Beach',2.4],
['Old Beach',0.5],
['Old Beach',3],
['Old Beach',2.5],
['Old Beach',2],
['Old Beach',3.5],
['Pickle Creek',4],
['Pickle Creek',3.5],
['Pickle Creek',3.5],
['Pickle Creek',3.5],
['Pickle Creek',4],
['Port Beach',5],
['Port Beach',3.83],
['Port Beach',5],
['Port Beach',2.5],
['Port Beach',4],
['Sawmill Beach',2.2],
['Sawmill Beach',3],
['Sawmill Beach',3.4],
['Sheep Park Beach',1.67],
['Sheep Park Beach',2.6],
['Sheep Park Beach',3],
['Sheep Park Beach',3.2],
['Sheep Park Beach',4],
['Sheep Park ',2.45],
['Sheep Park ',2.4],
['Sheep Park ',2.86],
['Bass Park',2],
['Bass Park',2],
['Sugar Creek',2],
['Sugar Creek',5],
['Sugar Creek',3.64],
['Sugar Creek',2.9],
['Sugar Beach',2.75],
['Sugar Beach',3.1],
['Sugar Beach',2.85],
['Sugar Beach',2.75],
['Sugar Beach',4],
['Main Street Beach',1.8],
['Main Street Beach',3],
['Main Street Beach',2],
['Main Street Beach',2.14],
['Valley Park',3.5],
['ValleyPark',3.2],
['Valley  Park',2.89],
['Valley Park',1.93],
['Valley Park',2.55],
['Walnut Beach',2],
['Walnut Beach',2],
['Walnut Beach',2],
['Walnut Beach',2],
['Windy Park',6],
['Windy Park',1],
['Windy Park',2]]

# Find the highest value in the dataset.
topValue = highest(beachData)
print("The highest value of " + str(topValue[1]) + " was found at " + topValue[0] + ".")

# Find the geometric average of the test results.
geomMean = geometricMean(beachData)
geomMean = round(geomMean, 2)
print("The geometric average is " + str(geomMean) + ".")
