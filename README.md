# NYUAD-Hackathon-Team1
We are the QSPirates

## QvsPy, the virus for viruses.
We are developing a quantum sensor simulator for virus detection. Quantum Sensors have been used to increase Covid-19 detection accuracy. Such an outcome has the potential to decrease the trajectory of the pandemic, potentially decreasing numbers of deaths and patients. Our project aims to extend the benefit of high acccuracy of virus detection through quantum sensing to all viruses through creating a software package for scientists to use to detect the presence of viruses in input data. Having a simulator of the quantum sensor instead of the full quantum sensor hardware to detect the presence of viruses can save researchers time, effort, and the expense of materials. On a macroscale, the global community benefits from this as the increased accessibility for researchers to understand life-threatening viruses can lead to the increased quality of the global community's health.

### Files in repo:
- QASM.ipynb: we obtain the hamiltonian which gives us the mathematical expression to simulate the quantum sensor and the time evolution for the quantum circuit (done under pi/3 time)
- quantum-sensing-simulator.ipynb: quantum sensor simulator[^1]   
![alt text](https://github.com/Innanov/NYUAD-2022-QSPirates/blob/main/img/fig1.png?raw=true)   

*Control operations used in simulation*


### How to run:

```shell
pip install -r requirements.txt
```

## References

[^1]: Danilin, S., and M. Weides. "Quantum sensing with superconducting circuits." *arXiv preprint arXiv:2103.11022* (2021).
