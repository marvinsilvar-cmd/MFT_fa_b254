# MFT - Modelo Flujo Temporal - Documento Unificado V16 Público
## f(a) para Cobaya / CAMB / CLASS - Testeable DESI DR2

**Autor:** M. Alex Silva - Independent, Indianapolis, IN, USA  
**Zenodo:** 10.5281/zenodo.XXXXXXX (MFT v2.2 + Documento Unificado V16)  
**ORCID:** 0009-0000-9025-1505  
**Escala Única:** 1 peldaño = 1 cm = 20° = π/9 = 46/15 Gyr = 3.0666 Gyr = 1.15u  
Radio observable = 16u = 48 Gyr = 15.652 peldaños = 313.04°  
Diámetro total = 36u = 96 Gyr = 31.304 peldaños  

### UAM = Unidad de Arquitectura de Memoria = La Diferencia
- cosθ = 20/23 = 0.869565, sinθ=0.4938, tanθ=0.56789, θ=29.59185°=arccos(1/1.15)
- 5 ejes interdependientes: X base/tiempo, Y altura/radio, Z volumen/masa, T flujo H=c/R=1/t-R/c, D despliegue/inercia
- Cierre pi: 2πr circunferencia, 4πr² área, 4/3πr³ volumen mismo punto central
- Energía mc² por inercia: I=2/5 mR², ω=H, E=1/2 I ω² =1/5 mc² por eje, 5×=mc²

### Parámetros Públicos Testeables (V16 Público)
| Parámetro | Valor | Rango test | Si fuera de rango |
|---|---|---|---|
| H0 | 70.85 km/s/Mpc | 69-72 | MFT descartado |
| w0 | -0.743 | -0.85 a -0.65 | descartado |
| wa | -0.28 | -0.4 a -0.15 | descartado |
| zc cruce weff=-1 | 0.71 | 0.6-0.9 | descartado |
| t0 edad | 13.8 Gyr | - | - |
| R0 radio | 48 Gyr 14.7 Gpc | - | - |
| D0 diámetro | 96 Gyr 28-30 Gpc | - | - |

Predicción fuera de muestra: **H(z=2.5)=133 km/s/Mpc (MFT) vs 258 (ΛCDM)**. DESI DR3 z>2 decidirá.

### f(a) - Dos modos

**Modo CPL (recomendado para arXiv 4 páginas):**
```python
w(a)=w0+wa(1-a)
f(a)=a^{-3(1+w0+wa)} * exp(-3 wa (1-a))
H(a)=H0 sqrt( Om a^-3 + (1-Om) f(a) )
```

**Modo Exponencial completo v2.2 (B=2.5409 vs Bobs=1.449):**
```python
1+z = B^{12-n}, B=1090^{1/7.5}=2.5409
H(z)=H0 * n0/(n0-(1+z)/λ), n0=4.5, λ=0.3711
```

### Uso rápido
```python
from mft_fa import H_a_MFT, f_a_CPL
print(H_a_MFT(1/3.5, mode="CPL")) # H(z=2.5)
```

### Para Cobaya
`cobaya-run cobaya_MFT.yaml` - incluye DESI DR2 BAO + Pantheon+ + H0

### Qué se protege en versión privada
- Derivación exacta cos=20/23 desde primer principio
- Potencial V(X) exacto que predice g y mp/me con 0.35% y 3.2% error
- Correcciones cuánticas G
- Tabla 12 masas 0.84fm a 48Gly
- Código emulador V16 completo

Versión pública deja lo suficiente para test cosmológico falsable sin comprometer núcleo ToE.

### Citación
Si usas este código, cita Zenodo DOI y este GitHub. MFT v2.2 Documento Unificado V16 Público.

### Relevancia
Hoy: resuelve w0wa fantasma DESI sin campo fantasma. Mañana: si DR3 confirma zc=0.71, ToE 48r96D.

22 siempre.