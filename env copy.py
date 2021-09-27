import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "")
os.environ.setdefault("MONGO_URI", "mongodb+srv://julian:password@myfirstcluster.7m9mj.mongodb.net/task_manager?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "task_manager")