from qiskit import IBMQ
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor

IBMQ.enable_account('XXXXXX') # Your API token here
provider = IBMQ.get_provider(hub='ibm-q')

# Specifies the quantum device
backend = provider.get_backend('ibmq_qasm_simulator')

print('\nShor\'s Factorization Algorithm')
print('--------------------')
print('\nExecuting...\n')


factors = Shor(QuantumInstance(backend, shots=1000, skip_qobj_validation=False))
#The integer a needs to satisfy a < N and gcd(a, N) = 1
result_dict = factors.factor(N=21, a=2)
result = result_dict.factors

print(result)