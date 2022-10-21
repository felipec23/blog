import streamlit as st
import pandas as pd
import numpy as np

st.title("Ideas para convertir a Cúcuta en smart city")

st.subheader("1. Red de semáforos inteligentes")

with st.expander("Ver más"):
    tab1, tab2 = st.tabs(["Cómo", "Porqué"])

    with tab1:
        punts = """
        - Instalar cámaras económicas con modelos de inteligencia artificial que cuenten cuántos carros pasan por dónde y a qué horas.
        - Enviar esta información a los semáforos para que en tiempo real, y por sí solos, cambien la duración en rojo y en verde.
        
        """
        st.markdown(punts)

    with tab2:
        punts = """
        - Por trancones se pierde mucha plata.
        - Los conductores y los peatones se estresan.
        - En un trancón se producen más gases de efecto invernadero, que eventualmente calientan más la atmósfera.
        
        """
        st.markdown(punts)


st.subheader("2. Predecir corrupción en contratos con inteligencia artificial")

with st.expander("Ver más"):
    tab1, tab2 = st.tabs(["Cómo", "Porqué"])

    with tab1:

        punts = """
        - Programadores se reúnen con veedores ciudadanos e intentan transformar sus conocimientos en algo que un computador entienda.
        - Se despliega un algoritmo en la nube que constantemente está monitoreando los contratos subidos al SECOP, buscando patrones de corrupción.

        """


        st.markdown(punts)


    with tab2:

        punts = """
        - La inteligencia artificial puede hacer esto y más.
        - Se facilita el trabajo para medios de comunicación, pues estos podrían enfocarse en realizar las denuncias.
        - La corrupción nos quita mucha plata a todos. Siempre.
        """
        st.markdown(punts)


st.subheader("3. Detectar huecos con inteligencia artificial")

with st.expander("Ver más"):
    tab1, tab2 = st.tabs(["Cómo", "Porqué"])

    with tab1:

        punts = """
        - Cualquier conductor de carro que lo desee puede descargar una app en su celular, que, al apuntar hacia la calle, identificará automáticamente los huecos.
        - Cada vez que la app registre un hueco, enviará su ubicación y su foto a la nube.
        - Gracias a eso, se podrá tener un mapa de huecos actualizado por la misma comunidad.

        """


        st.markdown(punts)

        df = pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [7.89391, -72.507],
            columns=['lat', 'lon'])
        st.map(df)

    with tab2:

        punts = """
        - Los huecos pueden causar accidentes fatales.
        - La gente pierde plata por averías causadas por los huecos.
        - Permitiría que la comunidad monitoree con datos si la alcaldía de verdad está pavimentando sus calles.
        
        """
        st.markdown(punts)


st.subheader("4. Detectar tala de árboles ilegal con celulares viejos")

with st.expander("Ver más"):
    tab1, tab2 = st.tabs(["Cómo", "Porqué"])

    with tab1:

        punts = """
        - Se instalan celulares viejos en zonas de bosque que se quieran monitorear.
        - El celular puede detectar el sonido de una moto sierra a kilómetros y enviar un mensaje de alerta a las autoridades.
        - Se conecta a la red GSM. Se alimenta por energía solar. Se instala en lo alto de los árboles.
        """

        st.markdown(punts)

    with tab2:

        punts = """
        - La tala de árboles destruye hábitats enteros.
        - Amenaza a especies en peligro de extinción.
        - Genera un costo altísimo para la economía global, y es el mayor contribuyente al cambio climático.
        """
        st.markdown(punts)


st.subheader("5. Parques con sistemas de riego automáticos (instalados por niños y niñas)")

with st.expander("Ver más"):
    tab1, tab2 = st.tabs(["Cómo", "Porqué"])

    with tab1:

        punts = """
        - Con la ayuda de la comunidad se diseña el parque, se escogen las flores y se hacen excavaciones para instalar tubería y sensores. 
        - Se instala un sistema de riego automático con Arduino que se encargará de regar el pasto y las flores.
        - La gente del barrio ayudará a monitorear y a echarle fertilizantes.
        - Para 60 metros cuadrados de parque, el sistema no costaría más de 4 millones de pesos. 
        """

        st.markdown(punts)

    with tab2:

        punts = """
        - La literatura científica ha comprobado el diseño urbano de parques puede ayudar a reducir crímenes.
        - Niños y niñas pueden aprender a programar y aplicar sus conocimientos en la configuración e instalación de estos sistemas.
        - Se fortalecen los barrios y las comunidades, que unen esfuerzos y tiempo por una misma causa.
        """
        st.markdown(punts)


st.subheader("6. Sensores de calidad del aire en vehículos")

with st.expander("Ver más"):
    tab1, tab2 = st.tabs(["Cómo", "Porqué"])

    with tab1:

        punts = """
        - Conductores que lo deseen pueden conectar a su celular un aparato, que a través de una app, enviará datos de calidad del aire a la nube.
        - Dado que son conductores, eventualmente, se podrá ver un mapa de Cúcuta con barrios con peores condiciones para respirar.
        - El costo de un sensor es de 150.000 pesos."""

        st.markdown(punts)

    with tab2:

        punts = """
        - La mala calidad del aire en las ciudades mata lentamente a la gente.
        - No hay regulación y control sobre las emisiones de las industrias en la ciudad.
        - Se fortalece la veeduría ciudadana, pues se permitiría ejercer control con datos. """
        st.markdown(punts)

st.subheader("7. Contratos inteligentes para donaciones")

with st.expander("Ver más"):
    tab1, tab2 = st.tabs(["Cómo", "Porqué"])

    with tab1:

        punts = """
        - Los smart contracts son contratos incorruptibles, sin intermediarios y 100% transparentes, basados en blockchain.
        - Se crea una plataforma para que refugios de animales, fundaciones para migrantes y demás se registren y creen sus campañas.
        - La gente podrá donar a donde sea, sin comisiones y de forma directa a quien lo necesita."""

        st.markdown(punts)

    with tab2:

        punts = """
        - Hay muchas ONGs sin recursos en la ciudad, pero es difícil estar seguro de que las donaciones que uno hace de verdad les lleguen a ellos.
        - Es blockchain: es incorruptible. """
        st.markdown(punts)



st.title("Otras ideas")

punts = """
- Un lugar donde cualquiera pueda explorar de forma fácil cómo le va a Cúcuta en temas de indicadores.
- Una app (que las entidades lean) para reportar:
    * Dónde suelen inundarse más las calles.
    * Problemas de iluminación, malos olores y basuras.
    * Qué problemas tiene un barrio.
- Observatorios de: 
    * Prevención y alerta de enfermedades y brotes.
    * Turismo.
    * Asentamientos urbanos.
    * Accidentes de tránsito, movilidad y congestión vehicular.
    * Deserción escolar.


"""

st.markdown(punts)