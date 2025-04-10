from app import create_app
import os

app = create_app()
print(f"Ubicación de templates: {os.path.abspath(app.template_folder)}")  # <-- Aquí

if __name__ == '__main__':
    app.run(port=5050, debug=True)