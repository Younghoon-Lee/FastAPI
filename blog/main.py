from fastapi import FastAPI

blog = FastAPI()

@blog.get('/')
def index():
    return "Main Page"