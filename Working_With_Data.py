import pandas as pd 
import numpy as np
from scipy import stats

pd.set_option('display.max_columns', None)
df = pd.read_excel("C:\\Users\\vturn\\OneDrive\\CollegeRanking.xlsx")
"""
first thing to do when we upload a new excel file that we havent gotten a chance to overview is get a 
understanding of what were working with we can do that through a few steps.

1. lets get the column names using the .columns funtion will print all the column titles into a list
for a better high level overview 
input:
print(df.columns)

output:
Index(['World Rank', 'Institution', 'Country', 'State', 'Bachelors Tuition ',
       'Acceptance Rate', 'Class', 'Country Rank', 'Education Rank',
       'Employability Rank', 'Faculty Rank', 'Research Rank', 'Score'],
      dtype='object')

this will also accomplish the same thing the 
print(df.keys()) 
"""
# print(df.columns)

"""
okay now that we've got that out of the way lets actually look at the data using print()

2. Open raw excel sheet with no filters applied 

input: 
print(df)

output:
    World Rank                              Institution  ... Research Rank  Score
0            1                     Harvard University    ...             1  100.0  
1            2  Massachusetts Institute of Technology    ...             7   96.7  
2            3                    Stanford University    ...             2   95.1  
3            4                 University of Cambridge   ...            10   94.1  
4            5          University of Oxford  Education  ...             4   93.3  
..         ...                                      ...  ...           ...    ...  
95          96               National Taiwan University  ...           125   81.9  
96          97                      Zhejiang University  ...            37   81.9  
97          98                     University of Sydney  ...            39   81.8  
98          99                        Boston University  ...            77   81.8  
99         100                          Keio University  ...           392   81.8  
"""
# print(df)
"""
Now that we got the opportunity to see the full raw dataset we see that we have some missing values 
we can take a more in depth look at those and eventually clean those up using the isna() function

3.How many missing values do we actually have per columns ? 
input:
df.isna().sum()

output:
13
World Rank            0
Institution           0
Country               0
State                 0
Bachelors Tuition     5
Acceptance Rate       5
Class                 0
Country Rank          0
Education Rank        0
Employability Rank    0
Faculty Rank          0
Research Rank         0
Score                 0





find the missing values
df[df.isna().any(axis=1)]  


    World Rank                                Institution  Country   
18          19                             PSL University   France  \
46          47                        Tsinghua University    China
50          51                          Peking University    China
55          56                  Free University of Berlin  Germany
62          63  University of Chinese Academy of Sciences    China
77          78                         University of Oslo   Norway
78          79             Technical University of Munich  Germany
88          89                    University of Gottingen  Germany

           State  Bachelors Tuition   Acceptance Rate    Class  Country Rank       
18         Paris             17040.0              NaN  Private             1  \    
46     Tsinghua              18780.0              NaN   Public             1       
50       Beijing              4650.0              NaN  Private             2       
55        Berlin                 NaN             0.15  Private             2       
62       Beijing              9920.0              NaN   Public             3       
77  Problemveien                 NaN             0.10   Public             1       
78        Munich                 NaN             0.08  Private             5       
88     Gottingen             10148.0              NaN   Public             6       

   Education Rank Employability Rank Faculty Rank  Research Rank  Score
18             17                 30          107             86   88.4
46            521                 60            -             23   84.9
50            366                 65            -             28   84.5
55             72               1142           37             78   84.2
62              -               1253            -             12   83.7
77            103                751           77             94   82.8
78             79                356          141             84   82.8
88             43                329          105            155   82.2
"""


# print(df[df.isna().any(axis=1)])

""" 
We have a few missing values(-) and values that have the term (Nan (not actual number)) so someone
attempted to clean it prior but we can go a bit more in depth lets start with the column Bachelors 
Tuition 

4.fill in missing values to prevent them from skewing the analysis its a lot and complicated at first 
glance but we can take it apart to make it easier to understand

part 1 
the same way we'd update any other table columns the column name followed by the update 
df[""Bachelors Tuition "] 

part 2
fill the not applicable 
df[""Bachelors Tuition "].fillna()

part 3
the fillna() function takes two arguments the first is what we're replacing the missing values to
(in our case 0 makes the most sense) and the inplace = True is to ensure we arent making a seperate 
dataframe and are making the changes to the main dataframe
df[""Bachelors Tuition "].fillna(0, inplace=True)


End Result
df[""Bachelors Tuition "].fillna(0, inplace=True)

after we finish this we need to make sure that it worked so we run the following code 
print(df[""Bachelors Tuition "].isna().sum())

if this returns 0 it means that it worked there are 0 missing values in the Bachelors Tuition
column of our dataframe
"""

df["Bachelors Tuition "].fillna(0, inplace=True)
print(df["Bachelors Tuition "].isna().sum())

"""
With the neccesary missing values being removed from the dataframe we can get a quick analysis of the 
numerical columns using the describe() function

5.use describe() function to get the total number of entries(count), the average(mean), the standard
deviation(std), the 25th, 50th, and 75th percentiles, and lastly the maximum number in the column(max)

print(df.describe())

World Rank  Bachelors Tuition   Acceptance Rate  Country Rank   
count  100.000000          100.000000        95.000000    100.000000  \
mean    50.500000        94890.120000         0.443994     14.180000
std     29.011492       100879.326674         1.465420     15.380284
min      1.000000            0.000000         0.039000      1.000000
25%     25.750000        25582.000000         0.110000      2.000000
50%     50.500000        58620.000000         0.204000      5.500000
75%     75.250000       122606.000000         0.475000     25.250000
max    100.000000       545976.000000        14.400000     50.000000

       Research Rank       Score
count     100.000000  100.000000
mean       74.180000   84.718000
std        78.590921    9.265493
min         1.000000    0.000000
25%        25.750000   82.900000
50%        52.500000   84.500000
75%        91.500000   87.050000
max       436.000000  100.000000

"""
print(df.describe)

"""
1. The first question to answer is which is typically more expensive private or public tuition and 
by how much ? 

private_schools = df[df["Class"] == "Private"]

this is a larger dataset so were limiting the amount displayed in the terminal but the following
will make sure our private_schools dataset is working properly

input:
print(Private_Schools.head(5)[["Institution", "Class"]])

out: 
                               Institution    Class
0                     Harvard University    Private
1  Massachusetts Institute of Technology    Private
2                    Stanford University    Private
5                   Princeton University    Private
7           Columbia University  Education  Private

now that we've established the one for private we need to do the same for Public schools as well

public_schools = df[df["Class"] == "Public"]

input: 
print(public_schools.head(5)[["Institution", "Class"]])

output: 
                        Institution   Class
3               University of Cambridge   Public
4        University of Oxford  Education  Public
11  University of California, Berkeley    Public
12                   University of Tokyo  Public
14     University of Michigan, Ann Arbor  Public

now that theyre both established lets use numpy to get the average(mean) for both

****important, remember it will return an error if your using np.mean on any column that isnt made
up strictly of numbers i made that mistake a few seconds ago

example:
public_schools_average = numpy.mean(public_schools[["Institution","Bachelors Tuition "]])

this wont work because Institution is a string not a number 
public_schools_average = np.mean(public_schools[["Bachelors Tuition "]]) this is fine since its only 
an integer****** 
  
public_schools_average = np.mean(public_schools[["Bachelors Tuition "]])
Input: 
print(public_schools_average)

output: 
77459.15094339622

lets do the same for private schools now 
private_schools_average = np.mean(private_schools[["Bachelors Tuition "]])
input:
print(private_schools_average)

output:                               
122022.73809523809

now we have our numbers lets put them into a currency format that's easier to understand by slicing 

input: 
print("${:,.2f}".format(private_schools_average))
output:
$122,022.74

input: 
print("${:,.2f}".format(public_schools_average))
output: 
$77,459.15

finally we need to find out how much the difference in price is between the two 
difference = private_schools_average - public_schools_average
print("${:,.2f}".format(difference))

output:
$44,563.59

so it looks like public schools are less expensive than private by an average of $44,563.59. 
test it yourself below
""" 


Private_Schools = df[df["Class"] == "Private"]
Private_mean_tuition = np.mean(Private_Schools["Bachelors Tuition "])
print("${:,.2f}".format(Private_mean_tuition))

Public_Schools = df[df["Class"] == "Public"]
Public_mean_tuition = np.mean(Public_Schools["Bachelors Tuition "])
print("${:,.2f}".format(Public_mean_tuition))

""" 
2. How many indivdual countries are in the ranking, which country is the most reoccurring in the top
100 schools

lets start by getting a list of all the countries included in the ranking the unique method returns 
a list of all unique entries similar to the distinct cin SQL

input: 
Countries = df["Country"].unique()
print(Countries)

output: 
['USA' 'United Kingdom' 'Japan' 'France' 'Canada' 'Switzerland'
 'South Korea' 'Denmark' 'Sweden' 'Germany' 'China' 'Australia' 'Israel'
 'Netherlands' 'Norway' 'Singapore' 'Taiwan']
 
now that we have our list instead of manually adding them up we can just use the len function
input:
print(len(Countries))

output:
17

we have 17 countries in our ranking, to understand which country is the most common we can use the 
mode function in python. lets update our variable countries since that only takes one instance of 
each country



***
important here when using the mode we need to add [0] at the end, without it itll still return 
the most frequent occurence but it will return it as a dataframe/set format rather than a string. 
ill show an example below

input: 
Countries = df["Country"]
MostFrequent = Countries.mode() #without the [0]
print(MostFrequent)

output:
0    USA
Name: Country, dtype: object

compared to with the [0] 
input: 
Countries = df["Country"]
MostFrequent = Countries.mode()[0]
print(MostFrequent)

output:
'USA'
***

input: 
Countries = df["Country"]

MostFrequent = Countries.mode()[0]
print(MostFrequent)

output:
USA

That answers question 2 we have 17 unique countries and the USA is the most frequently occurring one 
lets see how many schools are actually in the USA 

input: 
USA = df[df["Country"] == "USA"]
print(len(USA))

output: 
50

wow 50 total not bad thats half of our rankings
"""

TotalCountry = df["Country"].unique()
print(len(TotalCountry))

Countries = df["Country"]
MostFrequent = Countries.mode()[0]
print(MostFrequent)


"""
3. how many schools are there per state in the USA ?
start by grouping all the schools in the USA into a separate dataframe using 

USA = df[df["State"] == "USA"] #this works but we see too much frequency we can cut it down again
using the unique method from earlier 

input:
Unique_USA_States = USA["States"].unique()

output:
['Massachusetts' 'California' 'New Jersey' 'Illinois' 'New York'
 'Pennsylvania' 'Connecticut' 'Michigan' 'Maryland' 'North Carolina'
 'NewYork' 'Washington' 'Wisconsin' 'Texas' 'New Hampshire' 'Missouri'
 'Minnesota' 'Tennessee' 'Ohio' 'Indiana' 'Rhode Island,' 'Georigia'
 'Colorado' 'Virginia' 'California ' 'Florida' 'Arizona']
 
now we have a list of each state in the USA that has a school in our rankings that limits things
lets get a total count that represents the number of schools per state

input: 
for state in Unique_USA_States: 
  count = len(USA[USA["State"] == state])
  print("{} has {} schools".format(state, count))
  
that should return 
Massachusetts has 3 schools
California has 9 schools
New Jersey has 2 schools
Illinois has 3 schools
New York has 4 schools
Pennsylvania has 4 schools
Connecticut has 1 schools
Michigan has 1 schools
Maryland has 2 schools
North Carolina has 2 schools
NewYork has 1 schools
Washington has 1 schools
Wisconsin has 1 schools
Texas has 3 schools
New Hampshire has 1 schools
Missouri has 1 schools
Minnesota has 1 schools
Tennessee has 1 schools
Ohio has 1 schools
Indiana has 1 schools
Rhode Island, has 1 schools
Georigia has 1 schools
Colorado has 1 schools
Virginia has 1 schools
California  has 1 schools
Florida has 1 schools
Arizona has 1 schools


"""

USA = df[df["Country"] == "USA"]
unique_states = USA["State"].unique()
for state in unique_states:
    count = len(USA[USA["State"] == state])
    print("{} has {} schools".format(state, count))
"""    
What is the average tuition by country?
**** important Side note theres always a different way of doing things in python this line of code 
will accomplish the same result as doing the for loop for question 2

input:
country_tuition = (df.groupby("Country")["Bachelors Tuition "].mean())
print(country_tuition)

output:
Country
Australia          56534.50
Canada             50774.75
China              13475.60
Denmark            47200.00
France             39011.20
Germany            24156.00
Israel             20375.00
Japan              14631.75
Netherlands       235015.00
Norway                  NaN
Singapore          38250.00
South Korea        48000.00
Sweden             65760.00
Switzerland         6640.00
Taiwan              1682.00
USA               135328.88
United Kingdom     80897.00
Name: Bachelors Tuition , dtype: float64
***

"""


