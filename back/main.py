from back.app import app

from back.routes import auth, forum

app.include_router(auth.router, prefix='/auth', tags=['Auth'])
app.include_router(forum.router, prefix='/forum', tags=['Forum'])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('back.main:app', host='127.0.0.1', port=8000, reload=True)