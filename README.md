# Reconhecimento Facial com Mediapipe

👤 Sistema simples de reconhecimento facial com múltiplos ângulos

Este projeto usa Python e Mediapipe para capturar múltiplas poses do rosto de uma pessoa, salvar os vetores dos pontos faciais e depois reconhecer o rosto em tempo real com tolerância para diferentes ângulos e expressões.

---

🧩 Como Funciona
O usuário digita seu nome e posiciona o rosto em vários ângulos diante da câmera.

Cada pose é capturada e os pontos do rosto são salvos em um arquivo .json com o nome do usuário.

No reconhecimento, o sistema carrega todas as poses salvas e compara o rosto atual com todas elas.

Se a distância entre os pontos for menor que um limite configurável, o rosto é identificado com nome e retângulo.

Caso contrário, aparece como "Desconhecido".

---

📷 Exemplo de Funcionamento
Capture várias poses: frente, direita, esquerda, leve inclinação, etc.

Depois, ao abrir a câmera para reconhecimento, o sistema detecta o rosto mesmo se estiver com ângulos diferentes, exibindo um retângulo verde com seu nome quando reconhecido.

---

🛠 Requisitos
Python 3.7+

OpenCV

Mediapipe

Numpy

---

Na captura:

s → Salvar pose atual do rosto

q → Sair e salvar arquivo JSON com todas poses

No reconhecimento:

q → Sair da câmera

---

⚙️ Configurações
Ajuste o limite de distância para aumentar ou diminuir a rigidez do reconhecimento.

Capture múltiplas poses para melhorar a robustez ao variar o ângulo do rosto.

---

💡 Dicas
Quanto mais poses diferentes capturar, melhor o sistema reconhecerá rostos em ângulos variados.

Iluminação consistente ajuda na detecção.

Pode ser expandido para múltiplos usuários salvando arquivos diferentes por nome.

---

🚀 Aplicações
Controle de acesso simples com reconhecimento facial.

Sistemas de autenticação pessoal com múltiplas poses.

Base para projetos mais avançados com reconhecimento facial em Python.
