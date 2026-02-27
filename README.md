# Identifying Earthquakes in Low-Cost Sensor Signals Contaminated with Vehicular Noise

<div align="center">
  <img width="550" height="245" alt="image" src="https://github.com/user-attachments/assets/cd94cb52-7203-475f-b63b-85b62aed30cc" />
</div>

Monitoring earthquakes is critical for public safety and disaster management. While low-cost seismic sensors allow for widespread, dense monitoring networks due to their affordability, they face a significant challenge in urban environments: **vehicular noise contamination**. This noise often masks or mimics seismic signals, leading to false positives.

This work addresses the challenge by proposing a hybrid neural network architecture that combines knowledge from professional seismic data and localized vehicular noise profiles.

## 🚀 Key Contributions

1. **Novel Architecture:** Development of an amalgamated DNN that fuses a model trained on professional seismic equipment with one trained on vehicular signals from low-cost sensors.

2. **Low-Cost Hardware:** Design of a seismic data logger approximately two orders of magnitude less expensive than professional equipment.

3. **Dataset Dissemination:** Creation of three discrete datasets: vehicular noise from low-cost sensors, ground truth seismic data from professional stations, and a two-fold synchronized dataset from both sensor types in close proximity.

4. **Performance:** Demonstrated significant improvements in effectiveness and efficiency over traditional stochastic differential models.

## 🛠 Methodology & Model Architecture

The core of the project is the **Amalgamated DNN**, which utilizes a dual-training approach to filter environmental "clutter".

### Neural Network Configuration

The classification model is based on a **Long Short-Term Memory (LSTM)** architecture consisting of five layers:

1. **Hidden LSTM Layer:** 64 units with ```return_sequences=True```.

2. **Flatten Layer:** Converts 3D output to a 2D tensor.

3. **Dense Layer 1:** 32 units using **ReLU** activation.

4. **Dense Layer 2:** 16 units using **ReLU** activation.

5. **Output Layer:** Dense layer with **Sigmoid** activation for probability scoring.

### The Amalgamation Process

* **VN_DNN:** Trained on vehicular signals captured by low-cost sensors to identify traffic patterns.

* **NOA_DNN:** Trained on high-fidelity earthquake signals from the National Observatory of Athens (NOA).

* **AM_DNN:** The final model, created by concatenating the pre-trained models into a single tensor to differentiate seismic events from noise.

## 📡 Hardware Specifications
The low-cost sensory equipment was developed at the [CMODLab](https://cmodlab.di.ionio.gr/) of Ionian University.

| Component | Specification |
| ---------- | ---------- |
| Microcomputer | Raspberry Pi 3 B+ |
| A/D Board | ADS1256 (24-bit high-speed precision) |
| Sensor | 3-axis Geophone (4.5 Hz, 380 Ohm) |
| Sampling Rate | 225 Hz - 3750 Hz (internally) |
| Power | Solar panel, battery, and step-down converter for autonomy |
| Connectivity | USB GSM-GPRS 4G modem |


## 📚 Citation
If you use this research or code in your work, please cite the original paper:

Plain Text
```
Agathos, L., Avgoustis, A., Avgoustis, N., Vlachos, I., Karydis, I., & Avlonitis, M. (2023). Identifying Earthquakes in Low-Cost Sensor Signals Contaminated with Vehicular Noise. Applied Sciences, 13(19), 10884. https://doi.org/10.3390/app131910884
```
BibTex
```bibtex
@Article{app131910884,
AUTHOR = {Agathos, Leonidas and Avgoustis, Andreas and Avgoustis, Nikolaos and Vlachos, Ioannis and Karydis, Ioannis and Avlonitis, Markos},
TITLE = {Identifying Earthquakes in Low-Cost Sensor Signals Contaminated with Vehicular Noise},
JOURNAL = {Applied Sciences},
VOLUME = {13},
YEAR = {2023},
NUMBER = {19},
ARTICLE-NUMBER = {10884},
URL = {https://www.mdpi.com/2076-3417/13/19/10884},
ISSN = {2076-3417},
ABSTRACT = {The importance of monitoring earthquakes for disaster management, public safety, and scientific research can hardly be overstated. The emergence of low-cost seismic sensors offers potential for widespread deployment due to their affordability. Nevertheless, vehicular noise in low-cost seismic sensors presents as a significant challenge in urban environments where such sensors are often deployed. In order to address these challenges, this work proposes the use of an amalgamated deep neural network constituent of a DNN trained on earthquake signals from professional sensory equipment as well as a DNN trained on vehicular signals from low-cost sensors for the purpose of earthquake identification in signals from low-cost sensors contaminated with vehicular noise. To this end, we present low-cost seismic sensory equipment and three discrete datasets that—when the proposed methodology is applied—are shown to significantly outperform a generic stochastic differential model in terms of effectiveness and efficiency.},
DOI = {10.3390/app131910884}
}
```
