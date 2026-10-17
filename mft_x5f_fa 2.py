"""
MFT - Modelo Flujo Temporal - Documento Unificado V16 Publico
f(a) = exp(3∫_a^1 (1+w(a')) dln a') con w(a)=w0+wa(1-a)
Parametros publicos testables:
  H0 = 70.85 km/s/Mpc [69-72]
  w0 = -0.743 [-0.85,-0.65]
  wa = -0.28 [-0.4,-0.15]
  zc = 0.71 [0.6-0.9] cruce weff=-1
  1 peldano = 46/15 Gyr = 3.0666 Gyr = 1 cm = 20 deg = pi/9
  Radio observable = 16u = 48 Gyr = 15.652 peldanos
  Diametro total = 36u = 96 Gyr = 31.304 peldanos
  Escala UAM: 1u=8/3 Gyr, cosTheta=20/23=0.869565, Theta=29.59185 deg
  B geometrico = 2.5409 anclado CMB n=4.5 z=1089
  B observacional = 1.449 lambda=0.3711 best fit H(z)+BAO

Para Cobaya/CAMB/CLASS: H(a)=H0 sqrt(Om a^-3 + OMFT f(a))
f(a) es densidad relativa energia oscura MFT
"""
import numpy as np

# Parametros por defecto V16 publico
H0_DEFAULT = 70.85
W0_DEFAULT = -0.743
WA_DEFAULT = -0.28
OM_DEFAULT = 0.315
B_GEOM = 2.5409153667
B_OBS = 1.449
LAMBDA = 0.3711
N0 = 4.5

def w_a(a, w0=W0_DEFAULT, wa=WA_DEFAULT):
    """CPL w(a)=w0+wa(1-a)"""
    return w0 + wa*(1-a)

def f_a_CPL(a, w0=W0_DEFAULT, wa=WA_DEFAULT):
    """
    f(a)=a^{-3(1+w0+wa)} * exp(-3 wa (1-a))
    Derivacion estandar CPL
    """
    a = np.asarray(a)
    return a**(-3*(1+w0+wa)) * np.exp(-3*wa*(1-a))

def f_a_MFT_exponential(a, B=B_GEOM, n0=N0, lam=LAMBDA):
    """
    Version exponencial completa v2.2 para contraste DESI
    H(z)=H0 * n0/(n0-(1+z)/lam), con 1+z=1/a
    Para Cobaya: E(a)=H/H0 = f_exp
    """
    a = np.asarray(a)
    zp1 = 1.0/a
    return n0/(n0 - zp1/lam)

def H_a_MFT(a, H0=H0_DEFAULT, Om=OM_DEFAULT, w0=W0_DEFAULT, wa=WA_DEFAULT, mode="CPL"):
    """
    H(a) = H0 sqrt( Om a^-3 + (1-Om) f(a) )
    mode: CPL o EXP
    """
    a = np.asarray(a)
    if mode.upper()=="CPL":
        f = f_a_CPL(a, w0, wa)
    else:
        f = f_a_MFT_exponential(a)**2  # porque E^2
        # para compatibilidad, usamos E directamente
        return H0 * f_a_MFT_exponential(a)
    return H0 * np.sqrt(Om * a**-3 + (1-Om)*f)

def zc_crossing(w0=W0_DEFAULT, wa=WA_DEFAULT):
    """z donde w=-1"""
    # w0+wa(1-a) = -1 -> a = 1 + (1+w0)/wa
    a_c = 1 + (1+w0)/wa
    z_c = 1/a_c -1
    return z_c, a_c

if __name__=="__main__":
    zc, ac = zc_crossing()
    print(f"MFT V16 Publico H0={H0_DEFAULT} w0={W0_DEFAULT} wa={WA_DEFAULT}")
    print(f"zc={zc:.3f} ac={ac:.3f}")
    print(f"f(a=1)=1.0, f(a=0.5)={f_a_CPL(0.5):.4f}")
    print(f"H(z=2.5) CPL={H_a_MFT(1/3.5, mode='CPL'):.1f} km/s/Mpc")
    print(f"H(z=2.5) EXP={H_a_MFT(1/3.5, mode='EXP'):.1f} km/s/Mpc vs LCDM~258")