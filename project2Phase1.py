#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:43:51 2024

@author: Tahsan
"""

###############################################################################
#
# Specification: Reads information from the files "miles.txt" and loads all the 
# data from the file into a giant dictionary and returns this dictionary.
# If, for some reason, "miles.txt" is missing, the function should gracefully
# finish, returning the empty dictionary {}.
# 
###############################################################################

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
       
   

                
         
###############################################################################
#
# Specification: takes the dictionary that contains all the information associated 
# with the cities and a particular city name and returns the coordinates (which is a 
# list of 2 integers) of the given city. If, for some reason, cityName is not a key
# in cityDataDict, it returns None.
#
###############################################################################
def getCoordinates(cityDataDict, cityName):
    cityData = cityDataDict.get(cityName)
    
    if cityData is not None:
        coordinates = cityData[0]
        return coordinates
    else:
        return None
    
###############################################################################
#
# Specification: takes the dictionary that contains all the information associated 
# with the cities and a particular city name and returns the population (which is a 
# positive integer) of the given city. If, for some reason, cityName is not a key
# in cityDataDict, it returns None.
#
###############################################################################
def getPopulation(cityDataDict, cityName):
    cityData = cityDataDict.get(cityName)
    
    if cityData is not None:
        population = cityData[1]
        return population
    else:
        return None

###############################################################################
#
# Specification: takes the dictionary that contains all the information associated 
# with the cities and two city names and returns the distance (an integer) 
# between cities cityName1 and cityName2. If cityName1 and cityName2 are identical, 
# it returns 0. If either cityName1 or cityName2 are not in cityDataDict, it returns
# None.
#
###############################################################################    
def getDistance(cityDataDict, cityName1, cityName2):
    cityData1 = cityDataDict.get(cityName1)
    cityData2 = cityDataDict.get(cityName2)
    
    if cityData1 is not None and cityData2 is not None:
        if cityData1 == cityData2:
            return 0
        
        distanceCity1 = cityData1[2].get(cityName2)
        return distanceCity1
    
    else:
        return None
###############################################################################
#
# Specification: The function takes 3 paramaters:
#    
# cityDataDict: the dictionary that contains all the information associated 
# with the cities
# 
# cityName: is a name of a city
#
# r: is a non-negative floating point number
#
# The function returns a list of cities at distance at most r from the given city,
# cityName. This list can contain the names of cities in any order. If cityName is
# not a key in cityDataDict, the function should return None.
#
###############################################################################
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
        
