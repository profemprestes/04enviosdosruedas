import asyncio
import os
from dotenv import load_dotenv
from browser_use import Agent, ChatOpenAI

# Cargar la API Key desde el archivo .env
load_dotenv()

nvidia_api_key = os.getenv("NVIDIA_API_KEY")

# Lista de URLs a explorar
urls_envios = [
    "https://www.enviosdosruedas.com/",
    "https://www.enviosdosruedas.com/contacto",
    "https://www.enviosdosruedas.com/cotizar",
    "https://www.enviosdosruedas.com/servicios/enviosflex",
    "https://www.enviosdosruedas.com/servicios/deposito-fulfillment",
    "https://www.enviosdosruedas.com/servicios/envios-lowcost",
    "https://www.enviosdosruedas.com/servicios/envios-express",
    "https://www.enviosdosruedas.com/servicios/envios-contrareembolso",
    "https://www.enviosdosruedas.com/servicios/plan-emprendedores",
    "https://www.enviosdosruedas.com/guias/envios-flex-mar-del-plata",
    "https://www.enviosdosruedas.com/nosotros/sobre-nosotros",
    "https://www.enviosdosruedas.com/nosotros/preguntas-frecuentes",
    "https://www.enviosdosruedas.com/nosotros/nuestras-redes",
    "https://www.enviosdosruedas.com/terminos-y-condiciones",
    "https://www.enviosdosruedas.com/politica-de-privacidad"
]

async def main():
    # Configuración del modelo con el endpoint de NVIDIA NIM
    llm = ChatOpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=nvidia_api_key,
        model="meta/llama-3.1-405b-instruct"
    )

    # Instrucción detallada para el agente
    instrucciones = f"""
    Navega secuencialmente por cada una de estas secciones del sitio web de Envíos Dos Ruedas:
    {', '.join(urls_envios)}

    En cada página realiza lo siguiente:
    1. Verifica que la página cargue correctamente.
    2. Extrae el título principal y los puntos clave de información o servicios ofrecidos.
    3. Si encuentras formularios (como en /contacto o /cotizar), identifica qué datos solicitan.

    Al finalizar el recorrido, entrega un resumen ejecutivo estructurado con los hallazgos de cada sección.
    """

    # Crear y ejecutar el agente
    agent = Agent(
        task=instrucciones,
        llm=llm
    )

    history = await agent.run()

    print("\n=== RESUMEN DE RECORRIDO ===")
    print(history.final_result())

if __name__ == "__main__":
    asyncio.run(main())