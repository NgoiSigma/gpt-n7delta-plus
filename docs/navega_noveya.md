from pathlib import Path

# HTML and Markdown blocks
html_block = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>НОВЕЯ: Архітектура осмисленого суверенітету</title>
</head>
<body>
    <h1>НОВЕЯ: Δ+ Навігаційна консоль</h1>
    <ul>
        <li><strong>Манифести</strong></li>
        <li><strong>FDL-громади</strong></li>
        <li><strong>Презентаційні матеріали</strong></li>
        <li><strong>Посилання на платформи</strong></li>
        <li><strong>Контактна інформація</strong></li>
    </ul>
    <p>📎 Репозиторій: <a href="https://github.com/NgoiSigma">NgoiSigma GitHub</a></p>
    <p>📎 Сайт: <a href="https://protonovea.wordpress.com/">protonovea.wordpress.com</a></p>
</body>
</html>
"""

markdown_block = """
# НОВЕЯ: Δ+ Навігаційна консоль

📌 Головні розділи:
- **Манифести**
- **FDL-громади**
- **Презентаційні матеріали**
- **Посилання на платформи**
- **Контактна інформація**

📎 [Репозиторій на GitHub](https://github.com/NgoiSigma)  
📎 [Сайт NOVEYA](https://protonovea.wordpress.com/)
"""

# Save to files
html_path = "/mnt/data/navega_noveya.html"
markdown_path = "/mnt/data/navega_noveya.md"

Path(html_path).write_text(html_block, encoding="utf-8")
Path(markdown_path).write_text(markdown_block, encoding="utf-8")

html_path, markdown_path
