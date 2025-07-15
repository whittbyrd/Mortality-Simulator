from sys import *
import csv
from random import random


class MortalityTable():
    """
    Contains a mortality table object.
    This stores information on the probability an individual dies in the next year
    given their current age.
    """

    def __init__(self,fileName):
        """
        Initialize a mortality table object.

        :param fileName: The name of the file where mortality information is stored. Must be a CSV file.
        """

        with open(fileName,'r') as file:
            csvData=list(csv.reader(file,delimiter=","))[1:]
            self.QxData={int(csvData[index][0]): float(csvData[index][1]) for index in range(len(csvData))}

    def getQx(self,age):
        """
        Finds the probability an individual dies in the following year given their current age
        using the mortality table data.

        :param age: Current age of the individual
        :return: Probability Qx they die in the following year (0<=Qx<=1)
        """

        return self.QxData.get(age,1.0)

class Person():
    """
    Simulates the life of one person starting from the age given. Deaths are randomized using the
    mortality table information. Their final age can be returned once their life has been simulated.
    A valid mortality table is needed.
    """

    def __init__(self,mortalityTable, age=30):
        """
        Initialize a person to simulate their life.

        :param age: Their current (initial) age
        :param mortalityTable: The mortality table whose data we are using
        """

        self.age=int(age)
        self.mortalityTable=mortalityTable
        self.isDead=False

    def runLife(self):
        """
        Simulate their full life. Once it is completed, their final
        age is left in the age parameter.

        :return: None
        """

        while not self.isDead:
            Qx=self.mortalityTable.getQx(self.age)
            if self.diedThisYear(Qx):
                self.isDead=True
            else:
                self.age+=1

    def diedThisYear(self,Qx):
        """
        Randomly decides if the individual dies in a current year. The probability that they do
        is given by the mortality table.

        :param Qx: The probability they die in the given year
        :return: Whether they die
        """

        num=random()

        if num<=Qx:
            return True
        return False

    def getAge(self):
        """
        Returns the current or final age of the individual

        :return: The age of the individual
        """

        return self.age


class Simulation():
    """
    Simulates a series of lives using mortality table information. It then reports
    statistics of these lives in a CSV file or prints graphics and charts describing the
    life distribution. A valid mortality table is required.
    """

    def __init__(self,age,simulations,mortalityTable):
        """
        Initialize the simulation to be used.

        :param age: The age at which the individuals should begin at
        :param simulations: The number of simulations to be ran
        :param mortalityTable: The mortality table data to us
        """

        self.age=age
        self.simulations=simulations
        self.mortalityTable=mortalityTable
        self.Ages={}

    def runSimulation(self):
        """
        Runs a number of individuals lives. Once these individuals lives are ran, their final age is
        stored for data collection.

        :return: None
        """

        for i in range(self.simulations):
            newPerson=Person(self.mortalityTable,self.age)
            newPerson.runLife()
            self.Ages[newPerson.getAge()]=self.Ages.get(newPerson.getAge(),0)+1

    def expectedAge(self):
        """
        Finds the age we expect an individual at the age given to live to.
        This is found by finding the average age the indidivuals in the
        simulation lived to.

        :return: The age we expect one individual to live to
        """

        ageSum=0
        for key in self.Ages:
            ageSum+=key*self.Ages[key]
        return ageSum/self.simulations

    def probDieBeforeAge(self,age):
        """
        Returns the probability the individual dies before a given age

        :param age: The age that we want to find a probability they live relative to
        :return: The proability P they live to that age (0<=P<=1
        """

        num=0
        for key in self.Ages:
            if key<age:
                num+=self.Ages[key]
        return num/self.simulations

    def standardDeviation(self):
        """
        Finds the standard deviation of the data set. This is done using the known
        standard deviation formula.

        :return: The standard deviation of the data
        """

        mean=self.expectedAge()
        variance=0
        for key in self.Ages:
            variance+=self.Ages[key]*(key-mean)**2
        variance/=self.simulations
        return variance**0.5

    def median(self):
        """
        Finds the median age that individuals in the simulation died at. This is doen by
        finding the 50th percentile.

        :return: The median age individuals died at in the simulation
        """

        keys=sorted(self.Ages.keys())
        numDeaths=0
        for age in keys:
            numDeaths+=self.Ages[age]
            if numDeaths>=self.simulations // 2:
                return age

    def writeToCSV(self):
        """
        Writes all previous statistics into a CSV file. This will create a new CSV file in
        the directory called MortalitySimulationOutput.

        :return: None
        """

        data={"Initial Age": self.age, "Number of Simulations": self.simulations,
              "Expected Age": self.expectedAge(),
              "Probability of Dying by Age  " + str(self.age+10): self.probDieBeforeAge(self.age+10),
              "Standard Deviation": self.standardDeviation(), "Median Age": self.median()}
        with open("MortalitySimulationOutput.csv",'w',newline="") as file:
            csvWriter=csv.writer(file,delimiter=',',)
            csvWriter.writerow(data.keys())
            csvWriter.writerow(data.values())



