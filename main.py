from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\nGestión de Tareas")
        print("1. Agregar Tarea")
        print("2. Listar Tareas")
        print("3. Marcar Tarea como Completada")
        print("4. Eliminar Tareas Completadas")
        print("5. Exportar Tareas a JSON")
        print("6. Importar Tareas desde JSON")
        print("7. Salir")

        option = input("Selecciona una opción: ")

        if option == "1":
            title = input("Título de la tarea: ").strip()
            while not title:
                print("Error: El título no puede estar vacío. Inténtalo de nuevo.")
                title = input("Título de la tarea: ").strip()

            description = input("Descripción de la tarea: ").strip()
            while not description:
                print("Error: La descripción no puede estar vacía. Inténtalo de nuevo.")
                description = input("Descripción de la tarea: ").strip()
            
            manager.add_task(title, description)

        elif option == "2": 
            tasks = manager.get_all_tasks()  
            if not tasks:  
                print("No hay tareas registradas actualmente para mostrar.")
            else:
                manager.list_tasks()
            
        elif option == "3":
            while True:  
                try:
                    task_id = int(input("Ingrese ID de la tarea a marcar como completada: "))
                    break  
                except ValueError:
                    print("Error: Debes ingresar un número válido para el ID.")

            manager.mark_task_completed(task_id)
            
        elif option == "4":
            tasks = manager.get_completed_tasks()  
            if not tasks:  
                print("No hay tareas registradas completadas actualmente para eliminar.")
            else:
                manager.delete_completed_tasks()
   
        elif option == "5":
            tasks = manager.get_all_tasks()  
            if not tasks:  
                print("No hay tareas registradas actualmente para exportar en formato JSON.")
            else:
                manager.export_tasks_to_json()
            
        elif option == "6":
            manager.import_tasks_from_json()
        elif option == "7":
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
