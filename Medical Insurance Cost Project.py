#!/usr/bin/env python
# coding: utf-8

# In[71]:


# set up and prepare data 
# データをセットや準備します


# In[ ]:


import csv


# In[72]:


ages = []
sexes = []
bmis = []
num_children = []
smoker_status = []
regions = []
insurance_charges = []


# In[73]:


def load_list_data(lst, csv_file, column_name):
    with open('insurance.csv') as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            lst.append(row[column_name])
        return lst    
    


# In[74]:


load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_status, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')


# In[148]:


# Classifying ages into four groups

children = []
youth = []
adult = []
senior = []

children_charges = []
youth_charges = []
adult_charges = []
senior_charges = []

for i in range(len(ages)):
    ages[i] = float(ages[i])
    if ages[i] >= 0 and ages[i] <= 14:
        children.append(ages[i])
        children_charges.append(insurance_charges[i])
    elif ages[i] > 14 and ages[i] <= 24:
        youth.append(ages[i])
        youth_charges.append(insurance_charges[i])
    elif ages[i] > 24 and ages[i] <= 64:
        adult.append(ages[i])
        adult_charges.append(insurance_charges[i])
    else:
        senior.append(ages[i])
        senior_charges.append(insurance_charges[i])
        
        
print(len(children))
print(len(senior))
print("the precentage of youth pay for the insurance cost " + str(round((len(youth)/len(ages)),3)))
print("the precentage of youth pay for the insurance cost " + str(round(len(adult)/len(ages),3)))


# In[156]:


sum_youth = 0
for i in youth_charges:
    sum_youth += float(i)
avg_youth = round(sum_youth/len(youth_charges),3)

sum_adult = 0
for i in adult_charges:
    sum_adult += float(i) 
avg_adult = round(sum_adult/len(adult_charges),3)    


# In[157]:


# In order to find the median we need to sort the list first
def sort_the_list(float_list):
    for i in range(len(float_list)):
        float_list[i] = float(float_list[i])
    float_list.sort()
sort_the_list(youth_charges)


# In[158]:


sort_the_list(youth_charges)
sort_the_list(adult_charges)


# In[159]:


#The median of the youth_charges list
median_youth_cost = youth_charges[int(len(youth_charges)/2)]
median_youth_cost


# In[160]:


#The mean cost of youth group
avg_youth


# In[161]:


#The median of the adult_charges list
median_adult_cost = adult_charges[int(len(adult_charges)/2)]
median_adult_cost


# In[162]:


#The mean cost of adult group
avg_adult


# In[83]:


# Among age groups, children and senior do not take part in the medical insurance, two main groups are youth and aldult group
# Youth group occupy about 20% of the number of patients and aldult group occupy nearly 80% of the number of the patients
# There is a larger difference in youth group than adult group
# it means the average charges which are seperated among patients in youth group is less even than adult group's
# The average charges in adult group is obviously higher which is considered based on both mean and median measure
# There four the age aspect can be considered to get influence on the insurance charges


# In[132]:


# classifying bmi index into four group

under_weight_charges = []
healthy_weight_charges = []
over_weight_charges = []
obesity_charges = []

for i in range(len(bmis)):
    bmis[i] = float(bmis[i])
    if bmis[i] < 18.5:
        under_weight_charges.append(insurance_charges[i])
    elif bmis[i] >= 18.5 and bmis[i] < 25:
        healthy_weight_charges.append(insurance_charges[i])
    elif bmis[i] >= 25 and bmis[i] < 30:
        over_weight_charges.append(insurance_charges[i])
    else: obesity_charges.append(insurance_charges[i])
        
sum_one = 0
for i in under_weight_charges:
    sum_one += float(i)
avr_one = round((sum_one/len(under_weight_charges)),3)

sum_two = 0
for i in healthy_weight_charges:
    sum_two += float(i)
avr_two = round((sum_two/len(healthy_weight_charges)),3)

sum_three = 0
for i in over_weight_charges:
    sum_three += float(i)
avr_three = round((sum_three/len(over_weight_charges)),3)

sum_four = 0
for i in obesity_charges:
    sum_four += float(i)
avr_four = round((sum_four/len(obesity_charges)),3)


# In[133]:


sort_the_list(under_weight_charges)
sort_the_list(healthy_weight_charges)
sort_the_list(over_weight_charges)
sort_the_list(obesity_charges)


# In[134]:


#The median of under_weight_charges
under = under_weight_charges[int(len(under_weight_charges)/2)]


# In[135]:


#The median of healthy_weight_charges
healthy = healthy_weight_charges[int((len(healthy_weight_charges)+1)/2)]


# In[136]:


#The median over_weight_charges
over = over_weight_charges[int(len(over_weight_charges)/2)]


# In[137]:


#The median of obesity_charges
obesity = obesity_charges[int(len(obesity_charges)/2)]


# In[222]:


#The medians of bmi groups
median_bmi_group={}
median_bmi_group['underweight_median']=under
median_bmi_group['healthy_median']=healthy
median_bmi_group['over_median']=over
median_bmi_group['obesity_median']=obesity

median_bmi_group


# In[223]:


#The mean cost of under weight group
avr_one


# In[224]:


#The mean cost of healthy weight group
avr_two


# In[225]:


#The mean cost of over weight group
avr_three


# In[226]:


#The mean cost of obesity group
avr_four


# In[227]:


#The means of bmi groups
mean_bmi_group={}
mean_bmi_group['underweight_mean']=avr_one
mean_bmi_group['healthy_mean']=avr_two
mean_bmi_group['over_mean']=avr_three
mean_bmi_group['obesity_mean']=avr_four

mean_bmi_group


# In[228]:


# Both mean and median measure confirm that the escalation of insurance cost following the increase of weight
# Median is not pull much by outliers show that the insurance costs are seperated quite evenly among patients in all four groups
# BMI is predicted as the significant factor contribute to the surge of insurance costs


# In[240]:


male_charges = []
female_charges = []

for i in range(len(sexes)):
    if sexes[i] == 'male':
        male_charges.append(float(insurance_charges[i]))
    if sexes[i] == 'female':
        female_charges.append(float(insurance_charges[i]))
        
sum_male = 0
sum_female = 0

for i in male_charges:
    sum_male += float(i)
avg_male = round(sum_male/len(male_charges),3 )

for i in female_charges:
    sum_female += float(i)
avg_female = round(sum_female/len(female_charges),3)


# In[241]:


sort_the_list(male_charges)
sort_the_list(female_charges)


# In[242]:


#The median charge of male
male_med = male_charges[int(len(male_charges)/2)]


# In[243]:


#The median charge of female
female_med = female_charges[int(len(female_charges)/2)]


# In[244]:


#The dictionary of sex_charges_median
sex_charge_median={}
sex_charge_median['male_med']=male_med
sex_charge_median['female_med']=fem_med

sex_charge_median


# In[245]:


#The mean charge of male
avg_male


# In[246]:


#The mean charge of female
avg_female


# In[247]:


# The dictionary of sex charge means
sex_charge_mean={}
sex_charge_mean['male_mean']=avg_male
sex_charge_mean['female_mean']=avg_female

sex_charge_mean


# In[ ]:


# overall, male have to pay the higher cost for insurance than female
# The charge variation among patients in male group is higher than female group's but insignificantly
# The sex metric can affect the insurance charges in some level


# In[238]:


#男の人や女の人に違いはあります


# In[249]:


smoking = []
none_smoking = []


# In[250]:


for i in range(len(smoker_status)):
    if smoker_status[i] == 'yes':
        smoking.append(insurance_charges[i])
    elif smoker_status[i] == 'no':
        none_smoking.append(insurance_charges[i])
    else: print(smoker_status)


# In[251]:


sort_the_list(smoking)
sort_the_list(none_smoking)


# In[252]:


#The median cost of people having the habit of smoking
smoking_med = smoking[int(len(smoking)/2)]


# In[253]:


#The mean cost of people not having the habit of smoking
none_smoking_med = none_smoking[int(len(none_smoking)/2)]


# In[256]:


smoking_median={}
smoking_median['smoking_med']=smoking_med
smoking_median['none_smoking_med']=none_smoking_med

smoking_median


# In[262]:


sum_smoking = 0
for i in smoking:
    sum_smoking += float(i)
avg_smoking = round(sum_smoking/len(smoking),3)

sum_none_smoking = 0
for i in none_smoking:
    sum_none_smoking += float(i)
avg_none_smoking = round(sum_none_smoking/len(none_smoking),3)   


# In[263]:


#The mean cost of people having the habit of smoking
avg_smoking


# In[264]:


#The mean cost of people not having the habit of smoking
avg_none_smoking


# In[268]:


smoking_mean={}
smoking_mean['smoking_mean']=avg_smoking
smoking_mean['none_smoking_mean']=avg_none_smoking

smoking_mean


# In[ ]:


# Obviously, the people have the habit of smoking incurring the heavier burden of insurance costs than the people does not have.
# It is not biased because both center points and mean cost in smoking group is much higher than none smoking group
# It show that this contribution factor does not depend much on other ones.


# In[266]:


from collections import Counter
Counter(num_children)    


# In[178]:


none_children_charges=[]
one_children_charges=[]
two_children_charges=[]
three_children_charges=[]
four_children_charges=[]

for i in range(len(num_children)):
    if num_children[i]=='0':
        none_children_charges.append(float(insurance_charges[i]))
    elif num_children[i]=='1':
        one_children_charges.append(float(insurance_charges[i]))
    elif num_children[i]=='2':
        two_children_charges.append(float(insurance_charges[i]))
    elif num_children[i]=='3':
        three_children_charges.append(float(insurance_charges[i]))
    elif num_children[i]=='4':
        four_children_charges.append(float(insurance_charges[i]))

sort_the_list(none_children_charges)
sort_the_list(one_children_charges)
sort_the_list(two_children_charges)
sort_the_list(three_children_charges)
sort_the_list(four_children_charges)    


# In[179]:


sum_zero = 0
sum_one = 0
sum_two = 0
sum_three = 0
sum_four = 0

for i in none_children_charges:
    sum_zero += i
for i in one_children_charges:
    sum_one += i
for i in two_children_charges:
    sum_two += i
for i in three_children_charges:
    sum_three += i
for i in four_children_charges:
    sum_four += i


# In[180]:


#The median insurance cost of the families do not have childs
me_none = none_children_charges[int(len(none_children_charges)/2)]


# In[194]:


#The mean insurance cost of the families do not have childs
avg_none = round(sum_zero/len(none_children_charges),3)


# In[195]:


#The median insurance cost of the families have one child
me_one = one_children_charges[int(len(one_children_charges)/2)]


# In[196]:


#The mean insurance cost of the families have one child
avg_one = round(sum_one/len(one_children_charges),3)


# In[197]:


#The median insurance cost of the families have two childs
me_two = two_children_charges[int(len(two_children_charges)/2)]


# In[198]:


#The mean insurance cost of the families have two childs
avg_two = round(sum_two/len(two_children_charges),3)


# In[199]:


#The median insurance cost of the families have three childs
me_three = three_children_charges[int((len(three_children_charges)+1)/2)]


# In[200]:


#The mean insurance cost of the families have three childs
avg_three = round(sum_three/len(three_children_charges),3)


# In[201]:


#The median insurance cost of the families have four childs
me_four = four_children_charges[int((len(four_children_charges)+1)/2)]


# In[202]:


#The mean insurance cost of the families have four childs
avg_four = round(sum_four/len(four_children_charges),3)


# In[203]:


num_children_median = {}

num_children_median['none_children']=me_none
num_children_median['one_children']=me_one
num_children_median['two_children']=me_two
num_children_median['three_children']=me_three
num_children_median['four_children']=me_four

#The median costs of age group
num_children_median


# In[204]:


num_children_mean = {}

num_children_mean['none_children']=avg_none
num_children_mean['one_children']=avg_one
num_children_mean['two_children']=avg_two
num_children_mean['three_children']=avg_three
num_children_mean['four_children']=avg_four

#The mean costs of age group
num_children_mean


# In[276]:


# The mean of insurance costs rise up steadily according to the number of children, however it drop a little when it reach four children
# Tha age metric may be affected significantly by outliers when each center point does not follow the certain order
# The families have none children and having four children whose insurance chrages are separated more equally than other groups


# In[209]:


from collections import Counter
Counter(regions) 


# In[274]:


south_west_charges = []
south_east_charges = []
north_west_charges = []
north_east_charges = []
for item in range(len(regions)):
    if regions[item]=='southwest':
        south_west_charges.append(float(insurance_charges[item]))
    elif regions[item]=='southeast':
        south_east_charges.append(float(insurance_charges[item]))
    elif regions[item]=='northwest':
        north_west_charges.append(float(insurance_charges[item]))
    else: north_east_charges.append(float(insurance_charges[item]))  


# In[275]:


sort_the_list(south_west_charges)
sort_the_list(south_east_charges)
sort_the_list(north_west_charges)
sort_the_list(north_east_charges)


# In[283]:


#The median of south west charges
sw_char = south_west_charges[int((len(south_west_charges)+1)/2)]


# In[282]:


#The median of south east charges
se_char = south_east_charges[int(len(south_east_charges)/2)]


# In[285]:


#The median of north west charges
nw_char = north_west_charges[int((len(north_west_charges)+1)/2)]


# In[288]:


#The median of north east charges
ne_char = north_east_charges[int(len(north_east_charges)/2)]


# In[290]:


region_med={}
region_med['southwest']=sw_char
region_med['southeast']=se_char
region_med['northwest']=nw_char
region_med['northeast']=ne_char

region_med


# In[216]:


#The mean insurance costs of southwest
avg_sw = round((south_west_charges/325),3)
avg_sw


# In[217]:


#The mean insurance costs of southeast
avg_se = round((south_east_charges/364),3)
avg_se


# In[218]:


#The mean insurance costs of northwest
avg_nw = round((north_west_charges/325),3)
avg_nw


# In[219]:


#The mean insurance costs of northeast
avg_ne= round((north_east_charges/324),3)
avg_ne


# In[289]:


region_mean= {}
region_mean['south_west'] = avg_sw
region_mean['south_east'] = avg_se
region_mean['north_west'] = avg_nw
region_mean['north_east'] = avg_ne
region_mean


# In[292]:


#The average insurance cost in the south part
round(((avg_sw+avg_se)/2),3)


# In[293]:


#The average insurance cost in the north part
round(((avg_nw+avg_ne)/2),3)


# In[221]:


# The mean insurance costs of the east regions is higher than the west regions
# The medians in both east and west regions does not variate far from the mean confirm that the first statement
# ost people in the east region pay higher insurance charges
# The average insurance cost in the north regions is lower than the south regions


# In[ ]:


# In summary, all aspects are investigated in this project influence the charges in different levels
# The factors are considered that the most objectly influencing are the ones have the least amount of bias, it means that the mean value is not far from the center point
# There are two independent variables affecting the results the most are bmis and smoker_status without much biased
# The number of children factor does not have obvious effect on the result
# In the sex group, some bias may be exist because the charges among female patient is closer than the charges among the male patients
# In the reigion group, the east and north region seem to bear the higher costs


# In[ ]:


# Recommendation
# People can reduce the medical insurance charges by focus and changing the controllable variables such as bmi index, the habit of smoking or even reducing the births


# In[ ]:


# 終わります

