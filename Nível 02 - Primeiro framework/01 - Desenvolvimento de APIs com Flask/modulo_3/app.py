from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

# @app.route("/")
# def hello_world():
#   return "Hello world!"

# @app.route("/about")
# def about():
#   return "Página sobre"

# CRUD
# Create, Read, Update and Delete = Criar, Ler, Atualizar, Deletar
# Tabela: Tarefa

tasks = []
task_id_control = 1

@app.route("/tasks", methods=["POST"])
def create_task():
  global task_id_control
  data = request.get_json()
  new_task = Task(id=task_id_control, title=data["title"], description=data.get("description", ""))
  task_id_control += 1
  tasks.append(new_task)
  print(tasks)
  # return 'Nova tarefa criada com sucesso'
  return jsonify({"message": "Nova tarefa criada com sucesso"}), 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
  """
  task_list = []
  for task in tasks:
    task_list.append(task.to_dict())
  """
  task_list = [task.to_dict() for task in tasks]
  
  output = {
    "tasks": task_list,
    "total_tasks": len(tasks)
  }
  
  return jsonify(output)

if __name__ == "__main__":
  app.run(debug=True)