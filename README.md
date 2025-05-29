
1. Cada aluno deve:

2. Criar uma branch para sua página (ex: git checkout -b pagina-aluno1).

3. Editar seu HTML em templates/aluno1.html.

4. Adicionar estilos personalizados em static/style.css (se necessário).

5. Fazer commit e push da branch:

            Terminal:
            git add templates/aluno1.html
            git commit -m "Adiciona página do Aluno 1"
            git push origin pagina-aluno1
            Abrir um Pull Request no GitHub para merge na main.




6. Configuração do Ambiente Virtual (Python)
Para evitar conflitos de dependências, crie um ambiente virtual e instale o Flask:
# No terminal, na pasta do projeto:
python -m venv venv       # Cria o ambiente virtual
source venv/bin/activate  # Ativa o ambiente (Linux/Mac)
venv\Scripts\activate     # Ativa o ambiente (Windows)
pip install flask         # Instala o Flask