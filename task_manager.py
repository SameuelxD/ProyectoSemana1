import json
from sqlalchemy.orm import Session
from models import Task
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

class TaskManager:
    def __init__(self):
        self.db_session = SessionLocal()

    def add_task(self, title, description):
        
        new_task = Task(title=title, description=description)
        self.db_session.add(new_task)
        self.db_session.commit()
        print("Tarea agregada exitosamente.")

    def list_tasks(self):
        
        tasks = self.db_session.query(Task).all()
        for task in tasks:
            status = "Completada" if task.completed else "Pendiente"
            print(f"ID: {task.id}, Título: {task.title}, Estado: {status}, Descripción: {task.description}")

    def mark_task_completed(self, task_id):
        
        task = self.db_session.query(Task).filter(Task.id == task_id).first()
        
        if not task:
            print("Tarea no encontrada.")
        elif task.completed:
            print("La tarea ya está marcada como completada.")
        else:
            task.completed = True
            self.db_session.commit()
            print("Tarea marcada como completada.")


    def delete_completed_tasks(self):
        
        completed_tasks = self.db_session.query(Task).filter(Task.completed == True)
        deleted_count = completed_tasks.delete()
        self.db_session.commit()
        print(f"Se eliminaron {deleted_count} tareas completadas.")

    def export_tasks_to_json(self, file_path="tasksExport.json"):

        tasks = self.db_session.query(Task).all()
        tasks_data = [{"id": t.id, "title": t.title, "description": t.description, "completed": t.completed} for t in tasks]
        with open(file_path, "w") as f:
            json.dump(tasks_data, f, indent=4)
        print(f"Tareas exportadas a {file_path}.")

    def import_tasks_from_json(self, file_path="tasksImport.json"):
        try:
            with open(file_path, "r") as f:
                tasks_data = json.load(f)  
            
            
            if not self.db_session:
                print("Error: La sesión de base de datos no está inicializada.")
                return

            
            for task in tasks_data:
                new_task = Task(
                    title=task.get("title", "Sin título"),
                    description=task.get("description", ""),
                    completed=task.get("completed", False)
                )
                self.db_session.add(new_task)

            
            self.db_session.commit()
            print(f"Se importaron {len(tasks_data)} tareas exitosamente.")

        except FileNotFoundError:
            print(f"Error: El archivo '{file_path}' no fue encontrado.")
        except json.JSONDecodeError:
            print(f"Error: El archivo '{file_path}' no tiene un formato JSON válido.")
        except Exception as e:
            print(f"Error al importar tareas: {e}")

    def get_all_tasks(self):
        return self.db_session.query(Task).all()

    def get_completed_tasks(self):
        return self.db_session.query(Task).filter(Task.completed == True).all()