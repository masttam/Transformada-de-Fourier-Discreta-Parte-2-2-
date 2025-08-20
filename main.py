import sys
from src import examen_p2

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py examen_p2")
        sys.exit(1)

    task = sys.argv[1]

    if task == "examen_p2":
        examen_p2.run()
    else:
        print(f"Tarea '{task}' no encontrada.")

if __name__ == "__main__":
    main()
