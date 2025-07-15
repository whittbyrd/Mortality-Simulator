from MortalitySimulation import *

def main():
    mortalityTable=MortalityTable("MortalitySimulationInput.csv")
    simulation=Simulation(30,100000,mortalityTable)
    simulation.runSimulation()
    simulation.writeToCSV()


main()