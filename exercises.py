from qiskit import *
from qiskit.quantum_info import Statevector, random_statevector
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram,plot_bloch_multivector
import matplotlib.pyplot as plt
import numpy as np

## EXERCICE 1
titre = "Exercice 1"
circuit = QuantumCircuit(1)
circuit.h(0)
circuit.draw('mpl',filename=titre+" - Circuit")
#Visualiser les états
state = Statevector.from_int(0, 2)
state.draw('bloch',filename=titre+" - Etat initial")
state = state.evolve(circuit)
state.draw('bloch',filename=titre+" - Etat final")

## EXERCICE 2
titre = "Exercice 2"
circuit = QuantumCircuit(1)
circuit.h(0)
#Visualiser les états
circuit.draw('mpl',filename=titre+" - Circuit")
state = Statevector.from_int(1, 2)
state.draw('bloch',filename=titre+" - Etat initial")
state = state.evolve(circuit)
state.draw('bloch',filename=titre+" - Etat final")

## EXERCICE 3
titre = "Exercice 3"
circuit = QuantumCircuit(1)
circuit.x(0)
circuit.draw('mpl',filename=titre+" - Circuit")
#Visualiser les états
state = Statevector.from_int(0, 2)
state.draw('bloch',filename=titre+" - Etat initial")
state = state.evolve(circuit)
state.draw('bloch',filename=titre+" - Etat final")

## EXERCICE 4
titre = "Exercice 4"
circuit = QuantumCircuit(1)
circuit.x(0)
circuit.h(0)
circuit.draw('mpl',filename=titre+" - Circuit")
#Visualiser les états
state = Statevector.from_int(0, 2)
state.draw('bloch',filename=titre+" - Etat initial")
state = state.evolve(circuit)
state.draw('bloch',filename=titre+" - Etat final")

## EXERCICE 5
titre = "Exercice 5"
circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cnot(0,1)
circuit.draw('mpl',filename=titre+" - Circuit")
#Visualiser les états
state = Statevector.from_int(0, 2**2)
state.draw('qsphere',filename=titre+" - Etat initial")
state = state.evolve(circuit)
state.draw('latex_source')
state.draw('qsphere',filename=titre+" - Etat final")

## EXERCICE 6
titre = "Exercice 6"
circuit = QuantumCircuit(2)
circuit.h(0)
circuit.x(1)
circuit.cnot(0,1)
circuit.draw('mpl',filename=titre+" - Circuit")
#Visualiser les états
state = Statevector.from_int(0, 2**2)
state.draw('qsphere',filename=titre+" - Etat initial")
state = state.evolve(circuit)
state.draw('latex_source')
state.draw('qsphere',filename=titre+" - Etat final")

## EXERCICE 7
titre = "Exercice 7"
circuit = QuantumCircuit(3,3)
circuit.initialize('010')
init = Statevector(circuit)
circuit.x(0)
circuit.x(1)
final = Statevector(circuit)
circuit.measure([0, 1], [0, 1])
circuit.draw('mpl',filename=titre+" - Circuit")
init.draw('qsphere',filename=titre+" - Etat initial")
final.draw('qsphere',filename=titre+" - Etat final")
#Mesures des bits classiques
#Choix du simulateur
simulator = AerSimulator()
circuit.save_statevector()
#Compilation du circuit
compiled_circuit = transpile(circuit, simulator)
# Execution du circuit sur le simulateur
job = simulator.run(compiled_circuit, shots=1000)
# Agrégation des résultats
result = job.result()
counts = result.get_counts(compiled_circuit)
plot_histogram(counts,filename=titre+" - Mesures") 

## EXERCICE 8
titre = "Exercice 8"
circuit = QuantumCircuit(1,1)
psi = random_statevector(2)
circuit.initialize(psi,[0])
circuit.barrier()
final = Statevector(circuit)
circuit.measure(0,0)
circuit.draw('mpl',filename=titre+" - Circuit")
psi.draw('bloch',filename=titre+" - Etat initial")
print(psi.draw('latex_source'))
print('|a|² = ',np.abs(psi[0])**2,', |b|² = ',np.abs(psi[1])**2)
#Mesures des bits classiques
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=10000)
result = job.result()
counts = result.get_counts(compiled_circuit)
plot_histogram(counts,filename=titre+" - Mesures")

## EXERCICE 9
titre = "Exercice 9"
init = random_statevector(2)
qr= QuantumRegister(3, name="q")
crz, crx = ClassicalRegister(1, name="crz"), ClassicalRegister(1,name="crx")
teleportation_circuit = QuantumCircuit(qr, crz, crx)
teleportation_circuit.initialize(init,0)
teleportation_circuit.h(1)
teleportation_circuit.cnot(1,2)
teleportation_circuit.barrier()
teleportation_circuit.cnot(0,1)
teleportation_circuit.h(0)
teleportation_circuit.barrier()
teleportation_circuit.measure([0,1],[0,1])
teleportation_circuit.x(2).c_if(crx,1)
teleportation_circuit.z(2).c_if(crz,1)
teleportation_circuit.save_statevector()
teleportation_circuit.draw('mpl',filename=titre+" - Circuit")
#Visualiser les états par simulation du cicuit
compiled_circ = transpile(teleportation_circuit, simulator)
result = simulator.run(compiled_circ).result()
counts = result.get_counts(compiled_circ)
final = result.get_statevector(teleportation_circuit)
init.draw('bloch',filename=titre+" - Etat initial")
final.draw('bloch',filename=titre+" - Etat final")