# Teoría Σ — Saturación, fases y estructura real del universo

Una introducción breve, clara y accesible a la Teoría Σ y a las predicciones que pueden probarse con observaciones.

Resumen ejecutivo
-----------------
Teoría Σ propone que el espacio, la materia y la energía son manifestaciones de una misma sustancia finita. Este repositorio contiene los textos canónicos (PDFs) y código de ejemplo para reproducir predicciones testables, por ejemplo una estimación para la sombra de SgrA* (EHT).

Por qué leer esto
-----------------
- Idea central en 1 frase: el universo exhibe saturación geométrica que evita singularidades y genera fases observables.
- Predicciones testables: se incluyen cálculos y un script simple para obtener valores comparables con observaciones del EHT.
- Estado: borrador público, comentarios bienvenidos.

Accesibilidad y formatos
------------------------
- Documentos principales están en PDF (ver archivos en la raíz). Si necesitas una versión en texto plano, HTML, o un formato accesible (lectores de pantalla, fuente grande), abre un issue o contacta al autor; prepararé versiones alternativas.
- Los PDFs incluyen índice y referencias; el README ofrece resúmenes para evitar leer todo el PDF de entrada.

Resumen técnico breve (para lectores con prisa)
-----------------------------------------------
- Hipótesis: espacio-tiempo y materia son la misma sustancia con límites físicos reales.
- Consecuencias: ausencia de singularidades, conservación global emergente y señales observables en escalas astrofísicas.
- Predicción ejemplo: tamaño efectivo del fotón-sphere modificado por saturación — script reproducible en /code.

Cómo reproducir la predicción de SgrA* (rápido)
-----------------------------------------------
1. Clona el repositorio:
   git clone https://github.com/fernando1986figueroa-a11y/TEORIA-UNIFICADA-.-SATURACI-N-FASES-Y-ESTRUCTURA-REAL-DEL-UNIVERSO.git
2. Entra en la carpeta y crea un entorno virtual (opcional):
   python3 -m venv venv && source venv/bin/activate
3. Instala dependencias:
   pip install -r requirements.txt
4. Ejecuta el ejemplo:
   python code/predict_sgrA.py

Salida esperada
---------------
El script imprime un valor numérico para la cantidad r_ph_sigma (valor de ejemplo y unidad simplificada en el código). Esto es una demostración reproducible mínima; las derivaciones completas están en los PDFs.

Código y reproducibilidad
------------------------
- El código está en /code con un script ejecutable y dependencias en requirements.txt.
- Si quieres integrarlo en un paquete o añadir notebooks, por favor abre un issue o PR.

Cómo contribuir
---------------
- Abre issues para comentarios, preguntas o solicitudes de formato accesible.
- Para aportar código: create una rama, añade pruebas y abre un PR. Lee CONTRIBUTING.md para detalles.

Contacto y citación
-------------------
Fernando Figueroa — https://github.com/fernando1986figueroa-a11y
Si existe DOI, añádelo aquí para citación formal.

English short summary
---------------------
Teoría Σ (Sigma Theory) suggests a unifying picture where space, matter and energy are emergent aspects of a single finite substrate. This repo includes canonical PDFs and a minimal reproducible Python script to compute an observational prediction for SgrA*.