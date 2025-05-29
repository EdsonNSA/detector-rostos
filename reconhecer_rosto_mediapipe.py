import cv2
import mediapipe as mp
import numpy as np
import json
import os

nome = input("Digite o nome para reconhecimento: ").strip()
caminho = f"rostos_salvos/{nome}.json"

if not os.path.exists(caminho):
    print(f"❌ Arquivo {caminho} não encontrado.")
    exit()

with open(caminho) as f:
    dados = json.load(f)

rostos_salvos = [np.array(rostos) for rostos in dados["rostos"]]

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def comparar(p1, p2):
    p1 = np.array(p1)
    p2 = np.array(p2)
    return np.linalg.norm(p1 - p2)

cap = cv2.VideoCapture(0)

limite_distancia = 0.40  # ajuste para ser mais ou menos rigoroso

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = face_mesh.process(frame_rgb)

    if resultado.multi_face_landmarks:
        rosto = resultado.multi_face_landmarks[0]
        pontos = [[p.x, p.y, p.z] for p in rosto.landmark]

        # comparar com todos os vetores salvos e pegar o menor dist
        distancias = [comparar(pontos, r) for r in rostos_salvos]
        menor_dist = min(distancias)

        h, w, _ = frame.shape
        pontos_2d = np.array([[p.x * w, p.y * h] for p in rosto.landmark])
        x1, y1 = np.min(pontos_2d, axis=0).astype(int)
        x2, y2 = np.max(pontos_2d, axis=0).astype(int)

        if menor_dist < limite_distancia:
            texto = f"{nome}"
            cor = (0, 255, 0)
        else:
            texto = "Desconhecido"
            cor = (0, 0, 255)

        cv2.rectangle(frame, (x1, y1), (x2, y2), cor, 2)
        cv2.putText(frame, texto, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, cor, 2)

    cv2.imshow("Reconhecimento facial", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
