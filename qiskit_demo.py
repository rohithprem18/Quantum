from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt


def basic_entangle_demo():
    qc = QuantumCircuit(2)
    qc.h(0)        # Put qubit 0 into superposition
    qc.cx(0, 1)    # Entangle qubit 0 with qubit 1
    qc.state_vector()

    sim=Aer.get_backend('aer_simplator')

    sim = Aer.get_backend('aer_simulator')
    tqc = transpile(qc, sim)
    result = sim.run(tqc).result()   # ✅ no execute()
    state = result.get_statevector()

    print("Statevector:", state)
    plot_bloch_multivector(state)
    plt.show()

    qc.draw('mpl')
    plt.show()


if __name__ == "__main__":
    basic_entangle_demo()
    