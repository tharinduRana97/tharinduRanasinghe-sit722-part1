import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://user:BISKgnK5sFOG1Uf489Xm1TWPh7wqCNXM@dpg-cqpmdcqj1k6c73dt3ki0-a.oregon-postgres.render.com/sit722postgre")

settings = Settings()
