# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 23:27:43 2024

@author: Tahsan Ul Alam
"""

############# From Project 2 Phase 1 ##########################

def loadCityData():
    citylist = []
    statename = ''
    with open("miles.txt", 'r') as file:
        for i in file:
            if i[0].isalpha():
                m = i.index(',')
                statename += i[0: m + 4]
                b = statename.replace(',', '')
                citylist.append(b)
                statename = ''
                
    return citylist


def loadInformation():
  try:
    coordinateList = []
    populationList = []
    distanceList = []
    tempList = []
    tempList1 = []
    with open("miles.txt","r") as file:
        for line in file:
          if line[0].isalpha():
             for i in range(1,len(line)):
                    if not line[i].isalpha() and not line[i].isdigit():
                       line = line.replace(line[i]," ")
             line = line.split()
            
             numString1 = int(line[-1])
             tempList = [int(line[-3]),int(line[-2])]
             coordinateList.append(tempList)
             populationList.append(numString1)
             tempList = []
             numString1 = ""
             
             if tempList1 != []:
              distanceList.append(tempList1)
              tempList1 = []
              
                 
            
          if line[0].isdigit():
                  line = line.split()
                  for i in range(len(line)):
                      tempList1.append(int(line[i]))
        distanceList.append(tempList1)
        tempList1 = []
     
    
    return coordinateList, populationList, distanceList

  except:
    return []

def listAllInformation():
    
    cityList = loadCityData()
    coordinateList, populationList, distanceList = loadInformation()
    distanceDictionary = {}
    ind1 = 1
    totalList = []
  
    for i in range(1,len(cityList)):
        distanceDictionary[cityList[i]] = distanceList[i-1][-1]
    tempList = [coordinateList[0],populationList[0],distanceDictionary]
    totalList.append(tempList)
    tempList = []
    distanceDictionary = {}
   

    for i in range(len(distanceList)):
        
        for j in range(len(distanceList[i])):
          distanceDictionary[cityList[len(distanceList[i])-j-1]] = distanceList[i][j]
        
        for k in range(len(distanceList[i]) + 1,len(cityList)):
            distanceDictionary[cityList[k]] = distanceList[k-1][-i-2]
        
        tempList = [coordinateList[ind1],populationList[ind1], distanceDictionary]
        totalList.append(tempList)
        tempList = []
        distanceDictionary = {}
        ind1 += 1
    
    
    return totalList
         
            
def loadData():
   cityList = loadCityData()
   coordinateList, populationList, distanceList = loadInformation()
   totalList = listAllInformation()
   cityDataDictionary = {}
   
   for i in range(len(totalList)):
       cityDataDictionary[cityList[i]] = totalList[i]
   
   return cityDataDictionary

def nearbyCities(cityDataDict, cityName, r):
    nearbyCitiesList = []
    
    if cityName not in cityDataDict:
        return None
    
    for city in cityDataDict:
        if city in cityDataDict[cityName][2]:
            if cityDataDict[cityName][2][city] <= r:
              nearbyCitiesList.append(city)
       
    nearbyCitiesList.append(cityName)

    return nearbyCitiesList
        

#################### Porject2 Phase 2 ###############################

## Greedy Algorithm Approach
        
def greedyFacilitySet(cityDataDictionary,r):
    served = set()
    unserved = []
    for city in cityDataDictionary:
        unserved.append(city)
    
    maxNum = 0
    finalList = []
    cityName = ""
    facilityList = []
    while unserved:
        for city in cityDataDictionary:
            
            facilityList = []
            totalFacilityList = []
            totalFacilityList = nearbyCities(cityDataDictionary, city, r)
            
            for facility in totalFacilityList: 
                if facility not in served:
                   facilityList.append(facility) 
           
            totalFacilities = len(facilityList)
            if maxNum < totalFacilities:
                maxNum = totalFacilities
                maximumFacilityList = facilityList
                cityName = city
                   
            elif maxNum == totalFacilities:
                cityName = min(city,cityName)
                if cityName == city:
                  maximumFacilityList = facilityList
                
       
        for facility in maximumFacilityList: 
            served.add(facility)
            unserved.remove(facility)
        if cityName not in finalList:
          finalList.append(cityName)
      
        cityName = ""
        maxNum = 0
        maximumFacilityList = []
        
  
    return finalList

## Brute Force Algorithm Approach

# Helper Function- 1
def actualSolution(cityDataDictionary, cityList, r):
    servedList = set()
    for city in cityList:
            facilityList = nearbyCities(cityDataDictionary,city,r)
            for facility in facilityList:
                servedList.add(facility)
 
    if len(servedList) == len(cityDataDictionary):
        return True
                      
    return False  

# Helper Function- 2

def generateAllSolutions(cityList, k):
    subset = []
    if k == 0:
        return [[]]  
    if len(cityList) == 0:
        return []
    first = cityList[0]
    rest = cityList[1:]
    print("call")
    list1 = generateAllSolutions(rest, k - 1)
    print("List1",list1)
    for solution in list1:
        subset.append([first] + solution)
        print("Subset",subset)
    list2 = generateAllSolutions(rest, k)
    print("list2",list2)
    subset.extend(list2)
    print("Subsent2",subset)
    return subset

print(generateAllSolutions(['a','b','c'],3))

# Helper Function- 3

def generate_All_Solutions_Of_1_to_K(cityList,k):
    AllSubset = []
    for i in range(1,k+1):
        tempList = (generateAllSolutions(cityList,i))
        for sublist in tempList:
            AllSubset.append(sublist)
            tempList = []
    return AllSubset


# Main Function

def optimalFacitilitySet(cityDataDictionary, r, oneSolution):
   k = len(oneSolution) - 1
   min = len(oneSolution)
   cityList = []
   possibleSolution = []
   for city in cityDataDictionary:
       cityList.append(city)
   possibleSolutions = generate_All_Solutions_Of_1_to_K(cityList,k)
   for solution in possibleSolutions:
       if actualSolution(cityDataDictionary,solution, r):
           if min > len(solution):
               min = len(solution)
               possibleSolution = solution
   return possibleSolution



