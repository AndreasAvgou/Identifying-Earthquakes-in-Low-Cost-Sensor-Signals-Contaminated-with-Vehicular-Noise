# Identifying Earthquakes in Low-Cost Sensor Signals Contaminated with Vehicular Noise

<div align="center">
  <img width="550" height="245" alt="image" src="https://github.com/user-attachments/assets/cd94cb52-7203-475f-b63b-85b62aed30cc" />
</div>

An amalgamated deep neural network constituent of a DNN trained on earthquake signals from professional sensory equipment as well as a DNN trained on vehicular signals from low-cost sensors for the purpose of earthquake identification in signals from low-cost sensors contaminated with vehicular noise.

The study addresses the critical challenge of using affordable, low-cost seismic sensors in urban environments, where vehicular traffic creates significant "noise" that can be easily mistaken for seismic activity.

## 🚀 Key Contributions

1. **Amalgamated Deep Neural Network (DNN):** The core innovation is a composite architecture that combines:

    * A DNN trained on high-fidelity earthquake signals obtained from **professional-grade** sensory equipment.
    * A DNN trained on specific vehicular noise patterns captured directly by **low-cost** sensors.

2. **Noise-Robust Identification:** By merging these two specialized models, the system can accurately distinguish between actual seismic events and urban vibrations, even when signals are heavily contaminated by traffic noise.

3. **Hardware & Datasets:** The work introduces custom low-cost seismic hardware and provides three discrete datasets used to validate the methodology.

4. **Performance:** The proposed model significantly outperforms traditional stochastic differential models in both **effectiveness** (accuracy) and **efficiency** (computational speed), making it suitable for real-time monitoring.


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
