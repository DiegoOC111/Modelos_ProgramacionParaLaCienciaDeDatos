import os
import torch
import torch.nn as nn
from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
import io
from torchvision import transforms

app = FastAPI(
    title="Pipeline de Detección de Neumonía",
    description="API local para la clasificación de radiografías de tórax utilizando el modelo base_cnn entrenado."
)

MODEL_PATH = "artifacts/models/base_cnn.pt"
MODEL_NAME = "base_cnn"
DEFAULT_THRESHOLD = 0.5

# Configuración del preprocesamiento según el contrato técnico
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406], 
        std=[0.229, 0.224, 0.225]
    )
])

# Variable global para almacenar el modelo en memoria
model = None

@app.on_event("startup")
def load_model():
    global model
    if not os.path.exists(MODEL_PATH):
        raise RuntimeError(f"No se encontró el archivo del modelo en la ruta: {MODEL_PATH}. Asegúrate de tener los artefactos generados.")
    
    try:
        # Intenta cargar el modelo completo serializado
        model = torch.load(MODEL_PATH, map_location=torch.device('cpu'))
        model.eval()
    except Exception as e:
        raise RuntimeError(f"Error al cargar el modelo binario: {str(e)}")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Validación del formato de archivo
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Formato de archivo inválido. Debe ser JPEG o PNG.")
    
    try:
        # Lectura de la imagen cargada
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))
        
        # Forzar el modo RGB tal como lo solicita el preprocesamiento esperado
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        # Aplicar transformaciones geométricas y de color
        tensor = preprocess(image).unsqueeze(0)
        
        # Ejecutar inferencia sin cálculo de gradientes
        with torch.no_grad():
            outputs = model(tensor)
            
            # Si el modelo termina en una capa densa lineal sin activación interna, aplicar sigmoide
            if isinstance(outputs, torch.Tensor):
                # Evaluación de probabilidad basada en salidas continuas o sigmoidales
                if outputs.shape[-1] == 1:
                    probability = torch.sigmoid(outputs).item()
                else:
                    # En caso de mapeo multiclase/softmax alternativo
                    probability = torch.softmax(outputs, dim=1)[0][1].item()
            else:
                probability = float(outputs)

        # Clasificación binaria basada en el umbral estándar
        predicted_label = "PNEUMONIA" if probability >= DEFAULT_THRESHOLD else "NORMAL"
        
        # Retorno estructurado bajo estricto cumplimiento del contrato de la API
        return {
            "predicted_label": predicted_label,
            "pneumonia_probability": round(probability, 4),
            "threshold": DEFAULT_THRESHOLD,
            "model_name": MODEL_NAME
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error durante el procesamiento de la imagen: {str(e)}")

@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": model is not None}