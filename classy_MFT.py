# Wrapper para CLASS para MFT
# Para usar con MontePython: w0_fld, wa_fld

def w_fld(a, w0=-0.743, wa=-0.28):
    return w0 + wa*(1-a)

# En .param file:
# w0_fld = -0.743
# wa_fld = -0.28
# Omega_L = 0.685
