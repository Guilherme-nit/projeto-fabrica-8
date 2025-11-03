# Vida & Cuidado – Sistema de Gestão de Médicos & Pacientes 🏥

## 📄 Descrição  
Este é um sistema web simples desenvolvido em Flask que permite visualizar listas de pacientes e de médicos, além de consultar detalhes individuais de cada um. O objetivo é oferecer uma interface clara, funcional e agradável para a gestão básica de dados de saúde.

## ⭐ Funcionalidades principais  
- Página inicial (rota `/`) com boas-vindas e explicação do sistema.  
- Lista de **pacientes** (rota `/pacientes`) com nome, idade, condição médica, imagem em miniatura.  
- Lista de **médicos** (rota `/medicos`) com nome, especialidade, anos de experiência, imagem em miniatura.  
- Detalhe de um paciente (rota `/paciente/<int:paciente_id>`) com informações completas e imagem em tamanho maior.  
- Detalhe de um médico (rota `/medico/<int:medico_id>`) com informações completas, imagem maior e (opcional) lista de pacientes atribuídos.  
- Tratamento de erro 404 para IDs que não existem (paciente ou médico).  
- Uso de templates Jinja2 para renderização das páginas HTML, com layout comum (`base.html`) para cabeçalho e rodapé.  
- Dados de exemplo usando listas de dicionários em Python — podendo ser estendido para banco de dados mais completo.

## 🛠 Tecnologias utilizadas  
- Python 3.x  
- Flask  
- Jinja2 (templating)  
- HTML / CSS (e, opcionalmente, Bootstrap para estilização)  

## 📁 Estrutura sugerida de pastas  
/projeto-vida-e-cuidado

│
├─ app.py
├─ requirements.txt
├─ templates/
│ ├─ base.html
│ ├─ index.html
│ ├─ listar_pacientes.html
│ ├─ detalhe_paciente.html
│ ├─ listar_medicos.html
│ └─ detalhe_medico.html
├─ static/
│ ├─ css/
│ └─ images/
└─ (opcional) dados/
└─ … ou banco de dados SQLite


## ⚙️ Instalação e execução  
1. Faça **fork** deste repositório para sua conta GitHub.  
2. Clone sua cópia (o fork) localmente:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
