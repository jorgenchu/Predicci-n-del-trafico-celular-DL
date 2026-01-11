# Reporte de Análisis de Tráfico de Internet
Fecha de generación: 2026-01-06 16:38:28

---

## 📊 Descripción del Dataset

Este análisis se basa en un conjunto de datos masivo de registros de detalles de llamadas (CDR) que capturan la actividad de la red móvil en un área urbana (habitualmente Milán).

- **Rango Temporal:** Los datos cubren desde el **31 de octubre de 2013** hasta el **1 de enero de 2014**.
- **Resolución Espacial:** El área está dividida en una cuadrícula de **100x100 celdas** (**10,000 GridIDs** en total), donde cada celda representa un área geográfica específica.
- **Tipos de Datos:**
  - `smsin`: Mensajes SMS recibidos.
  - `smsout`: Mensajes SMS enviados.
  - `callin`: Llamadas recibidas.
  - `callout`: Llamadas enviadas.
  - `internet`: Volumen de tráfico de navegación web y aplicaciones.
- **Unidades:** Los valores son medidas relativas de intensidad de tráfico (escaladas para privacidad y análisis), representando el volumen de actividad por intervalo de tiempo (cada 10 minutos).

---

## 📈 Análisis de Dinámicas de Tráfico

En este tipo de estudios masivos de datos, se suelen realizar los siguientes análisis para entender el comportamiento urbano:

1. **Análisis de Periodicidad:** Estudio de cómo el tráfico varía según el día de la semana (intra-semanal) y la hora del día (intra-diaria), identificando picos de actividad y "valles" nocturnos.
2. **Distribución Espacial (Hotspots):** Identificación de zonas críticas o "puntos calientes" donde la demanda de red es máxima (áreas comerciales, estaciones de transporte, zonas residenciales).
3. **Animación de "Respiración Urbana":** Visualización dinámica (3D) de la evolución temporal para observar cómo fluye la actividad por la ciudad a lo largo del día.
4. **Correlación de Servicios:** Análisis de cómo el uso de datos de Internet se relaciona con el uso de SMS o voz.

---

## Tráfico Semanal

Este gráfico muestra la evolución temporal de todos los servicios durante la semana seleccionada, permitiendo ver patrones de rutina diaria.

![Tráfico de Internet, SMS y Llamadas](internet_sms_call_traffic.png)

## Distribución Espacial de Internet

Visualización 3D de la carga de tráfico de Internet. Las elevaciones indican zonas de alta densidad de uso de datos.

![Distribución Espacial Internet](spatial_internet.png)

## Otras Distribuciones Espaciales

### SMS
![Distribución Espacial SMS](spatial_sms.png)

### Llamadas
![Distribución Espacial Llamadas](spatial_calls.png)
