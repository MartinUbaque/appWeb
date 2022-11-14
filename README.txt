PASOS PARA LA EJECUCIÓN Y EL USO DEL API DE REGRESIÓN LINEAL:

1. Ir a la carpeta del proyecto (appWeb)
2. Ejecutar comando: python -m pip install -–upgrade pip
3. Ejecutar comando: pip install -r requirements.txt 
4. Ejecutar comando: uvicorn main:app --reload

Para predecir un resultado de suicidio:
5. Abrir el siguiente link en un navegador: http://127.0.0.1:8000/docs#/default/make_predictions_predict_post
6. Hacer click en el botón "TRY IT OUT"
7. Ingresar un texto JSON con el siguiente formato:
{
  "text": "string" 
}
cambiando el "string" por el texto que quiere ingresar para predecir y hacer click en "EXCECUTE". La API responderá con el valor class predicho, el cual será 1 para positivo (suicidio) y 0 para negativo (no_suicidio).
