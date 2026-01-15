#!/usr/bin/env python3
"""Script minimal para reproducir la predicción EHT SgrA* (Teoría Σ).

Uso:
    python code/predict_sgrA.py [--M M_solar] [--B B_val]

Salida: imprime r_ph_sigma (valor numérico simple).
"""

import argparse
import numpy as np

def predict_r_ph_sigma(M_sgrA=4.3e6, B=1.6e-70):
    """Cálculo simplificado de ejemplo.

    Parámetros:
    - M_sgrA: masa en masas solares (float)
    - B: parámetro adimensional pequeño (float)

    Devuelve:
    - r_ph_sigma: valor escalado (float)
    """
    # Fórmula ejemplar (ajustar según derivaciones del PDF)
    r_ph_sigma = 5.2 * M_sgrA * (1.0 + 1e-3 * B)
    return r_ph_sigma

def main():
    parser = argparse.ArgumentParser(description="Predicción EHT SgrA* (Teoría Σ) — ejemplo reproducible")
    parser.add_argument('--M', type=float, default=4.3e6, help='Masa de SgrA* en masas solares')
    parser.add_argument('--B', type=float, default=1.6e-70, help='Parámetro B (valor pequeño)')
    args = parser.parse_args()

    r = predict_r_ph_sigma(M_sgrA=args.M, B=args.B)
    print(f"Predicción (r_ph_sigma) = {r:.6e}")

if __name__ == '__main__':
    main()
