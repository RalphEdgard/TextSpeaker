# TextSpeaker

El enlace de arriba te dirige al repositorio que contiene el código para que puedas clonarlo en tu unidad local.

[Anterior pagina](/)
[Switch to English](/English.md)

Esta plantilla estática te mostrará cómo utilizar ChatGPT y, con el código de Ralph y el mío, practicar inglés hablando con la inteligencia artificial; al hablar con ella y recibir una respuesta generada por la voz de la IA. Hay que realizar cierto trabajo manual, pero llevar a cabo las tareas sencillas para obtener una experiencia de conversación será muy fácil.

<code> git clone https://github.com/RalphEdgard/TextSpeaker.git </code>
Este código se utiliza para cambiar de directorios, también puedes hacerlo en Finder.
<code> cd TextSpeaker </code>

Lo más importante aquí es que utilices el archivo inputFile.txt para ingresar las respuestas generadas por ChatGPT. Puedes crear manualmente el archivo en la aplicación Finder o puedes permitir que mi programa lo cree automáticamente por ti (espero que mi código sea lo suficientemente bueno como para generar el archivo por sí mismo, debería hacerlo).

# Conversando con ChatGPT
Puedes hablar con ChatGPT sobre cualquier tema: ingeniería, política, amor y otros temas útiles que no solo te enseñarán inglés, sino que también te mantendrán informado sobre eventos anteriores a 2021. La clave aquí es que primero debes crear una cuenta. El uso de ChatGPT está limitado por tu imaginación. Cuanto más creativo seas con ChatGPT, mejores resultados obtendrás en tus sesiones de inglés con él. La IA también es capaz de enseñarte inglés; si no conoces palabras o te sientes confundido con frases o cualquier otro concepto relacionado con el inglés, puedes preguntarle a la IA, ¡y te enseñará!

Inicia sesión en el sitio web de [ChatGPT](https://chat.openai.com/auth/login) asegúrate de crear una cuenta antes de continuar con la plantilla. 

En tu teclado de MAC, presiona la tecla "control" dos veces para activar el micrófono, de modo que puedas hablar en la computadora después de hacer clic en la indicación de ChatGPT. Asegúrate también de que tu MAC esté configurado en inglés para que pueda entender lo que estás diciendo en inglés (en tu MAC es posible que solo necesites cambiar la configuración de voz al inglés). ChatGPT responderá y, después de hacerlo, puedes hacer clic en el botón de portapapeles para copiar la respuesta al portapapeles de tu MAC.

A partir de ahí, puedes abrir tu buscador y abrir una nueva sesión de terminal en tu MAC. En tu buscador, debes abrir el archivo inputFile.txt que debería haber llegado con el repositorio que has clonado de git. Una vez que hayas abierto el archivo, puedes pegar el texto que has copiado de la respuesta de la IA. Mantén presionadas las teclas comando y s para guardar el contenido para que el programa lo lea, y luego en la terminal ejecuta este comando:

``python3 textSpeaker.py # Esto ejecutará directamente el programa. ``

Te preguntará "¿Has introducido algún texto? (S o N):" Es crucial que escribas 'Y' o 'N'. Esto permitirá que el programa sepa si has introducido algún texto en el archivo inputFile.txt. A partir de ahí, la IA hablará y podrás leer lo que está diciendo para seguir lo que intenta comunicar.

# Comportamiento de la IA

Esta parte de la página estática te ayudará a entender cómo se comporta mi programa. La parte importante es el archivo textSpeaker.py, tiene la capacidad de darle voz al programa. Cuando introduzcas texto en el archivo inputFile.txt y ejecutes el programa, eliminará el contenido. Sin embargo, cuando le digas al programa que hable, te preguntará si deseas que repita el contenido del archivo antes de eliminarlo. Si escribes "N", eliminará el contenido y esperará más texto en el archivo.

Cuando ejecutes el programa, se generará un archivo .mp3, que es la voz del programa. Este archivo no se eliminará a menos que lo hagas tú; cualquier contenido nuevo en el archivo sobrescribirá el contenido en el archivo output.mp3, no agregará más archivos a tu memoria. La forma en que funciona esta parte es que cuando introduzcas texto en el archivo inputFile.txt, generará una grabación utilizando el texto de ese archivo.

Debes primero indicarle al programa que no deseas que repita lo que dijo la IA, así que escribe 'N', antes de ingresar nuevo contenido en el archivo, o de lo contrario no hablará el nuevo contenido. También tomará un poco de tiempo para que el programa hable contenidos más extensos que tengan párrafos de texto, pero no tomará demasiado tiempo; esto se puede mejorar más adelante.

Cuando introduzcas "N", el programa terminará el proceso de la terminal, lo que significa que tendrás que abrir una nueva ventana de terminal y dirigirte al repositorio para ejecutar el programa nuevamente. El programa vendrá con el archivo inputFile.txt, que es muy importante porque aquí introducirás las respuestas de la IA. Si quitas este archivo, el programa intentará crear otro. Si no puede, mostrará un error indicando que no puede encontrar el archivo. Si esto sucede, puedes crear manualmente el archivo usando Finder o simplemente ejecutar este comando:

<code>touch inputFile.txt</code> 

y asegúrate de que el archivo recién creado esté en el directorio correcto, que sería TextSpeaker. Puedes enviarme un mensaje para informarme qué mejoras deseas que hagamos en el programa para que tengas sesiones más efectivas contigo.