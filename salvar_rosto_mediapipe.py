import cv2
import mediapipe as mp
import json
import os

nome = input("Digite seu nome: ").strip()
os.makedirs("rostos_salvos", exist_ok=True)
caminho = f"rostos_salvos/{nome}.json"

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=True,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5
)

cap = cv2.VideoCapture(0)
print("Posicione o rosto em diferentes ângulos e aperte 's' para salvar cada pose.")
print("Quando terminar, aperte 'q' para sair.")

dados = {"nome": nome, "rostos": []}

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = face_mesh.process(frame_rgb)

    if resultado.multi_face_landmarks:
        for rosto in resultado.multi_face_landmarks:
            h, w, _ = frame.shape
            for ponto in rosto.landmark:
                x = int(ponto.x * w)
                y = int(ponto.y * h)
                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
        cv2.putText(frame, "Rosto detectado! Aperte 's' para salvar pose.", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Nenhum rosto detectado", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Captura múltiplos rostos", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s') and resultado.multi_face_landmarks:
        # Salvar vetor do rosto detectado
        pontos = [[p.x, p.y, p.z] for p in resultado.multi_face_landmarks[0].landmark]
        dados["rostos"].append(pontos)
        print(f"Pose salva. Total de poses: {len(dados['rostos'])}")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

if dados["rostos"]:
    with open(caminho, "w") as f:
        json.dump(dados, f)
    print(f"✅ Dados salvos em {caminho}")
else:
    print("Nenhuma pose salva, arquivo não criado.")
