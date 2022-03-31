#!/usr/bin/env python
# coding: utf-8

import boto3
from braket.aws import AwsDevice
from braket.devices import LocalSimulator
from braket.circuits import Circuit
import math

# create the circuit
bell = Circuit().ry(0, math.pi/2).ry(1, math.pi/2).cphaseshift10(0,1,math.pi).ry(0,math.pi/2)
#bell=Circuit().h(0).cnot(0,1).cnot(0,2).cnot(0,3)
bell2 = Circuit().ry(1, math.pi/2).cphaseshift00(0,1,math.pi).ry(0,math.pi/2).ry(1, math.pi/2)
bell.add_circuit(bell2)
print(bell)
print(bell2)

# instantiate the local simulator
local_sim = LocalSimulator()

# run the circuit
result = local_sim.run(bell, shots=1000).result()
counts = result.measurement_counts
print(counts)
result = local_sim.run(bell2, shots=1000).result()
counts = result.measurement_counts
print(counts)





