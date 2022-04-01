#!/usr/bin/env python
# coding: utf-8


import numpy as np

# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from ibm_quantum_widgets import *
from qiskit.providers.aer import QasmSimulator

# With only diamond
from qiskit_experiments.framework import ParallelExperiment
from qiskit_experiments.library import T1

# A T1 simulator
from qiskit.test.mock import FakeVigo
from qiskit.providers.aer import AerSimulator
from qiskit.providers.aer.noise import NoiseModel

class QuantumSensor():

    '''
    __init__() function sets up the noise model and the backend for the quantum simulator. The noise model is a simulator to the quantum computer
    whereas the backend is the actual quantum sensor. The experiements can be conducted on any one qubit of the quantum circuit. Delays depend
    on the materials of the sensor.s
    '''
    def __init__(self) -> None:
        self.noise_model = NoiseModel.from_backend(
                            FakeVigo(), thermal_relaxation=True, gate_error=False, readout_error=False
                            )
        self.backend = AerSimulator.from_backend(FakeVigo(), noise_model=self.noise_model)
        
    '''
    @parameter: qubit - the qubit to measure
    @parameter: delays - the iterator of time intervals to measure
    @return: the results of T1 experiment of the qubit
    '''
    def T1_experiment(self, qubit, delays):
        exp = T1(qubit=qubit, delays=delays)
        exp.set_transpile_options(scheduling_method='asap')
        exp_data = exp.run(backend=self.backend).block_for_results()
        return exp_data
    