# 🎵 Mini MCP Server - Music Visualizer

**Explora tus canciones favoritas de Spotify y descubre nuevas recomendaciones de manera interactiva**.  
Este proyecto es un laboratorio de aprendizaje de **Python, Flask, Docker, vis.js y MCP Server**, pensado para practicar desarrollo backend y visualización de datos en tiempo real.

---

## Características:

- 🎨 **Grafo interactivo** de tus canciones “Me gusta”  
  - Nodos azules → canciones favoritas  
  - Nodos verdes → recomendaciones sugeridas (Claude Desktop o mock)  
  - Aristas moradas → representan relaciones entre canciones  
  - Grosor de aristas → refleja la fuerza de relación (artista, género, colaboraciones, BPM, popularidad)

- 🔗 Interacción con nodos:  
  - Click → abrir preview de la canción (YouTube/Spotify)  
  - Dar “like” → nodo se convierte en azul y se repinta el grafo

- 🐳 Todo dentro de **Docker**  
  - Credenciales seguras en `.env`  
  - Código montado con volúmenes → edita y prueba sin reconstruir imagen

---

## Objetivos de aprendizaje

- Crear **backend dinámico con Python + Flask**  
- Visualización interactiva con **vis.js**  
- Levantar y probar todo dentro de **Docker**  
- Integración con APIs externas (**Spotify**) y MCP (**Claude Desktop**)  
- Representar relaciones complejas visualmente  
- Iteración y depuración dentro de contenedores, sin tocar el entorno local


